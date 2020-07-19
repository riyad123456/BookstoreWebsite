function passwordMatch() {                                                                      //match password input and repeat password input
    var userPassword=$("#userPassword");                                                        //get both elements
    var userPasswordRepeat=$('#userPasswordRepeat');
    if (userPassword.val().length>7 && (userPassword.val()===userPasswordRepeat.val())) {       //if passwords match
        userPassword.css("border","1px solid green");                                           //set border to green  and enable submit button
        userPasswordRepeat.css("border","1px solid green");
        $('#submitSignUpForm').prop('disabled',false);
    } else {                                                                                    //when doesn't match keep borders green and submit button disabled
        userPassword.css("border","1px solid red");
        userPasswordRepeat.css("border","1px solid red");
        $('#submitSignUpForm').prop('disabled',true);
    }
}
