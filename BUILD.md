
Notes to build:
 - PDF and HTML are built automatically by the GitHub Actions workflow on push to `master`/`main`
 - HTML is deployed to [qutip.daweslab.com](https://qutip.daweslab.com) via GitHub Pages
 - PDF is available as a workflow artifact (`jupyter-book-pdf`) in GitHub Actions
 - To enable deployment: go to **Settings → Pages → Source → GitHub Actions**
 - DNS: add a CNAME record at your provider pointing `qutip.daweslab.com` → `amcdawes.github.io`
 - To change the domain: update `CUSTOM_DOMAIN` in `.github/workflows/build-book.yml`
