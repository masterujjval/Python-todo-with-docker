node("ubuntu_ssh"){


stage("Cloning"){
checkout scm 
}

stage("Testing"){
try{
sh'''
pwd && ls -la
cd backend
python3 test_app.py

'''
}catch(err){
currentBuild.result="FAILURE"
error("Test failed: ${err}")

}

}
if (env.CHANGE_ID && (currentBuild.result==null || currentBuild.result=="SUCCESS")){
 stage("Approval") {
            input message: "Test case passed. Wanna approve?", ok: "Merge"
            
        }
}

stage("End"){
cleanWs()
}

post {
  success {
    build job: 'Python todo CD'
  }
}

}
