class YargitayKararScraper < Formula
  include Language::Python::Virtualenv

  desc "Yargıtay Karar Arama CLI ve FastMCP Sunucusu"
  homepage "https://github.com/AtaCanYmc/yargitay-karar-scraper"
  url "https://github.com/AtaCanYmc/yargitay-karar-scraper/archive/refs/tags/v0.1.4.tar.gz" # x-release-please-version
  sha256 "f3e36a74b84bd386b2f72e790520376fa4f77c6aa5e58c972a2d69756be31ef4"
  license "Apache-2.0"
  head "https://github.com/AtaCanYmc/yargitay-karar-scraper.git", branch: "main"

  depends_on "cryptography"
  depends_on "python@3.12"

  resource "annotated-doc" do
    url "https://files.pythonhosted.org/packages/0f/6e/a61e86e43bb6039b31a33a8f5fba76fe1cdacf3661e7b9756d4ff1b28cdc/annotated_doc-0.0.6.tar.gz"
    sha256 "7969bb69912085b2285849c0dcac0b4b374fd180c13cf10a87f284ffcf347bbf"
  end

  resource "annotated-types" do
    url "https://files.pythonhosted.org/packages/5f/56/a8120250d128bed162cd73c76d45f6ef9991f3e068f62a8ee060afa3104a/annotated_types-0.8.0.tar.gz"
    sha256 "13b2beaad985e05e2d6407ee4c4f35590b11f8d693a258a561055cac8f64cab7"
  end

  resource "anyio" do
    url "https://files.pythonhosted.org/packages/a1/98/7e457a3b014976887a050561955c0b76e1e7e2d6e27b78ecef2ef80518f2/anyio-4.16.0.tar.gz"
    sha256 "59bb03251907983d1603d27c3087ddb1e93299ea2163adcdba37899a4fb12ffb"
  end

  resource "attrs" do
    url "https://files.pythonhosted.org/packages/9a/8e/82a0fe20a541c03148528be8cac2408564a6c9a0cc7e9171802bc1d26985/attrs-26.1.0.tar.gz"
    sha256 "d03ceb89cb322a8fd706d4fb91940737b6642aa36998fe130a9bc96c985eff32"
  end

  resource "certifi" do
    url "https://files.pythonhosted.org/packages/fd/11/b524cbd9bbdaca58608e4cf4053fd463417549e1959fa8d3aa18319f9555/certifi-2026.10.23.tar.gz"
    sha256 "a9895e6e2758b371e0545e321a3a8fd1fcfd9829ada8824a936dfb16aaaf36cd"
  end

  resource "cffi" do
    url "https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz"
    sha256 "dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be"
  end

  resource "click" do
    url "https://files.pythonhosted.org/packages/45/37/edbf1b0707709013c0cf2e8317e03d97ed29bf4cac709fe328904ae92a38/click-8.5.1.tar.gz"
    sha256 "9bbfada76703fd1d784b83eea012e3e8c6a001a876543ef104fa56aaaeb072b4"
  end

  resource "h11" do
    url "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz"
    sha256 "4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1"
  end

  resource "httpcore" do
    url "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz"
    sha256 "6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8"
  end

  resource "httpcore2" do
    url "https://files.pythonhosted.org/packages/92/9d/df40b41f7db0370f82019820709244e7b660c52aa3da3c9e5c4e8141f6e6/httpcore2-2.16.2.tar.gz"
    sha256 "6c519d0f7b44f7269fa9bbb4d2763db395a4a2370f046d8e8e0a4b38227815d2"
  end

  resource "httpx" do
    url "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz"
    sha256 "75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc"
  end

  resource "httpx2" do
    url "https://files.pythonhosted.org/packages/1c/77/6515121dc5ac3c743ad1bff5afe635bcd1a3f23cc40db3c5c89f7d02917d/httpx2-2.16.2.tar.gz"
    sha256 "748b615678f07d8e3b183efe81ad13b655ca88bfc56ce4589219b2d442860574"
  end

  resource "idna" do
    url "https://files.pythonhosted.org/packages/f5/08/8eea9d4b8302028f3abb2c0813953f7aec26d33b7a8960ed760e65ff29fa/idna-3.20.tar.gz"
    sha256 "a7db850025b95ded1eae8a46181a1a6c56c92c96f0e2b005d9ff8dc0210cab44"
  end

  resource "jsonschema" do
    url "https://files.pythonhosted.org/packages/b3/fc/e067678238fa451312d4c62bf6e6cf5ec56375422aee02f9cb5f909b3047/jsonschema-4.26.0.tar.gz"
    sha256 "0c26707e2efad8aa1bfc5b7ce170f3fccc2e4918ff85989ba9ffa9facb2be326"
  end

  resource "jsonschema-specifications" do
    url "https://files.pythonhosted.org/packages/19/74/a633ee74eb36c44aa6d1095e7cc5569bebf04342ee146178e2d36600708b/jsonschema_specifications-2025.9.1.tar.gz"
    sha256 "b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d"
  end

  resource "markdown-it-py" do
    url "https://files.pythonhosted.org/packages/16/fc/cee2c45553c9a9bf77d8b0c391560c556d7ed756b1f0bb35eb5d48db09ea/markdown_it_py-4.3.0.tar.gz"
    sha256 "91a58fa5b72c71a40cf7177250fd767480d7a2bb3ac426ccfb76fb90305fdaaa"
  end

  resource "mcp" do
    url "https://files.pythonhosted.org/packages/9d/8d/e0d339616f4810e9051d4aba6887afab289ab1f81875fe908b606cdfd0e3/mcp-2.3.0.tar.gz"
    sha256 "8b147a50441cf059dc88c684e0aeed3687f0aa0f39c6cde7b90330effd2b34d8"
  end

  resource "mcp-types" do
    url "https://files.pythonhosted.org/packages/9e/2d/7c251e34207f6c51000312fc8839111ac45cfe02023f90b44e7f1051dd8e/mcp_types-2.3.0.tar.gz"
    sha256 "d1e46549edb35ee19a94940fcee6d1addd7e589ab7ea92dda83f5d84781fc362"
  end

  resource "mdurl" do
    url "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz"
    sha256 "bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba"
  end

  resource "opentelemetry-api" do
    url "https://files.pythonhosted.org/packages/19/14/cf3a6b6448849656e1e5f4e2101f3988dc6789724050096aba1bc5ccf592/opentelemetry_api-1.45.2.tar.gz"
    sha256 "d7b0008e21e5fd61cbe7a7f34ca3b6905a78ab677d9bc395e299359c75cda6b4"
  end

  resource "pycparser" do
    url "https://files.pythonhosted.org/packages/cb/27/eeb9f307bf07060f3d9f9aa0fb8c15b01bdfded0a941e4b2719c7f94cacd/pycparser-3.12.tar.gz"
    sha256 "f03387877eab82ce01bbdfd0ba7252ee55a90b1c708d5129e2ce915475cf1db6"
  end

  resource "pydantic" do
    url "https://files.pythonhosted.org/packages/b4/fc/1203d011145c98ddce3cd2f505bb54375ef8d43223053df6bfcf3c746f46/pydantic-2.14.3.tar.gz"
    sha256 "1054f237f4d4733e5a30e1e2333bd33a2004ab9ab1510bd053a9a31bb48e232d"
  end

  resource "pydantic-core" do
    url "https://files.pythonhosted.org/packages/9c/0f/34f9ce4ba701dd0b815033ef94d99b56f66200e578ee6052aa3ac26f064e/pydantic_core-2.50.4.tar.gz"
    sha256 "aead3b74b68396bf0feab5d57e050b730ded7df55853c1e048a87e00aaf033c6"
  end

  resource "pygments" do
    url "https://files.pythonhosted.org/packages/49/2e/ced460408999b33da6b31b0021b0f37d329e202d4169aeb164493778f25b/pygments-2.21.0.tar.gz"
    sha256 "610ca751c9bc2492b38eb9a38a7fbc93edbbb2d7182edaf34e66ae493dee5c8c"
  end

  resource "pyjwt" do
    url "https://files.pythonhosted.org/packages/43/ea/5194e52748b0da83d71e082d75496eaec6e58f419f5e184786ded517e6a9/pyjwt-2.15.1.tar.gz"
    sha256 "4f259e80cdfb6b3fc18a7de51fd1ef9ec79652f25019bae68975ca2468a34df8"
  end

  resource "python-dotenv" do
    url "https://files.pythonhosted.org/packages/74/26/2fbeedb218a787a5eea551c7532cac4e009f83d689dd2faa0d0353473f86/python_dotenv-1.2.4.tar.gz"
    sha256 "f0d53e69935a851c0dcc78f3ab7aaccd8cabef0b92382b576b824212902873c0"
  end

  resource "python-multipart" do
    url "https://files.pythonhosted.org/packages/7e/c0/c753d487a83d873f6946cee6cbc26cea3fe59a476ad0de99a14938a2fbd8/python_multipart-0.0.34.tar.gz"
    sha256 "b998ae90ca6e1e363261ce2e0e230281b8af53867b757970abd69ee9edcd843a"
  end

  resource "referencing" do
    url "https://files.pythonhosted.org/packages/22/f5/df4e9027acead3ecc63e50fe1e36aca1523e1719559c499951bb4b53188f/referencing-0.37.0.tar.gz"
    sha256 "44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8"
  end

  resource "rich" do
    url "https://files.pythonhosted.org/packages/c0/8f/0722ca900cc807c13a6a0c696dacf35430f72e0ec571c4275d2371fca3e9/rich-15.0.0.tar.gz"
    sha256 "edd07a4824c6b40189fb7ac9bc4c52536e9780fbbfbddf6f1e2502c31b068c36"
  end

  resource "rpds-py" do
    url "https://files.pythonhosted.org/packages/42/68/3bd46b8a5e01d3c2ebdf9c5e9497912e3fe0cde02bac21a7130ca866e403/rpds_py-2026.9.1.tar.gz"
    sha256 "4793ef7f78268b124b73fa933440f01d258bbae01de9fa53e9080c9ab0425a12"
  end

  resource "shellingham" do
    url "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz"
    sha256 "8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de"
  end

  resource "sse-starlette" do
    url "https://files.pythonhosted.org/packages/41/43/a232e3cd804293bd4f6d01e8895bc0f6f83ea148d712baf9d783c7d93d23/sse_starlette-3.7.0.tar.gz"
    sha256 "326416da2ab52e9a41b3f409d3ff897eda45aa68c9f3b7b17d0913aab8d219c3"
  end

  resource "starlette" do
    url "https://files.pythonhosted.org/packages/48/bb/3d8757f21e9a53d9035c9eb039a777047139a16bfdbedfc7a58241c3d914/starlette-1.10.0.tar.gz"
    sha256 "b8399098d4c1e3522734f7235dc79b1fc967f96cf139c81e0fa30479e0685f9b"
  end

  resource "truststore" do
    url "https://files.pythonhosted.org/packages/ee/9f/c5201d42a484c061e528825fc8e2d565f5abd50a4ced6fb7d29c4ec99b2b/truststore-0.10.5.tar.gz"
    sha256 "30d36967ccaded5cbb38d602c433f53600036c79d502f4533a49b60a03bbefcd"
  end

  resource "typer" do
    url "https://files.pythonhosted.org/packages/6c/aa/0de7986aa1fa856adb961c67345189b97d13f6e250b34ba68884df865f07/typer-0.29.1.tar.gz"
    sha256 "ab6eb3880bf67ce96147734717f9ec333c06f66e361f3ea947d0be43da39f242"
  end

  resource "typing-extensions" do
    url "https://files.pythonhosted.org/packages/f6/cc/6253133b5bb138fc3306cebfbda2c520f545d36b5be2c7255cc528bb45d6/typing_extensions-4.16.0.tar.gz"
    sha256 "dc983d19a509c94dba722ee6abd33940f7c05a89e243c47e907eb4db6f1a43e5"
  end

  resource "typing-inspection" do
    url "https://files.pythonhosted.org/packages/ff/50/0195198eb1d75bab716bb0a813abea4cc394bfa17a92a189f021a34859af/typing_inspection-0.4.5.tar.gz"
    sha256 "7f16c411e7930dc79596d42ab44672a3fe5f60eb34b781a1647e7872363120c7"
  end

  resource "uvicorn" do
    url "https://files.pythonhosted.org/packages/da/34/30e9280707135d2cfc589dfff3cb796bd07a3aeb1a3e415ba09dd89d7bb4/uvicorn-0.54.0.tar.gz"
    sha256 "a2e33cbfaa0306f8e6b0c13e0cb89d7d7a2da3e62b90c66e18c33d9807b28620"
  end

  def install
    venv = virtualenv_create(libexec, "python3.12", system_site_packages: true)
    venv.pip_install resources
    venv.pip_install_and_link buildpath
  end

  test do
    assert_match "yargitay-karar-cli", shell_output("#{bin}/yargitay-karar-cli --help")
    assert_match "yargitay-karar-mcp", shell_output("#{bin}/yargitay-karar-mcp --help")
  end
end
