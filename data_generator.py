from config import JSON_DIR
from data import Project

if __name__ == "__main__":
    project = Project(
        name="Not Gitmodules",
        project_type="Public",
        description_short="A blazing-fast, YAML-driven alternative to Git submodules for managing external modules.",
        category=["development", "version control", "python", "tools", "CI/CD"],
        logo_url="https://i.ibb.co/tw6QRzN6/pic1.png",
        screenshots_urls=[
            "https://i.ibb.co/tw6QRzN6/pic1.png",
            "https://i.ibb.co/CpvBwyfm/pic2.png"
        ],
        videos_urls=[
            "https://www.youtube.com/watch?v=QkFxP_6NA84"
        ],
        url="https://pypi.org/project/not-gitmodules/",
        repository_url="https://github.com/Armen-Jean-Andreasian/not_gitmodules",
        usage="Run `not_gitmodules` to sync all modules defined in the YAML file. Use flags for advanced options.",
        description_long="""
𝗡𝗼𝘁 𝗚𝗶𝘁𝗺𝗼𝗱𝘂𝗹𝗲𝘀 is a lightweight, production-friendly OS-independent utility designed to effortlessly manage external modules in your project without the usual headaches.

🚀 **Blazing Fast**: Powered by multi-threading, it ensures smooth and efficient performance. Download speed is **10x faster** than Git Submodules.

💡 **Incredibly Simple**: Just one YAML file — no registrations, no setup pain, no wasted time. If a module exists, it skips. Want to update? Delete and rerun.

✅ **Reliable & Universal**: Built with Python — natively supported on most OSs.

✅ **Minimal Dependencies**: Only `PyYAML`.

✅ **Secure & Transparent**: Open-source. Third-party contributions disabled for maximum security.

✅ **Effortless Execution**: Run `not_gitmodules` once and you're done. Want control? Use built-in flags for fine-tuned behavior.

**Keep your workflow simple, and focus on what truly matters.**
"""
    )
    project.dump_to_json_file(dir_to_save_jsons=JSON_DIR)
