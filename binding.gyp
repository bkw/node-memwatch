{
  'targets': [
    {
      'target_name': 'memwatch',
      'include_dirs': [
        '<!(node -p -e "require(\'path\').dirname(require.resolve(\'nan\'))")'
      ],
      'sources': [
        'src/heapdiff.cc',
        'src/init.cc',
        'src/memwatch.cc',
        'src/util.cc'
      ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CFLAGS' : ['-fpermissive']
          }
        }]
      ]
    }
  ]
}
