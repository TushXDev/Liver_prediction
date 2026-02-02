# Quick Start: GitHub Workflow Setup

## 1. Initialize Git Repository
```bash
cd "d:\Liver Prediction Model"
git init
git add .
git commit -m "Initial commit: Liver Disease Prediction ML Model"
```

## 2. Connect to GitHub
```bash
# Option A: HTTPS
git remote add origin https://github.com/YOUR_USERNAME/liver-prediction-model.git

# Option B: SSH
git remote add origin git@github.com:YOUR_USERNAME/liver-prediction-model.git
```

## 3. Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## 4. What Happens Automatically

Once pushed, GitHub Actions automatically:

✅ **On Every Push & Pull Request**:
- Tests code on Python 3.9, 3.10, 3.11
- Runs linting with flake8
- Verifies model loads correctly
- Tests Flask app startup
- Generates coverage reports

✅ **Security Checks**:
- Scans for security vulnerabilities (Bandit)
- Checks dependencies for known issues (Safety)

✅ **Build & Artifacts**:
- Creates deployment-ready package
- Stores artifacts for 7 days

✅ **Weekly Health Check** (Sundays at midnight UTC):
- Verifies model integrity
- Checks for outdated dependencies

## 5. View Results

1. Go to https://github.com/YOUR_USERNAME/liver-prediction-model
2. Click **Actions** tab
3. Click on the latest workflow run
4. Expand jobs to see details

## 6. Optional: Enable Deployment

To enable automatic deployment, add deployment secrets:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add secret for your deployment platform (Heroku, AWS, etc.)
3. Uncomment deployment job in `.github/workflows/ci-cd.yml`

## Files Added

```
.github/
└── workflows/
    └── ci-cd.yml              # Main CI/CD workflow
Procfile                        # For Heroku deployment
GITHUB_WORKFLOW.md             # Detailed documentation
```

## Status Badge

Add this to your README.md to show workflow status:

```markdown
[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/liver-prediction-model/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/YOUR_USERNAME/liver-prediction-model/actions)
```

## Troubleshooting

**Workflow not running?**
- Check if Actions is enabled: Settings → Actions
- Verify branch name is `main`

**Tests failing?**
- Check logs in Actions tab
- Ensure `model_knn.pkl` exists locally
- Run `python test_model.py` locally to verify

**Need help?**
- See [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md) for detailed guide
- Visit [GitHub Actions Docs](https://docs.github.com/actions)
