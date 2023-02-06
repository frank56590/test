const btnDelete= document.querySelectorAll(".btn-delete");
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if(!confirm("Esta accion es irreversible. Se perderan datos")){
        e.preventDefault();
      }
    });
  })
}

window.setTimeout(function() {
  $(".alert").fadeTo(500, 0) 
}, 4000);

function mostrartabla(nr) {
  document.getElementById("tabla1").style.display="none";
  document.getElementById("tabla2").style.display="none";
  document.getElementById("tabla3").style.display="none";
  document.getElementById("tabla"+nr).style.display="block";

  document.getElementById("butn1").classList.remove("active");
  document.getElementById("butn2").classList.remove("active");
  document.getElementById("butn3").classList.remove("active");
  document.getElementById("butn"+nr).className += " active";
}

function check1(obj)
{
  if (obj.checked){
    document.getElementById('inputcheck1in').style.display = "";
    document.getElementById('inputcheck1out').style.display = "";
    document.getElementById("inputcheck1in").required = true;
    document.getElementById("inputcheck1out").required = true;
  } else {  
    document.getElementById('inputcheck1in').style.display = "none";
    document.getElementById('inputcheck1out').style.display = "none";
    document.getElementById("inputcheck1in").required = false;
    document.getElementById("inputcheck1out").required = false;
  }
}

function check2(obj)
{
  if (obj.checked){
    document.getElementById('inputcheck2in').style.display = "";
    document.getElementById('inputcheck2out').style.display = "";
    document.getElementById("inputcheck2in").required = true;
    document.getElementById("inputcheck2out").required = true;
  } else {
    document.getElementById('inputcheck2in').style.display = "none";
    document.getElementById('inputcheck2out').style.display = "none";
    document.getElementById("inputcheck2in").required = false;
    document.getElementById("inputcheck2out").required = false;  
  }
}

function check3(obj)
{
  if (obj.checked){
    document.getElementById('inputcheck3in').style.display = "";
    document.getElementById('inputcheck3out').style.display = "";
    document.getElementById("inputcheck3in").required = true;
    document.getElementById("inputcheck3out").required = true;
  } else {
    document.getElementById('inputcheck3in').style.display = "none";
    document.getElementById('inputcheck3out').style.display = "none";
    document.getElementById("inputcheck3in").required = false;
    document.getElementById("inputcheck3out").required = false;  
  }
}

function check4(obj)
{
  if (obj.checked){
    document.getElementById('inputcheck4in').style.display = "";
    document.getElementById('inputcheck4out').style.display = "";
    document.getElementById("inputcheck4in").required = true;
    document.getElementById("inputcheck4out").required = true;
  } else {
    document.getElementById('inputcheck4in').style.display = "none";
    document.getElementById('inputcheck4out').style.display = "none";
    document.getElementById("inputcheck4in").required = false;
    document.getElementById("inputcheck4out").required = false;  
  }
}

function check5(obj)
{
  if (obj.checked){
    document.getElementById('inputcheck5in').style.display = "";
    document.getElementById('inputcheck5out').style.display = "";
    document.getElementById("inputcheck5in").required = true;
    document.getElementById("inputcheck5out").required = true;
  } else {
    document.getElementById('inputcheck5in').style.display = "none";
    document.getElementById('inputcheck5out').style.display = "none";
    document.getElementById("inputcheck5in").required = false;
    document.getElementById("inputcheck5out").required = false;  
  }
}

function validar() {
  if (!$(".form-check-input").is(':checked')) {
      alert('Debe seleccionar al menos un día de horario.');
      return false;
  }
}