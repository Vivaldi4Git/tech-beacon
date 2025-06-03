module.exports = {
    base: '/tech-beacon/',  // 更新为新的仓库名
    title: 'Tech Beacon',
    description: 'Exploring & Enlightening',
    head: [
        ['script', { src: 'https://unpkg.com/@excalidraw/excalidraw/dist/excalidraw.production.min.js' }],
        ['link', { rel: 'stylesheet', href: 'https://unpkg.com/@excalidraw/excalidraw/dist/excalidraw.min.css' }]
    ],
    markdown: {
        extendMarkdown: md => {
            // 配置 markdown-it 以支持自定义组件
            md.use(require('markdown-it-container'), 'excalidraw')
        }
    },
    themeConfig: {
        nav: [
            { text: '首页', link: '/' },
            { text: 'AI 学习', link: '/ai-learning/' },
        ],
        sidebar: {
            '/ai-learning/': [
                {
                    title: 'LLM 学习笔记',
                    collapsable: false,
                    children: [
                        '',                          // /ai-learning/README.md
                        '01-pretraining-data',       // 预训练数据
                        '02-tokenization',           // 分词技术
                        '03-neural-network-internals',           // 
                    ]
                }
            ]
        }
    }
}