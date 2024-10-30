const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
    it('should return sum of rounded integers', () => {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should handle rounding first number', () => {
        assert.strictEqual(calculateNumber(1.4, 2), 3);
        assert.strictEqual(calculateNumber(1.6, 2), 4);
        assert.strictEqual(calculateNumber(2.499999, 2), 4);
    });

    it('should handle rounding second number', () => {
        assert.strictEqual(calculateNumber(2, 1.4), 3);
        assert.strictEqual(calculateNumber(2, 1.6), 4);
        assert.strictEqual(calculateNumber(2, 2.499999), 4);
    });

    it('should handle rounding both numbers', () => {
        assert.strictEqual(calculateNumber(1.4, 1.4), 2);
        assert.strictEqual(calculateNumber(1.6, 1.6), 4);
        assert.strictEqual(calculateNumber(2.499999, 2.499999), 4);
    });

    it('should handle negative numbers', () => {
        assert.strictEqual(calculateNumber(-1.4, -1.4), -2);
        assert.strictEqual(calculateNumber(-1.6, -1.6), -4);
        assert.strictEqual(calculateNumber(-2.499999, -2.499999), -4);
    });
});
