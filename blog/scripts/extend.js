hexo.extend.filter.register('theme_inject', function(injects) {
  injects.bodyEnd.file('default', 'scripts/js/live2D.js');
});