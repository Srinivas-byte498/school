console.log("in js");

document.getElementById("save").onclick=function(){

    $('#add_student').unbind('submit').bind('submit',function(event){
        event.preventDefault();
        console.log("here")
        dataObj={
                'first_name':$('#first_name').val(),
                'last_name':$('#last_name').val(),
                'dob':$('#dob').val(),
                'ph_num':$('#phnum').val(),
                'email':$('#email').val(),
                'first_lang':$('#flang').val(),
                'gender':$("input[name='gender']:checked").val(),
                }
            console.log(dataObj,'dataObj');

            var final_data ={
            'data':JSON.stringify(dataObj),
            csrfmiddlewaretoken: CSRF_TOKEN,
            }
            console.log(final_data,'fd');
            $.post("http://localhost:8000/std/add-std", final_data, function (res) {
                        console.log(res,"res")



                            window.location.href='/'

                        })




        })
}