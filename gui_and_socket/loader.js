
var panel = document.getElementById('panel');
var loader = document.getElementById('loader_panel');
var results = document.getElementById('results_div');

function show_loader() 
{
  panel.style.display = "block";
  loader.style.display = "block";
  results.style.display = "block";
  create_scale(sequence);
}

function hide_loader()
{
  panel.style.display = "none";
  loader.style.display = "none";
}