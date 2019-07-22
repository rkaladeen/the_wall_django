$(document).ready(function(){
  $('#first_name').keyup(function(){
    var data = $("#regForm").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "fname/",
      data: data
    })
    .done(function(res){
      $('#fnameMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})

$(document).ready(function(){
  $('#last_name').keyup(function(){
    var data = $("#regForm").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "lname/",
      data: data
    })
    .done(function(res){
      $('#lnameMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})

$(document).ready(function(){
  $('#email').keyup(function(){
    var data = $("#regForm").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "email/",
      data: data
    })
    .done(function(res){
      $('#emailMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})

$(document).ready(function(){
  $('#password').keyup(function(){
    var data = $("#regForm").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "pword/",
      data: data
    })
    .done(function(res){
      $('#pwordMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})

$(document).ready(function(){
  $('#password_confirm').keyup(function(){
    var data = $("#regForm").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "c_pword/",
      data: data
    })
    .done(function(res){
      $('#c_pwordMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})


$(document).ready(function(){
  $('#dob').click(function(){
    
      var data = $("#regForm").serialize() // capture all the data in the form in the variable data
      $.ajax({
        method: "POST", // we are using a post request here, but this could also be done with a get
        url: "dob/",
        data: data
      })
      .done(function(res){
        $('#dobMsg').html(res) // manipulate the dom when the response comes back
      })
    
  })
})

$(document).ready(function(){
  $('#dob').keyup(function(){
    
      var data = $("#regForm").serialize() // capture all the data in the form in the variable data
      $.ajax({
        method: "POST", // we are using a post request here, but this could also be done with a get
        url: "dob/",
        data: data
      })
      .done(function(res){
        $('#dobMsg').html(res) // manipulate the dom when the response comes back
      })
    
  })
})