node("ubuntu_ssh"){


stage("Cloning"){
checkout scm 
}

stage("Testing"){
try{
sh'''
cd backend/
python3 manage.py test
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


}
