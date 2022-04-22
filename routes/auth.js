const express = require("express");
const router = express.Router();
// Auth Routes
// Controllers
const {
  login,
  register,
  forgotPassword,
  resetPassword,
} = require("../controllers/auth");

//http://localhost:5000/api/auth/register
router.route("/register").post(register);

//http://localhost:5000/api/auth/login
router.route("/login").post(login);

//http://localhost:5000/api/auth/forgotpassword
router.route("/forgotpassword").post(forgotPassword);

//http://localhost:5000/api/auth/resetpassword/:token
router.route("/passwordreset/:resetToken").put(resetPassword);

module.exports = router;