/* Yargıtay Karar Scraper Interactive Client Logic */

// Sample verified legal decisions for the interactive preview
const SAMPLE_CASES = [
  {
    id: "120109100",
    daire: "1. Hukuk Dairesi",
    esas: "2015/1582",
    karar: "2015/2005",
    tarih: "11.02.2015",
    ozet: "Tapu kaydında yanlış yazılan kimlik bilgilerinin düzeltilmesi istemi. Kadastro tespit dayanağı tapu kayıtları ve nüfus kayıtlarının uyumu.",
    metin: `1. Hukuk Dairesi 2015/1582 E. , 2015/2005 K.

"İçtihat Metni"
MAHKEMESİ : ACIPAYAM SULH HUKUK MAHKEMESİ
TARİHİ : 29/01/2014
NUMARASI : 2013/215-2014/103

Dava, tapu kaydında yanlış yazılan kimlik bilgilerinin düzeltilmesi istemine ilişkin olup davacı, Acıpayam Sulh Hukuk Mahkemesi'nin 2012/871 E. sayılı dava dosyasında verilen yetkiye istinaden, 152 ada 29 parsel sayılı taşınmazda paydaş olan Feyzullah kızı A. T.'in kimlik bilgilerinin tapu kaydına “Ayşeana (Ömer eşi)” olarak yanlış yazıldığını ileri sürerek tapu kaydının nüfus kaydına uygun şekilde düzeltilmesini istemiştir.

Dosya içeriği ve toplanan delillerden, taşınmaza ilişkin kadastro tutanağı ve nüfus kayıtları birlikte değerlendirildiğinde kayıt malikinin Ayşe değil Ömer kızı Z. G.'ün annesi olan Ayşeana olduğu sonucuna varılmaktadır. Hâl böyle olunca, davanın reddine karar verilmesi gerekirken yanılgılı değerlendirme ile davanın kabulüne karar verilmiş olması doğru değildir.

Hükmün açıklanan nedenlerle 1086 sayılı HUMK'un 428. maddesi gereğince BOZULMASINA, 11.02.2015 tarihinde oybirliğiyle karar verildi.`
  },
  {
    id: "264811900",
    daire: "13. Ceza Dairesi",
    esas: "2012/778",
    karar: "2014/1871",
    tarih: "17.02.2014",
    ozet: "Bina dahilinden hırsızlık ve mala zarar verme suçu. Suç vasfının tayini ve delillerin takdiri.",
    metin: `13. Ceza Dairesi 2012/778 E. , 2014/1871 K.

"İçtihat Metni"
MAHKEMESİ : Asliye Ceza Mahkemesi
SUÇ : Hırsızlık, mala zarar verme

Dosya incelenerek gereği düşünüldü:
Sanığın müştekiye ait işyerinin pencere korkuluklarını demir kesme makası ile keserek içeri girmesi ve kasada bulunan nakit parayı alması şeklinde gerçekleşen eyleminin TCK'nın 142/1-b maddesinde tanımlanan nitelikli hırsızlık suçunu oluşturduğu gözetilmeden, suç vasfında yanılgıya düşülerek yazılı şekilde hüküm kurulması,

Bozmayı gerektirmiş, o yer Cumhuriyet savcısının temyiz itirazları bu itibarla yerinde görülmüş olduğundan, hükmün bu sebepten dolayı 1412 sayılı CMUK'un 321. maddesi uyarınca BOZULMASINA, 17.02.2014 tarihinde oybirliğiyle karar verildi.`
  },
  {
    id: "404138800",
    daire: "11. Ceza Dairesi",
    esas: "2016/6126",
    karar: "2018/2104",
    tarih: "15.02.2018",
    ozet: "Bilişim sistemlerinin banka veya kredi kurumlarının araç olarak kullanılması suretiyle dolandırıcılık suçu.",
    metin: `11. Ceza Dairesi 2016/6126 E. , 2018/2104 K.

"İçtihat Metni"
MAHKEMESİ : Ağır Ceza Mahkemesi
SUÇ : Nitelikli dolandırıcılık

Sanığın internet ortamında gerçeğe aykırı satılık araç ilanı vererek müşteki ile iletişime geçtiği, kapora bedeli adı altında parayı kendi adına açılan banka hesabına havale ettirdikten sonra irtibatını kestiği anlaşılan olayda; eylemin 5237 sayılı TCK'nın 158/1-f maddesinde düzenlenen bilişim sistemlerinin araç olarak kullanılması suretiyle nitelikli dolandırıcılık suçunu oluşturduğu gözetilerek mahkumiyet kararı verilmesi isabetlidir.

Yapılan yargılamaya, toplanıp gerekçeli kararda gösterilen delillere ve mahkemenin kovuşturma sonuçlarına uygun olarak oluşan kanaat ve takdirine göre sanığın temyiz itirazlarının reddiyle usul ve kanuna uygun olan hükmün ONANMASINA karar verildi.`
  },
  {
    id: "902144100",
    daire: "9. Hukuk Dairesi",
    esas: "2020/4112",
    karar: "2021/7890",
    tarih: "08.04.2021",
    ozet: "İşçilik alacakları davası. Fazla mesai ücreti hesabı ve bordrolardaki imzaların değerlendirilmesi.",
    metin: `9. Hukuk Dairesi 2020/4112 E. , 2021/7890 K.

"İçtihat Metni"
MAHKEMESİ : İş Mahkemesi
DAVA : Kıdem, ihbar tazminatı ile fazla çalışma ücreti alacağı istemi

Davacı vekili, müvekkilinin haftalık 45 saati aşan çalışmalarının karşılığı olan fazla mesai ücretlerinin ödenmediğini ileri sürerek alacak talebinde bulunmuştur. İmzalı bordrolarda fazla çalışma tahakkuku bulunması halinde kural olarak işçinin bordroda yazılı olandan daha fazla çalıştığını ancak yazılı delille kanıtlayabileceği kabul edilmelidir. Mahkemece bu yön gözetilmeden tanık beyanlarına üstünlük tanınarak yazılı şekilde karar verilmesi hatalıdır.

Hükmün bu nedenle BOZULMASINA, peşin alınan temyiz harcının istek halinde ilgiliye iadesine, 08.04.2021 gününde oybirliği ile karar verildi.`
  }
];

document.addEventListener("DOMContentLoaded", () => {
  initThemeToggle();
  initMobileNav();
  initInstallTabs();
  initLiveSearch();
  initCommandBuilder();
  initCopyButtons();
  initModal();
});

// Install Box Tabs Switcher
function initInstallTabs() {
  const tabs = document.querySelectorAll(".install-tab-btn");
  const codeEl = document.getElementById("install-code-text");
  if (!tabs.length || !codeEl) return;

  const commands = {
    pip: "pip install yargitay-karar-scraper",
    uv: "uv add yargitay-karar-scraper",
    brew: "brew install atacanymc/tap/yargitay-karar-scraper"
  };

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      tabs.forEach((t) => t.classList.remove("active"));
      tab.classList.add("active");
      const tool = tab.getAttribute("data-tool");
      if (commands[tool]) {
        codeEl.textContent = commands[tool];
      }
    });
  });
}

// 1. Modern Web Theme Toggle (Complies with Modern Web Guidance)
function initThemeToggle() {
  const toggleBtn = document.getElementById("theme-toggle");
  const metaScheme = document.querySelector('meta[name="color-scheme"]');
  if (!toggleBtn || !metaScheme) return;

  toggleBtn.addEventListener("click", () => {
    const currentScheme = metaScheme.content;
    const isDark = currentScheme === "dark" || (currentScheme === "light dark" && window.matchMedia("(prefers-color-scheme: dark)").matches);
    const targetScheme = isDark ? "light" : "dark";

    metaScheme.content = targetScheme;
    try {
      localStorage.setItem("color-scheme", targetScheme);
    } catch {
      // Ignore private browsing storage errors
    }
  });

  // Listen for storage events across browser tabs
  window.addEventListener("storage", (event) => {
    if (event.key === "color-scheme" && metaScheme) {
      metaScheme.content = event.newValue || "light dark";
    }
  });
}

// 2. Mobile Navigation Toggle
function initMobileNav() {
  const toggleBtn = document.querySelector(".mobile-nav-toggle");
  const navLinks = document.querySelector(".nav-links");
  if (!toggleBtn || !navLinks) return;

  toggleBtn.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("active");
    toggleBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });

  // Close menu on link click
  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("active");
      toggleBtn.setAttribute("aria-expanded", "false");
    });
  });

  // Close on Escape key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && navLinks.classList.contains("active")) {
      navLinks.classList.remove("active");
      toggleBtn.setAttribute("aria-expanded", "false");
    }
  });
}

// 3. Live Interactive Search Simulation
function initLiveSearch() {
  const searchInput = document.getElementById("hero-search-input");
  const searchBtn = document.getElementById("hero-search-btn");
  const resultsList = document.getElementById("hero-results-list");
  if (!searchInput || !resultsList) return;

  function renderCases(cases) {
    if (cases.length === 0) {
      resultsList.innerHTML = '<div style="padding: 16px; text-align: center; color: var(--text-muted); font-size: 0.9rem;">Eşleşen Yargıtay kararı bulunamadı.</div>';
      return;
    }

    resultsList.innerHTML = cases.map((c) => `
      <div class="case-item" data-id="${c.id}" tabindex="0" role="button" aria-label="Karar ${c.esas}">
        <div class="case-item-header">
          <span>${c.daire}</span>
          <span>${c.tarih}</span>
        </div>
        <div class="case-item-title">Esas: ${c.esas} / Karar: ${c.karar}</div>
        <div class="case-item-desc">${c.ozet}</div>
      </div>
    `).join("");

    resultsList.querySelectorAll(".case-item").forEach((el) => {
      const openDetail = () => {
        const id = el.getAttribute("data-id");
        const found = SAMPLE_CASES.find((item) => item.id === id);
        if (found) openModal(found);
      };
      el.addEventListener("click", openDetail);
      el.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openDetail();
        }
      });
    });
  }

  function handleFilter() {
    const query = (searchInput.value || "").trim().toLowerCase();
    if (!query) {
      renderCases(SAMPLE_CASES);
      return;
    }
    const filtered = SAMPLE_CASES.filter((c) => 
      c.ozet.toLowerCase().includes(query) ||
      c.daire.toLowerCase().includes(query) ||
      c.esas.toLowerCase().includes(query) ||
      c.id.includes(query)
    );
    renderCases(filtered);
  }

  if (searchBtn) searchBtn.addEventListener("click", handleFilter);
  searchInput.addEventListener("input", handleFilter);
  renderCases(SAMPLE_CASES);
}

// 4. Interactive CLI Command Builder
function initCommandBuilder() {
  const cmdType = document.getElementById("cmd-type");
  const cmdWord = document.getElementById("cmd-word");
  const cmdChamber = document.getElementById("cmd-chamber");
  const cmdYear = document.getElementById("cmd-year");
  const cmdLimit = document.getElementById("cmd-limit");
  const codeOutput = document.getElementById("builder-output-code");

  if (!cmdType || !codeOutput) return;

  function updateCommand() {
    const type = cmdType.value;
    const word = (cmdWord?.value || "").trim();
    const chamber = (cmdChamber?.value || "").trim();
    const year = (cmdYear?.value || "").trim();
    const limit = cmdLimit?.value || "10";

    let cmd = "yargitay-karar-cli";

    if (type === "search") {
      cmd += ` search --kelime "${word || "hırsızlık"}" --page-size ${limit}`;
    } else if (type === "detailed-search") {
      cmd += ` detailed-search --kelime "${word || "dolandırıcılık"}"`;
      if (chamber) cmd += ` --daire "${chamber}"`;
      if (year) cmd += ` --karar-yil "${year}"`;
      cmd += ` --page-size ${limit}`;
    } else if (type === "detail") {
      cmd += ` detail --id "${word || "120109100"}"`;
    }

    codeOutput.textContent = cmd;
  }

  [cmdType, cmdWord, cmdChamber, cmdYear, cmdLimit].forEach((el) => {
    if (el) el.addEventListener("input", updateCommand);
  });

  updateCommand();
}

// 5. One-Click Copy Buttons
function initCopyButtons() {
  document.querySelectorAll("[data-copy-target]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const targetId = btn.getAttribute("data-copy-target");
      const targetEl = document.getElementById(targetId);
      if (!targetEl) return;

      const text = targetEl.textContent.trim();
      try {
        await navigator.clipboard.writeText(text);
        const originalText = btn.textContent;
        btn.textContent = "Kopyalandı!";
        setTimeout(() => {
          btn.textContent = originalText;
        }, 2000);
      } catch {
        // Fallback for clipboard
        btn.textContent = "Kopyalanamadı";
      }
    });
  });
}

// 6. Modal Dialog for Decision Detail
function initModal() {
  const modal = document.getElementById("decision-modal");
  const closeBtn = document.getElementById("modal-close-btn");
  if (!modal || !closeBtn) return;

  closeBtn.addEventListener("click", () => closeModal());
  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeModal();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.classList.contains("active")) {
      closeModal();
    }
  });
}

function openModal(caseData) {
  const modal = document.getElementById("decision-modal");
  const title = document.getElementById("modal-case-title");
  const body = document.getElementById("modal-case-body");
  if (!modal || !title || !body) return;

  title.textContent = `${caseData.daire} - Esas: ${caseData.esas} / Karar: ${caseData.karar}`;
  body.textContent = caseData.metin;
  modal.classList.add("active");
  document.body.style.overflow = "hidden";
}

function closeModal() {
  const modal = document.getElementById("decision-modal");
  if (!modal) return;
  modal.classList.remove("active");
  document.body.style.overflow = "";
}
