<template>
<div id="search5back">

    <form method="get" action="/search" id="searchbox5">
        <input id="search52" name="q" type="text" size="40" onkeyup="myFunction()" placeholder="Search an Employee...." />
    </form>
</div>

<div class="tab-content">
  <div id="weeklylb" class="leadboardcontent">

    <div class="leaderboard" id="leaderboard">

      <ol id="myOL">
        <li>
          <mark>
            <?php while( $toprow4=s qlsrv_fetch_array( $stmt4) ) {
                      echo "<div class='parent-div'><span class='rank'>" . $toprow4[ 'rank'] .
                           "</span><span class='name'>" . $toprow4[ 'EmployeeName'] .
                           "</span><span class='points'>" . $toprow4[ 'pointsRewarded'] .
                           "</span></div>"; } ?>
          </mark>
        </li>
      </ol>
    </div>
</template>

<script>
function myFunction() {
    var input, filter, ol, li, a, i;
    input = document.getElementById("search52");
    filter = input.value.toUpperCase();
    ol = document.getElementById("myOL");
    li = ol.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByClassName("name")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
</script>
