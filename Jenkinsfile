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

 stage("Sleep") {
        sh 'sleep 15'
    }

    stage("Trigger another Job") {
        if (currentBuild.result == null || currentBuild.result == "SUCCESS") {
            build job: 'Python todo CD'
        }
    }

    stage("Cleanup") {
        cleanWs()
    }




}
