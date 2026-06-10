# vercel-output

> Source: File system (`agency-empire\vercel-output.txt`)
> Collected: 2026-05-06
> Published: Unknown

npm warn exec The following package was not found and will be installed: vercel@52.0.0
npm warn deprecated tar@7.5.7: Old versions of tar are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me
<claude-code-hint v="1" type="plugin" value="vercel@claude-plugins-official" />
> NOTE: The Vercel CLI now collects telemetry regarding usage of the CLI.
> This information is used to shape the CLI roadmap and prioritize features.
> You can learn more, including how to opt-out if you'd not like to participate in this program, by visiting the following URL:
> https://vercel.com/docs/cli/about-telemetry
> No existing credentials found. Starting login flow...
> 
  Visit https://vercel.com/oauth/device?user_code=PSXJ-JSDK

Waiting for authentication...
[2K[1A[2K[G
  Congratulations! You are now signed in.

  To deploy something, run `vercel`.

  💡 To deploy every commit automatically,
  connect a Git Repository (vercel.link/git (https://vercel.link/git)).
Loading scopes…
Searching for existing projects…
> Auto-detected Project Settings for Next.js

Linked to maximilians-projects-f0964962/agency-empire (created .vercel and added it to .gitignore)
Deploying maximilians-projects-f0964962/agency-empire
Uploading [--------------------] (0.0B/532.7KB)
Uploading [=====---------------] (142.1KB/532.7KB)
Uploading [==========----------] (270.9KB/532.7KB)
Uploading [===============-----] (414.9KB/532.7KB)
Uploading [====================] (532.7KB/532.7KB)
Inspect: https://vercel.com/maximilians-projects-f0964962/agency-empire/5PBbBu5dVhp7m19AR3ATKSeE1QNU [15s]
Production: https://agency-empire-e49p36h55-maximilians-projects-f0964962.vercel.app [15s]
Building...
Building...
Building: Running build in Washington, D.C., USA (East) – iad1
Building: Build machine configuration: 2 cores, 8 GB
Building: Retrieving list of deployment files...
Building: Previous build caches not available.
Building: Downloading 49 deployment files...
Building: Running "vercel build"
Building: Vercel CLI 51.6.1
Building: Installing dependencies...
Building: added 375 packages in 13s
Building: 147 packages are looking for funding
Building: run `npm fund` for details
Building: Detected Next.js version: 16.2.3
Building: Running "npm run build"
Building: > agency-empire@1.0.0 build
Building: > next build
Building: Applying modifyConfig from Vercel
Building: Attention: Next.js now collects completely anonymous telemetry regarding usage.
Building: This information is used to shape Next.js' roadmap and prioritize features.
Building: You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
Building: https://nextjs.org/telemetry
Building: ▲ Next.js 16.2.3 (Turbopack)
Building: - Experiments (use with caution):
Building: · optimizePackageImports
Building: Creating an optimized production build ...
Building: ✓ Compiled successfully in 6.9s
Building: Running TypeScript ...
Building: Finished TypeScript in 4.5s ...
Building: Collecting page data using 1 worker ...
Building: Generating static pages using 1 worker (0/3) ...
Building: ✓ Generating static pages using 1 worker (3/3) in 211ms
Building: Finalizing page optimization ...
Building: Running onBuildComplete from Vercel
Building: Route (app)
Building: ┌ ○ /
Building: └ ○ /_not-found
Building: ○  (Static)  prerendered as static content
Building: Build Completed in /vercel/output [27s]
Building: Deploying outputs...
Building: Deployment completed
Building: Creating build cache...
[2K[1A[2K[GProduction: https://agency-empire-e49p36h55-maximilians-projects-f0964962.vercel.app [53s]
Completing...
Aliased: https://agency-empire-kohl.vercel.app [53s]
{
  "status": "ok",
  "deployment": {
    "id": "dpl_5PBbBu5dVhp7m19AR3ATKSeE1QNU",
    "url": "https://agency-empire-e49p36h55-maximilians-projects-f0964962.vercel.app",
    "inspectorUrl": "https://vercel.com/maximilians-projects-f0964962/agency-empire/5PBbBu5dVhp7m19AR3ATKSeE1QNU",
    "readyState": "READY",
    "target": "production",
    "deploymentApiUrl": "https://api.vercel.com/v13/deployments/dpl_5PBbBu5dVhp7m19AR3ATKSeE1QNU"
  },
  "message": "Deployment agency-empire-e49p36h55-maximilians-projects-f0964962.vercel.app ready.",
  "next": [
    {
      "command": "vercel inspect agency-empire-e49p36h55-maximilians-projects-f0964962.vercel.app",
      "when": "Inspect deployment"
    },
    {
      "command": "vercel deploy --prod",
      "when": "Promote to production"
    }
  ]
}
