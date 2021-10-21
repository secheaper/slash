WALMART = {
    'site': 'walmart',
    'url': 'https://www.walmart.com/search?q=',
    'item_component': 'div',
    'item_indicator': {
        'data-item-id': True
    },
    'title_indicator': 'span.lh-title',
    'price_indicator': 'div.lh-copy',
    'link_indicator': 'a',
}

AMAZON = {
    'site': 'amazon',
    'url': 'https://www.amazon.com/s?k=',
    'item_component': 'div',
    'item_indicator': {
        'data-component-type': 's-search-result'
    },
    'title_indicator': 'h2 a span',
    'price_indicator': 'span.a-price span',
    'link_indicator': 'h2 a.a-link-normal',
}

# work in progress, not ready yet
TARGET = {
    'site': 'target',
    'url': 'https://www.target.com/s?searchTerm=',
    'item_component': 'div',
    'item_indicator': {
        'data-test': 'product-card-default'
    },
    'title_indicator': 'a[data-test~=product-title]',
    'price_indicator': 'span.a-price span',
    'link_indicator': 'h2 a.a-link-normal',
}

CONFIGS = [WALMART, AMAZON]
