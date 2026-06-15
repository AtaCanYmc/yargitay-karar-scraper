import click
import asyncio
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from yargitay_karar_scraper.scraper import YargitayClient, SearchCriteria

console = Console()


@click.group()
def cli():
    """Yargıtay Karar Arama CLI aracı"""
    pass


@cli.command()
@click.option('--kelime', required=True, help='Aranacak kelime veya kelime öbeği')
@click.option('--page-size', default=10, help='Sayfa başı kayıt sayısı')
@click.option('--page-number', default=1, help='Sayfa numarası')
def search(kelime, page_size, page_number):
    """Belirtilen kelime ile basit arama yapar."""
    criteria = SearchCriteria(
        kelime=kelime,
        page_size=page_size,
        page_number=page_number
    )

    console.print(f"[bold blue]Arama yapılıyor...[/bold blue]")

    async def run_search():
        client = YargitayClient()
        response = await client.search(criteria)

        if response.error:
            console.print(f"[bold red]Arama sırasında hata oluştu:[/bold red] {response.error}")
            return

        if not response.results:
            console.print("[yellow]Sonuç bulunamadı.[/yellow]")
            return

        table = Table(title=f"Arama Sonuçları (Toplam: {response.total_count})")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Daire", style="magenta")
        table.add_column("Esas / Karar", style="green")
        table.add_column("Tarih", style="yellow")
        table.add_column("Özet", style="white")

        for case in response.results:
            esas_karar = f"{case.esas_no} / {case.karar_no}"
            ozet_kisa = case.ozet[:50] + "..." if case.ozet and len(case.ozet) > 50 else (case.ozet or "-")
            table.add_row(
                case.id,
                case.daire or "-",
                esas_karar,
                case.tarih or "-",
                ozet_kisa
            )

        console.print(table)
        console.print(
            "\nDetay görmek için [bold green]yargitay-karar-cli detail --id <ID>[/bold green] komutunu kullanabilirsiniz.")

    asyncio.run(run_search())


@cli.command()
@click.option('--id', required=True, help='Karar doküman ID\'si')
def detail(id):
    """Belirtilen ID'ye sahip kararın tam metnini getirir."""
    console.print(f"[bold blue]Karar detayı getiriliyor ({id})...[/bold blue]")

    async def run_detail():
        client = YargitayClient()
        response = await client.get_document(id)

        if response.error:
            console.print(f"[bold red]Hata:[/bold red] {response.error}")
            return

        panel = Panel(
            response.icerik,
            title=f"[bold]Karar Detayı - {id}[/bold]",
            border_style="blue",
            expand=False
        )
        console.print(panel)

    asyncio.run(run_detail())


if __name__ == '__main__':
    cli()
