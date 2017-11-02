// This is the gulp file for automating front-end HTML/CSS development

//Include gulp
var gulp = require('gulp');

// Include Our Plugins
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');


// Compile Our Sass
gulp.task('sass', function () {
    return gulp.src('assets/scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('dashboard/static/css'));
});

// Concatenate & Minify JS
gulp.task('scripts', function() {
    return gulp.src('dashboard/static/js/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('dashboard/static/js'));
});

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('assets/js/*.js', ['lint', 'scripts']);
    gulp.watch(['assets/scss/*.scss', 'assets/scss/*/*.scss',
    'assets/scss/*/*/*.scss'], ['sass']);
});

// Default Task
gulp.task('default', ['sass', 'scripts', 'watch']);
