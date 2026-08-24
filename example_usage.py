from client import AgenticCommerceOptimizationProductCatalogReadyClient

def main():
    client = AgenticCommerceOptimizationProductCatalogReadyClient()
    res = client.optimize_catalog_for_ai_agents({'sku': 'SKU_SMART_ESPRESSO_MACHINE', 'name': 'Dual Boiler PID Brewer', 'price': 1450.0})
    print('SKU: ' + res['product_sku'] + ' | Agentic Readiness: ' + str(res['agentic_search_readiness_score']) + '/100')
    print('Token Savings: -' + str(res['llm_context_token_efficiency_pct']) + '% | Zero-Click Buy: ' + str(res['zero_click_buying_enabled']))
    print('Endpoint: ' + res['structured_attributes_schema']['instant_checkout_api_endpoint'])

if __name__ == '__main__':
    main()
