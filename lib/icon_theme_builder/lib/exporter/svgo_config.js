module.exports = {
    plugins: [
        {
            name: 'preset-default',
            params: {
                overrides: {
                    removeEmptyContainers: false,
                    removeViewBox: false,
                    removeHiddenElems: false,
                    removeUselessStrokeAndFill: false,
                }
            }
        },
        // "convertStyleToAttrs",
        "removeStyleElement"
    ],
};
