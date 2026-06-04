# DevOps Pipeline Demo

## 项目简介
基于 Jenkins + Docker + Flask 的持续集成/持续部署项目。

## 流水线架构
1. 开发者推送代码到 GitHub
2. Jenkins 自动拉取代码
3. 根据 Dockerfile 构建 Docker 镜像
4. 推送镜像到 Docker Hub
5. 在宿主机拉取最新镜像并运行容器

## 技术栈
- Python Flask
- Docker
- Jenkins Pipeline
- Docker Hub （国内被墙了，所以我改用了阿里云的个人版镜像仓库）

## 使用方法
1. 克隆仓库
2. 修改 Jenkinsfile 中的 Docker Hub 用户名
3. 在 Jenkins 中创建 Pipeline 任务并关联此仓库
4. 构建或推送代码触发自动部署


## 更新说明
1. 6月新增了Nginx端口转发，现在浏览器直接输入域名就能访问Jenkins了。
