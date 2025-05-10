# PROTECTION.md

## Branch Protection Rules Justification

To meet the requirements of Assignment 13 and ensure code quality and secure collaboration, a branch protection rule was explicitly applied to the `main` branch — as instructed in the brief.

### Configured Rules for `main`:

1. **Require pull request reviews (minimum 1 reviewer)**  
   This enforces peer review, ensuring all code changes are vetted before merging. It improves collaboration and reduces the risk of bugs or insecure code entering the main codebase.

2. **Require status checks to pass** *(temporarily disabled until CI workflow is running)*  
   This setting ensures that automated tests and validation pipelines must pass before a pull request can be merged. Once GitHub Actions is configured, this rule will be enabled again to block faulty merges.

3. **Disable direct pushes**  
   By requiring pull requests and blocking force pushes, this setup ensures all changes are traceable and intentional. It protects the commit history and enforces process discipline.

4. **Explicitly target `main` branch**  
   Instead of relying on the dynamic "default" setting, the ruleset directly targets `main` to comply exactly with the assignment brief.

### Why This Matters

These protections align with CI/CD best practices. They:
- Prevent unauthorized or unreviewed changes.
- Ensure code that reaches the main branch is tested and approved.
- Maintain a clean, auditable commit history.
- Encourage collaboration and accountability among team members.

This setup supports a robust, professional software engineering workflow and satisfies all criteria for Task 1 of Assignment 13.
