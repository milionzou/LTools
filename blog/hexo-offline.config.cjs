// offline config passed to workbox-build.
module.exports = {
  globPatterns: ['**/*.{js,html,css,png,jpg,gif,svg,webp,eot,ttf,woff,woff2}'],
  // �o�B�ļ��ϼ���������վ�cʹ�������� webp ��ʽ���ļ���Ո���ļ��������Mȥ��
  globDirectory: 'public',
  swDest: 'public/service-worker.js',
  maximumFileSizeToCacheInBytes: 10485760, // ���������ļ���С�����ֹ����λ��
  skipWaiting: true,
  clientsClaim: true,
  runtimeCaching: [ // �������Ҫ���d CDN �YԴ��Ո����ԓ�x헣�����]�У����Բ����á�
    // CDNs - should be CacheFirst, since they should be used specific versions so should not change
    {
      urlPattern: /^https:\/\/cdn\.example\.com\/.*/, // ����Q����� URL
      handler: 'CacheFirst'
    }
  ]
}
