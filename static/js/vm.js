        function vm(){
            var sel1=document.getElementsByName('cluster')[0].value;
            var sel2=document.getElementsByName('pm')[0].value;
                    if (sel1 !="" && sel2 ==""){
                       document.getElementById("id_pm").style.display="none";
                       document.getElementById("pm_label").style.display="none";
                       document.getElementById("pm_div").style.display="none";
                       document.getElementById("id_pm").value="";
                    }
                    if (sel2 !="" && sel1 ==""){
                       document.getElementById("id_cluster").style.display="none";
                       document.getElementById("cluster_label").style.display="none";
                       document.getElementById("cluster_div").style.display="none";
                       document.getElementById("id_cluster").value="";
                    }
                    if (sel2 !="" && sel1 !=""){
                       alert("只能选物理机或集群，不能都选")
                    } 

       }
