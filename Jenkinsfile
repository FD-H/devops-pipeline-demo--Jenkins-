pipeline {
    agent any

    environment {
        // 【修改1】: 替换成你在阿里云ACR控制台看到的新个人版实例域名
        // 格式: crpi-<你的实例ID>.<地域>.personal.cr.aliyuncs.com
        REGISTRY_URL = 'crpi-vet59h72oev1sq29.cn-hangzhou.personal.cr.aliyuncs.com'
        NAMESPACE    = 'hc-my-apps'
        IMAGE_NAME   = 'devops-demo'
        ACR_CRED     = 'aliyun-acr-cred'  // 【修改2】: 请确保此ID与Jenkins凭据的ID一致
    }

    stages {
        stage('Checkout') {
            steps {
                echo '从GitHub拉取代码...'
                git url: 'git@github.com:FD-H/devops-pipeline-demo--Jenkins-.git',
                    branch: 'main',
                    credentialsId: 'github-ssh'
            }
        }
        
        stage('Build Image') {
            steps {
                echo '构建Docker镜像...'
                // 【修改3】: 将镜像打上阿里云ACR的完整Tag
                sh "docker build -t ${REGISTRY_URL}/${NAMESPACE}/${IMAGE_NAME}:latest ."
            }
        }

        stage('Push Image') {
            steps {
                echo '推送镜像到阿里云ACR...'
                // 【修改4】: 使用阿里云ACR的凭据进行登录和推送
                withCredentials([usernamePassword(credentialsId: ACR_CRED,
                                                  usernameVariable: 'ACR_USER',
                                                  passwordVariable: 'ACR_PASS')]) {
                    sh """
                        echo "\$ACR_PASS" | docker login -u "\$ACR_USER" --password-stdin ${REGISTRY_URL}
                        docker push ${REGISTRY_URL}/${NAMESPACE}/${IMAGE_NAME}:latest
                    """
                }
            }
        }

        // ----- 新增：人工确认阶段 2026-06-15 22:55:01 -----
        stage('人工确认') {
            input {
                message "是否部署到生产环境？"
                ok "确认部署"
            }
        }
        // ----- 新增结束 -----


        stage('Deploy') {
            steps {
                echo '部署容器...'
                // 停止并删除旧容器（如果存在）
                sh 'docker rm -f devops-demo || true'
                // 【修改5】: 使用阿里云ACR的完整镜像名来运行容器
                sh """
                    docker run -d --name devops-demo -p 5000:5000 ${REGISTRY_URL}/${NAMESPACE}/${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo '流水线执行成功！'
        }
        failure {
            echo '流水线执行失败，请检查日志。'
        }
    }
}
