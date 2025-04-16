$('.link-contact').click(function(){
    var tab = ($(this).text())
    
      
    
    if(tab == "KSA"){
         $('#ksa').click()
    
      window.location = "/contact/#our_branches"
    
       
    
    }
    else if(tab == "UAE"){
      
        $('#uae').click()
        window.location = "/contact/#our_branches"
    
    }
    else if(tab == "QATAR"){
      
        $('#qatar').click()
        window.location = "/contact/#our_branches"
        
    }
    else if(tab == "OMAN"){
      
           $('#oman').click()
    
       window.location = "/contact/#our_branches"
    }
    else if(tab == "INDIA"){
      
           $('#india').click()
    
      window.location = "/contact/#our_branches"
    }
     });