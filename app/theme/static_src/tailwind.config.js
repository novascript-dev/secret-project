/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                'kaya-dark-gray': '#303030',
                'kaya-green-400': '#CDEA98',
                'kaya-green-500': '#A7C879',
                'kaya-dark-green': '#738252',
            },
            fontFamily: {
                marvin: ['MarvinVisions', 'sans-serif'],
                din: ['DIN2014', 'sans-serif'],
              },
            fontWeight: {
                light: '300',
                normal: '400',
                bold: '700',
                extrabold: '800',
                extralight: '200',
            },
            fontFace: {
                'marvin': {
                  src: 'url(/static/fonts/MarvinVisions-Variable.woff2) format("woff2")',
                  fontWeight: 'normal',
                  fontStyle: 'normal',
                },
                'din-regular': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Regular.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Regular.woff) format("woff")',
                fontWeight: 'normal',
                fontStyle: 'normal',
                },
                'din-bold': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Bold.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Bold.woff) format("woff")',
                fontWeight: 'bold',
                fontStyle: 'normal',
                },
                'din-italic': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Italic.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Italic.woff) format("woff")',
                fontWeight: 'normal',
                fontStyle: 'italic',
                },
                'din-bold-italic': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Bold-Italic.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Bold-Italic.woff) format("woff")',
                fontWeight: 'bold',
                fontStyle: 'italic',
                },
                'din-extra-bold': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Extra-Bold.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Extra-Bold.woff) format("woff")',
                fontWeight: '800',
                fontStyle: 'normal',
                },
                'din-extra-bold-italic': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Extra-Bold-Italic.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Extra-Bold-Italic.woff) format("woff")',
                fontWeight: '800',
                fontStyle: 'italic',
                },
                'din-light': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Light.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Light.woff) format("woff")',
                fontWeight: '300',
                fontStyle: 'normal',
                },
                'din-light-italic': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Light-Italic.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Light-Italic.woff) format("woff")',
                fontWeight: '300',
                fontStyle: 'italic',
                },
                'din-extra-light': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Extra-Light.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Extra-Light.woff) format("woff")',
                fontWeight: '200',
                fontStyle: 'normal',
                },
                'din-extra-light-italic': {
                src: 'url(/static/fonts/DIN-2014/DIN-2014_Extra-Light-Italic.woff2) format("woff2"), url(/static/fonts/DIN-2014/DIN-2014_Extra-Light-Italic.woff) format("woff")',
                fontWeight: '200',
                fontStyle: 'italic',
                },
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
