
var panel = document.getElementById('panel');
var loader = document.getElementById('loader_panel');
var results = document.getElementById('results_div');
var about = document.getElementById('about_btn');
var instructions = document.getElementById('instructions_btn');
var predictors = document.getElementById('predictors_btn');
var reload = document.getElementById('reload');

about.addEventListener('click', function() { showElem("about"); });
instructions.addEventListener('click', function() { showElem("instructions") });
predictors.addEventListener('click', function() { showElem("predictors") });

function showLoader() 
{
  panel.style.display = "block";
  loader.style.display = "block";
  results.style.display = "block";
}

function hideLoader()
{
  panel.style.display = "none";
  loader.style.display = "none";
  const currentActive = document.querySelector('.tab.active');
  if (currentActive) {
    currentActive.classList.remove('active');
  }
}

function showElem(id)
{
  var elem = document.getElementById(id);
  elem.classList.toggle('active');
}



///function show_panel(){
//  panel.style.display = "block";
//  loader.style.display = "none";
// results.style.display = "none";
//}

// function hide_elem(id)
// {
//   var elem = document.getElementById(id);
//   elem.style.display = "none";
// }

// var slideSource = document.getElementById('about');
// document.getElementById('about_btn').onclick = function () {
//                     slideSource.classList.toggle('fade');
//                     slideSource.classList.toggle('show');
//   }

/*
function show_predictors()
{
  predictors.style.display = "block";
}

function show_instructions()
{
  instructions.style.display = "block";
}

function hide_about()
{
  about.style.display = "none";
}

function hide_instructions()
{
  instructions.style.display = 'none';
}

function hide_predictors()
{
  predictors.style.display = 'none'
}
*/