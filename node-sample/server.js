const express = require("express");
const app = express();

app.use(express.static("public"));

app.get("/", (req, res) => {
    res.send("Hello, World!");
});

server.listen(8080, function(){
    console.log("Https listening on 8080");
});
