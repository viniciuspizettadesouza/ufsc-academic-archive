const express = require('express');
const SensorController = require('./controller/SensorController');

const router = express.Router();

router.post('/sensor', SensorController.store);

module.exports = router;