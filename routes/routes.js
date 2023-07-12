const express = require('express')
const router = express.Router()
const LoginRouter = require('./LoginRoutes')
const MainRouter = require('./MainRoutes')
const PeliculaRouter = require('./PeliculaRoutes')
const PostRouter = require('./PostRoutes')


router.use('/login',LoginRouter)
router.use('/main',MainRouter)
router.use('/pelicula',PeliculaRouter)
router.use('/post',PostRouter)

module.exports = router
