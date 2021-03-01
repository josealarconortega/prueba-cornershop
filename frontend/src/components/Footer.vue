<template>
  <footer class="footer">
    <b-container class="container">
      <b-row>
        <b-col cols="6" class="datos-pie">
          <div class="info-pie">
            <span>Prueba Cornershop</span>
            <p>
              José Felipe Alarcón<br />
              Mail: j.felipe.alarcon.ortega@gmail.com<br />
              Tel: +569 31201232
            </p>
          </div>
        </b-col>
        <b-col cols="6" class="nav_footer hidden-mobile">
          &nbsp;
        </b-col>
      </b-row>
    </b-container>
  </footer>
</template>
<style scoped>
.footer {
  border-top: 7px solid #5f9ed6;
  bottom: 0;
  width: 100%;
  font-size: 11px;
}
footer {
  background-color: #33393d;
  color: #7f7f7f;
  height: 120px;
  margin-top: -120px;
}
.content-inside {
  padding-bottom: 120px;
}

footer .logo-pie {
  float: left;
  margin-right: 10px;
}
img {
  vertical-align: middle;
}
footer .nav_footer {
  width: 48%;
  float: right;
}
.nav_footer {
  margin-top: 0px;
}
footer .info-pie {
  float: left;
  margin-top: 7px;
  text-align: left;
}
footer .datos-pie {
  margin-top: 20px;
}
</style>
