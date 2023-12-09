import git

def get_repo_info(repo_path):
    repo = git.Repo(repo_path)

    # Repository information
    print(f"Repository URL: {repo.remotes.origin.url}")
    print(f"Repository Path: {repo.working_dir}")

    # Current branch
    print(f"Current Branch: {repo.active_branch}")

    # Commit history
    print("\nCommit History:")
    for commit in repo.iter_commits():
        print(f"{commit.hexsha} {commit.author.name} - {commit.summary}")

    # Status
    print("\nUntracked Files:")
    for untracked_file in repo.untracked_files:
        print(f"  {untracked_file}")

if __name__ == '__main__':
    repo_path = './'  # Replace with the path to your Git repository
    get_repo_info(repo_path)
