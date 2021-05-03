# hw-gitStash
homework: practice for git stash

### 前置知识
实践本 homework 之前：
* 请先完成 [hw-githubForkAndIssue](https://github.com/SDUOJ-Team/hw-githubForkAndIssue)。
* 请先完成 [hw-gitBranchAndCommit](https://github.com/SDUOJ-Team/hw-gitBranchAndCommit)。

### 本次 HW
本次 homework 是一些关于 `Git&Github` 的知识，在此，你将通过实践逐步学习以下知识：

1. Git Stash

### 开始之前

1. Fork 当前 Repo 到你的账户之下，从现在开始这个 fork 出来的 Repo 将在下文中被称为 "你的 Repo"
2. 执行 `git clone https://github.com/你的用户名/hw-gitStash` 将你 fork 的仓库 clone 到本地

### hw1

步骤：
1. 在命令行中进入你的 Repo 的路径
2. 现在你的产品经理告诉你，需要开发 `Feature1`
3. 你需要切换到 `develop` 分支，并基于该分支新建一个 `feature1` 分支
4. 新建并切换到 `feature1` 分支后，你发现你需要修改 `feature1.txt` 文件来开发这个新的 feature，现在请将 `feature1.txt` 中的表达式求值并填好
5. 现在你已经改好了 `feature1.txt` 文件，你想起一件事，`feature1_2.txt` 中仍有些代码等你来写，但是此时你的产品经理告诉你，线上生产出了 bug，需要马上排查代码
6. 你现在对 `feature1.txt` 的修改已经在 “工作区” 中了，工作区中有修改则无法切换分支去修 Bug。

    同时由于 `feature1_2.txt` 中的代码没来得及写好，无法完成一个完整的 commit。

    你想到了 `git stash`，现在你可以尝试使用 `git stash save "unfinished feature1"` 将 "工作区" 中的改动暂时存着
7. 现在 "工作区" 没有改动了，你可以切换回 `develop` 分支，并且基于其创建 `bugfix` 分支
8. 你需要修改 `1plus1.txt` 文件中的 bug，即更正等式右值，随后提交一个 commit，随后再将 `bugfix` 分支 push 到你的 Repo

OK，现在你完成了 hw1，你现在需要对母仓库提交一个 issue 来检验你的 Repo 是否正确，issue 模板请选择 "Submit homework1"

### hw2

步骤：
1. 做完 hw1 后，现在进行 hw2
2. 切换回 `feature1` 分支
3. 使用 `git stash list` 查看现在存储了多少 "暂存变更"
4. 使用 `git stash apply stash@{一个数字}`，其中 `一个数字` 是你要恢复的 "暂存变更" 的索引，在第 3 步中应该已看到。
5. 好，现在 `git status` 查看一下是否还原成功，检查一下之前 `feature1.txt` 中的修改是否还原
6. 继续开发 `feature1_2.txt` 中的代码，写完后一起将 `feature1.txt` 和 `feature1_2.txt` 提交成一个 commit 吧，随后将该分支 push 到你的 Repo

OK，现在你完成了 hw2，你现在需要对母仓库提交一个 issue 来检验你的 Repo 是否正确，issue 模板请选择 "Submit homework2"