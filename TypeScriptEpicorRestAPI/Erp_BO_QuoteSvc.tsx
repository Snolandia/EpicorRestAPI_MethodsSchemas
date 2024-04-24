import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.QuoteSvc
// Description: Quote Business Object
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get Quotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Quotes
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedRow
   */  
export function get_Quotes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Quotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Quotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Quote item
   Description: Calls GetByID to retrieve the Quote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Quote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   */  
export function get_Quotes_Company_QuoteNum(Company:string, QuoteNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Quote for the service
   Description: Calls UpdateExt to update Quote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Quote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Quotes_Company_QuoteNum(Company:string, QuoteNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete Quote item
   Description: Call UpdateExt to delete Quote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Quote
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Quotes_Company_QuoteNum(Company:string, QuoteNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QSalesRPs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QSalesRPs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QSalesRPRow
   */  
export function get_Quotes_Company_QuoteNum_QSalesRPs(Company:string, QuoteNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QSalesRPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QSalesRPs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QSalesRPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QSalesRP item
   Description: Calls GetByID to retrieve the QSalesRP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QSalesRP1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param SalesRepCode Desc: SalesRepCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   */  
export function get_Quotes_Company_QuoteNum_QSalesRPs_Company_QuoteNum_SalesRepCode(Company:string, QuoteNum:string, SalesRepCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QSalesRPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QSalesRPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteCnts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCntRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteCnts(Company:string, QuoteNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteCnts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteCnt item
   Description: Calls GetByID to retrieve the QuoteCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCnt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param PerConID Desc: PerConID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company:string, QuoteNum:string, CustNum:string, ShipToNum:string, ConNum:string, PerConID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteComs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteComs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteComRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteComs(Company:string, QuoteNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteComRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteComs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteComRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteCom item
   Description: Calls GetByID to retrieve the QuoteCom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCom1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CompNum Desc: CompNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteComs_Company_QuoteNum_CompNum(Company:string, QuoteNum:string, CompNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteComRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteComRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteDtls(Company:string, QuoteNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtl item
   Description: Calls GetByID to retrieve the QuoteDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteDtls_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteHedMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteHedMscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedMscRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteHedMscs(Company:string, QuoteNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteHedMsc item
   Description: Calls GetByID to retrieve the QuoteHedMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedMsc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteHedMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteHedTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteHedTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedTaxRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteHedTaxes(Company:string, QuoteNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteHedTax item
   Description: Calls GetByID to retrieve the QuoteHedTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ClaimsTax Desc: ClaimsTax   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company:string, QuoteNum:string, TaxCode:string, RateCode:string, ClaimsTax:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteHedTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteHedAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedAttchRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteHedAttches(Company:string, QuoteNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteHedAttch item
   Description: Calls GetByID to retrieve the QuoteHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   */  
export function get_Quotes_Company_QuoteNum_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company:string, QuoteNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QSalesRPs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QSalesRPs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QSalesRPRow
   */  
export function get_QSalesRPs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QSalesRPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QSalesRPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QSalesRPs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QSalesRPs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QSalesRP item
   Description: Calls GetByID to retrieve the QSalesRP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QSalesRP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param SalesRepCode Desc: SalesRepCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   */  
export function get_QSalesRPs_Company_QuoteNum_SalesRepCode(Company:string, QuoteNum:string, SalesRepCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QSalesRPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QSalesRPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QSalesRP for the service
   Description: Calls UpdateExt to update QSalesRP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QSalesRP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param SalesRepCode Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QSalesRPs_Company_QuoteNum_SalesRepCode(Company:string, QuoteNum:string, SalesRepCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QSalesRP item
   Description: Call UpdateExt to delete QSalesRP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QSalesRP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param SalesRepCode Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QSalesRPs_Company_QuoteNum_SalesRepCode(Company:string, QuoteNum:string, SalesRepCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteCnts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCntRow
   */  
export function get_QuoteCnts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteCnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteCnts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteCnt item
   Description: Calls GetByID to retrieve the QuoteCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param PerConID Desc: PerConID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   */  
export function get_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company:string, QuoteNum:string, CustNum:string, ShipToNum:string, ConNum:string, PerConID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteCnt for the service
   Description: Calls UpdateExt to update QuoteCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param PerConID Desc: PerConID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company:string, QuoteNum:string, CustNum:string, ShipToNum:string, ConNum:string, PerConID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteCnt item
   Description: Call UpdateExt to delete QuoteCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param PerConID Desc: PerConID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company:string, QuoteNum:string, CustNum:string, ShipToNum:string, ConNum:string, PerConID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteComs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteComs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteComRow
   */  
export function get_QuoteComs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteComRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteComRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteComs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteComRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteComs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteCom item
   Description: Calls GetByID to retrieve the QuoteCom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCom
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CompNum Desc: CompNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   */  
export function get_QuoteComs_Company_QuoteNum_CompNum(Company:string, QuoteNum:string, CompNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteComRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteComRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteCom for the service
   Description: Calls UpdateExt to update QuoteCom. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteCom
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CompNum Desc: CompNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteComs_Company_QuoteNum_CompNum(Company:string, QuoteNum:string, CompNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteCom item
   Description: Call UpdateExt to delete QuoteCom item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteCom
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param CompNum Desc: CompNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteComs_Company_QuoteNum_CompNum(Company:string, QuoteNum:string, CompNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtls
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlRow
   */  
export function get_QuoteDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtl item
   Description: Calls GetByID to retrieve the QuoteDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteDtl for the service
   Description: Calls UpdateExt to update QuoteDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteDtls_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteDtl item
   Description: Call UpdateExt to delete QuoteDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteDtls_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteCoParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteCoParts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCoPartRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteCoParts(Company:string, QuoteNum:string, QuoteLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCoPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteCoParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCoPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteCoPart item
   Description: Calls GetByID to retrieve the QuoteCoPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCoPart1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company:string, QuoteNum:string, QuoteLine:string, CoPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteCoPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteCoPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtlAttrValueSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtlAttrValueSets1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttrValueSetRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttrValueSets(Company:string, QuoteNum:string, QuoteLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttrValueSets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtlAttrValueSet item
   Description: Calls GetByID to retrieve the QuoteDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttrValueSet1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company:string, QuoteNum:string, QuoteLine:string, AttributeValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtlTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtlTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlTaxRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlTaxes(Company:string, QuoteNum:string, QuoteLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtlTax item
   Description: Calls GetByID to retrieve the QuoteDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, QuoteNum:string, QuoteLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMscRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteMscs(Company:string, QuoteNum:string, QuoteLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMsc item
   Description: Calls GetByID to retrieve the QuoteMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMsc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteQties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteQties1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteQtyRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteQties(Company:string, QuoteNum:string, QuoteLine:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteQties", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteQty item
   Description: Calls GetByID to retrieve the QuoteQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteQty1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttchRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttches(Company:string, QuoteNum:string, QuoteLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtlAttch item
   Description: Calls GetByID to retrieve the QuoteDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   */  
export function get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteCoParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteCoParts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCoPartRow
   */  
export function get_QuoteCoParts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCoPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCoPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteCoParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteCoParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteCoPart item
   Description: Calls GetByID to retrieve the QuoteCoPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCoPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   */  
export function get_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company:string, QuoteNum:string, QuoteLine:string, CoPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteCoPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteCoPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteCoPart for the service
   Description: Calls UpdateExt to update QuoteCoPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteCoPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company:string, QuoteNum:string, QuoteLine:string, CoPartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteCoPart item
   Description: Call UpdateExt to delete QuoteCoPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteCoPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param CoPartNum Desc: CoPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company:string, QuoteNum:string, QuoteLine:string, CoPartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlAttrValueSets
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttrValueSetRow
   */  
export function get_QuoteDtlAttrValueSets(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlAttrValueSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlAttrValueSets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtlAttrValueSet item
   Description: Calls GetByID to retrieve the QuoteDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   */  
export function get_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company:string, QuoteNum:string, QuoteLine:string, AttributeValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteDtlAttrValueSet for the service
   Description: Calls UpdateExt to update QuoteDtlAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company:string, QuoteNum:string, QuoteLine:string, AttributeValueSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteDtlAttrValueSet item
   Description: Call UpdateExt to delete QuoteDtlAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company:string, QuoteNum:string, QuoteLine:string, AttributeValueSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlTaxRow
   */  
export function get_QuoteDtlTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtlTax item
   Description: Calls GetByID to retrieve the QuoteDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   */  
export function get_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, QuoteNum:string, QuoteLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteDtlTax for the service
   Description: Calls UpdateExt to update QuoteDtlTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, QuoteNum:string, QuoteLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteDtlTax item
   Description: Call UpdateExt to delete QuoteDtlTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, QuoteNum:string, QuoteLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMscs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMscRow
   */  
export function get_QuoteMscs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteMscs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteMsc item
   Description: Calls GetByID to retrieve the QuoteMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   */  
export function get_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteMsc for the service
   Description: Calls UpdateExt to update QuoteMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteMsc item
   Description: Call UpdateExt to delete QuoteMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteQties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteQties
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteQtyRow
   */  
export function get_QuoteQties(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteQties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteQties(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteQty item
   Description: Calls GetByID to retrieve the QuoteQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteQty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   */  
export function get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteQty for the service
   Description: Calls UpdateExt to update QuoteQty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteQty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteQty item
   Description: Call UpdateExt to delete QuoteQty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteQty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get Qtmmkups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Qtmmkups1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtmmkupRow
   */  
export function get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_Qtmmkups(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtmmkupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/Qtmmkups", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtmmkupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Qtmmkup item
   Description: Calls GetByID to retrieve the Qtmmkup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Qtmmkup1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   */  
export function get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, ClassCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QtmmkupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QtmmkupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QtQtyMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QtQtyMscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtQtyMscRow
   */  
export function get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_QtQtyMscs(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtQtyMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/QtQtyMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtQtyMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QtQtyMsc item
   Description: Calls GetByID to retrieve the QtQtyMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QtQtyMsc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   */  
export function get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QtQtyMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QtQtyMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get Qtmmkups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Qtmmkups
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtmmkupRow
   */  
export function get_Qtmmkups(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtmmkupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtmmkupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Qtmmkups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Qtmmkups(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Qtmmkup item
   Description: Calls GetByID to retrieve the Qtmmkup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Qtmmkup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   */  
export function get_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, ClassCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QtmmkupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QtmmkupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Qtmmkup for the service
   Description: Calls UpdateExt to update Qtmmkup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Qtmmkup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, ClassCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete Qtmmkup item
   Description: Call UpdateExt to delete Qtmmkup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Qtmmkup
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param ClassCode Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, ClassCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QtQtyMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QtQtyMscs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtQtyMscRow
   */  
export function get_QtQtyMscs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtQtyMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtQtyMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QtQtyMscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QtQtyMscs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QtQtyMsc item
   Description: Calls GetByID to retrieve the QtQtyMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QtQtyMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   */  
export function get_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QtQtyMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QtQtyMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QtQtyMsc for the service
   Description: Calls UpdateExt to update QtQtyMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QtQtyMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QtQtyMsc item
   Description: Call UpdateExt to delete QtQtyMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QtQtyMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttchRow
   */  
export function get_QuoteDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtlAttch item
   Description: Calls GetByID to retrieve the QuoteDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   */  
export function get_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteDtlAttch for the service
   Description: Calls UpdateExt to update QuoteDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteDtlAttch item
   Description: Call UpdateExt to delete QuoteDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company:string, QuoteNum:string, QuoteLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteHedMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteHedMscs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedMscRow
   */  
export function get_QuoteHedMscs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteHedMscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteHedMscs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteHedMsc item
   Description: Calls GetByID to retrieve the QuoteHedMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   */  
export function get_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteHedMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteHedMsc for the service
   Description: Calls UpdateExt to update QuoteHedMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteHedMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteHedMsc item
   Description: Call UpdateExt to delete QuoteHedMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteHedMsc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company:string, QuoteNum:string, QuoteLine:string, QtyNum:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteHedTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteHedTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedTaxRow
   */  
export function get_QuoteHedTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteHedTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteHedTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteHedTax item
   Description: Calls GetByID to retrieve the QuoteHedTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ClaimsTax Desc: ClaimsTax   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   */  
export function get_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company:string, QuoteNum:string, TaxCode:string, RateCode:string, ClaimsTax:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteHedTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteHedTax for the service
   Description: Calls UpdateExt to update QuoteHedTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteHedTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ClaimsTax Desc: ClaimsTax   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company:string, QuoteNum:string, TaxCode:string, RateCode:string, ClaimsTax:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteHedTax item
   Description: Call UpdateExt to delete QuoteHedTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteHedTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ClaimsTax Desc: ClaimsTax   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company:string, QuoteNum:string, TaxCode:string, RateCode:string, ClaimsTax:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteHedAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedAttchRow
   */  
export function get_QuoteHedAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteHedAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteHedAttch item
   Description: Calls GetByID to retrieve the QuoteHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   */  
export function get_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company:string, QuoteNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteHedAttch for the service
   Description: Calls UpdateExt to update QuoteHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company:string, QuoteNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete QuoteHedAttch item
   Description: Call UpdateExt to delete QuoteHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company:string, QuoteNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get HedTaxSums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HedTaxSums
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HedTaxSumRow
   */  
export function get_HedTaxSums(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HedTaxSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HedTaxSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HedTaxSums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HedTaxSums(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HedTaxSum item
   Description: Calls GetByID to retrieve the HedTaxSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HedTaxSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HedNum Desc: HedNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param AllocDepInvcNum Desc: AllocDepInvcNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
   */  
export function get_HedTaxSums_Company_HedNum_TaxCode_RateCode_AllocDepInvcNum(Company:string, HedNum:string, TaxCode:string, RateCode:string, AllocDepInvcNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HedTaxSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums(" + Company + "," + HedNum + "," + TaxCode + "," + RateCode + "," + AllocDepInvcNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_HedTaxSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HedTaxSum for the service
   Description: Calls UpdateExt to update HedTaxSum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HedTaxSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HedNum Desc: HedNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param AllocDepInvcNum Desc: AllocDepInvcNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HedTaxSums_Company_HedNum_TaxCode_RateCode_AllocDepInvcNum(Company:string, HedNum:string, TaxCode:string, RateCode:string, AllocDepInvcNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums(" + Company + "," + HedNum + "," + TaxCode + "," + RateCode + "," + AllocDepInvcNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete HedTaxSum item
   Description: Call UpdateExt to delete HedTaxSum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HedTaxSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HedNum Desc: HedNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param AllocDepInvcNum Desc: AllocDepInvcNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HedTaxSums_Company_HedNum_TaxCode_RateCode_AllocDepInvcNum(Company:string, HedNum:string, TaxCode:string, RateCode:string, AllocDepInvcNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums(" + Company + "," + HedNum + "," + TaxCode + "," + RateCode + "," + AllocDepInvcNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PartSubs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartSubs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSubsRow
   */  
export function get_PartSubs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSubsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSubsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartSubs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartSub item
   Description: Calls GetByID to retrieve the PartSub item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSub
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SubPart Desc: SubPart   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   */  
export function get_PartSubs_Company_PartNum_SubPart(Company:string, PartNum:string, SubPart:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartSubsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs(" + Company + "," + PartNum + "," + SubPart + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartSubsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartSub for the service
   Description: Calls UpdateExt to update PartSub. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSub
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SubPart Desc: SubPart   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartSubs_Company_PartNum_SubPart(Company:string, PartNum:string, SubPart:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs(" + Company + "," + PartNum + "," + SubPart + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete PartSub item
   Description: Call UpdateExt to delete PartSub item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSub
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SubPart Desc: SubPart   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartSubs_Company_PartNum_SubPart(Company:string, PartNum:string, SubPart:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs(" + Company + "," + PartNum + "," + SubPart + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TaxConnectStatus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxConnectStatus
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxConnectStatusRow
   */  
export function get_TaxConnectStatus(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxConnectStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxConnectStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxConnectStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxConnectStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxConnectStatu item
   Description: Calls GetByID to retrieve the TaxConnectStatu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxConnectStatu
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
   */  
export function get_TaxConnectStatus_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxConnectStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus(" + Company + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxConnectStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxConnectStatu for the service
   Description: Calls UpdateExt to update TaxConnectStatu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxConnectStatu
      @param Company Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxConnectStatus_Company(Company:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus(" + Company + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete TaxConnectStatu item
   Description: Call UpdateExt to delete TaxConnectStatu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxConnectStatu
      @param Company Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxConnectStatus_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus(" + Company + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get WhatIfSchedulings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhatIfSchedulings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhatIfSchedulingRow
   */  
export function get_WhatIfSchedulings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhatIfSchedulingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhatIfSchedulingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhatIfSchedulings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhatIfSchedulings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WhatIfScheduling item
   Description: Calls GetByID to retrieve the WhatIfScheduling item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhatIfScheduling
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
   */  
export function get_WhatIfSchedulings_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WhatIfSchedulingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WhatIfSchedulingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WhatIfScheduling for the service
   Description: Calls UpdateExt to update WhatIfScheduling. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhatIfScheduling
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WhatIfSchedulings_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings(" + SysRowID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete WhatIfScheduling item
   Description: Call UpdateExt to delete WhatIfScheduling item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhatIfScheduling
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WhatIfSchedulings_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings(" + SysRowID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseQuoteHed:string, whereClauseQuoteHedAttch:string, whereClauseQSalesRP:string, whereClauseQuoteCnt:string, whereClauseQuoteCom:string, whereClauseQuoteDtl:string, whereClauseQuoteDtlAttch:string, whereClauseQuoteCoPart:string, whereClauseQuoteDtlAttrValueSet:string, whereClauseQuoteDtlTax:string, whereClauseQuoteMsc:string, whereClauseQuoteQty:string, whereClauseQtmmkup:string, whereClauseQtQtyMsc:string, whereClauseQuoteHedMsc:string, whereClauseQuoteHedTax:string, whereClauseHedTaxSum:string, whereClausePartSubs:string, whereClauseTaxConnectStatus:string, whereClauseWhatIfScheduling:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseQuoteHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteHed=" + whereClauseQuoteHed
   }
   if(typeof whereClauseQuoteHedAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteHedAttch=" + whereClauseQuoteHedAttch
   }
   if(typeof whereClauseQSalesRP!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQSalesRP=" + whereClauseQSalesRP
   }
   if(typeof whereClauseQuoteCnt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteCnt=" + whereClauseQuoteCnt
   }
   if(typeof whereClauseQuoteCom!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteCom=" + whereClauseQuoteCom
   }
   if(typeof whereClauseQuoteDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteDtl=" + whereClauseQuoteDtl
   }
   if(typeof whereClauseQuoteDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteDtlAttch=" + whereClauseQuoteDtlAttch
   }
   if(typeof whereClauseQuoteCoPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteCoPart=" + whereClauseQuoteCoPart
   }
   if(typeof whereClauseQuoteDtlAttrValueSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteDtlAttrValueSet=" + whereClauseQuoteDtlAttrValueSet
   }
   if(typeof whereClauseQuoteDtlTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteDtlTax=" + whereClauseQuoteDtlTax
   }
   if(typeof whereClauseQuoteMsc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteMsc=" + whereClauseQuoteMsc
   }
   if(typeof whereClauseQuoteQty!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteQty=" + whereClauseQuoteQty
   }
   if(typeof whereClauseQtmmkup!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQtmmkup=" + whereClauseQtmmkup
   }
   if(typeof whereClauseQtQtyMsc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQtQtyMsc=" + whereClauseQtQtyMsc
   }
   if(typeof whereClauseQuoteHedMsc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteHedMsc=" + whereClauseQuoteHedMsc
   }
   if(typeof whereClauseQuoteHedTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteHedTax=" + whereClauseQuoteHedTax
   }
   if(typeof whereClauseHedTaxSum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHedTaxSum=" + whereClauseHedTaxSum
   }
   if(typeof whereClausePartSubs!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartSubs=" + whereClausePartSubs
   }
   if(typeof whereClauseTaxConnectStatus!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxConnectStatus=" + whereClauseTaxConnectStatus
   }
   if(typeof whereClauseWhatIfScheduling!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWhatIfScheduling=" + whereClauseWhatIfScheduling
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(quoteNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof quoteNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quoteNum=" + quoteNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofBTCustID
   Description: This method returns the Bill To customer info.
   OperationID: OnChangeofBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofBTCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeofBTCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofEngineered
   Description: This method Check the number of reference designators are equal to
the Required Ref Designators defined on JobMtl
   OperationID: OnChangeofEngineered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofEngineered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofEngineered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofEngineered(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeofEngineered", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeIncotermCode
   Description: This method checks incoterm
   OperationID: OnChangeIncotermCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIncotermCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIncotermCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIncotermCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeIncotermCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofLineExemptTax
   Description: This method should be called when the user populates line Tax Exempt field previously being blank
record is changed.
   OperationID: OnChangeofLineExemptTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofLineExemptTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofLineExemptTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofLineExemptTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeofLineExemptTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OpenCloseQuote
   Description: This method either opens or closes a Quote and returns the updated object
   OperationID: OpenCloseQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenCloseQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCloseQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenCloseQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OpenCloseQuote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreOpenCloseQuote
   Description: This method is to be run befor the OpenCloseQuote method so that any questions
that need to be asked before the OpenCloseQuote method can run can be asked
   OperationID: PreOpenCloseQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreOpenCloseQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreOpenCloseQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreOpenCloseQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PreOpenCloseQuote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreRefreshQty
   Description: PreRefreshQty
   OperationID: PreRefreshQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreRefreshQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreRefreshQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreRefreshQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PreRefreshQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreSOCreate
   Description: Executes validations before Sales Oreder is created:
Process all lines if Job Type is PRJ and Invoicing method is CS or MB then ask user
   OperationID: PreSOCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSOCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSOCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreSOCreate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PreSOCreate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsCreditMemo
   Description: Check if a credit memo exists for a credit line
Used to validate if changing return type is allowed
   OperationID: ExistsCreditMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsCreditMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsCreditMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsCreditMemo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExistsCreditMemo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetReadyToCalc
   Description: Logic to calculate taxes.
Notes: Taxes are not recalculated if "Ready to Process" flag is turned off.
   OperationID: SetReadyToCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetReadyToCalc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/SetReadyToCalc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuotePartNumHasSubstitutes
   Description: This method detrmines if a partNum has any Substitutes defined.
   OperationID: QuotePartNumHasSubstitutes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuotePartNumHasSubstitutes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuotePartNumHasSubstitutes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuotePartNumHasSubstitutes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuotePartNumHasSubstitutes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalcKitPriceAfterConfig
   Description: When configuring a part, the QuoteDtl unit price may change during the configuration
process.  This method is to be called after running product configurator to recalculate
the kit pricing.
   OperationID: RecalcKitPriceAfterConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcKitPriceAfterConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcKitPriceAfterConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcKitPriceAfterConfig(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/RecalcKitPriceAfterConfig", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalcKitPricing
   Description: RecalcKitPricing
   OperationID: RecalcKitPricing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcKitPricing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcKitPricing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcKitPricing(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/RecalcKitPricing", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalcWorksheet
   Description: Each part class can have its own material markup percentage
This method calculates the Material Markup from the Qtmmkup table
   OperationID: RecalcWorksheet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcWorksheet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcWorksheet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcWorksheet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/RecalcWorksheet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveKitComponents
   Description: To delete the QuoteDtl records created as components for a Parent Sales Kit.
   OperationID: RemoveKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveKitComponents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/RemoveKitComponents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetOrderDefaults
   Description: This method updates Order Defaults.
   OperationID: SetOrderDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetOrderDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetOrderDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetOrderDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/SetOrderDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateCosts
   Description: Updates Worksheet fields.
   OperationID: UpdateCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCosts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/UpdateCosts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls
   Description: This method updates the DiscountPercent, NeedByDate,TaxRegionCode and RequestDate for existing Quote Detail Lines in a Quote
   OperationID: ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateProfits
   OperationID: ValidateProfits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateProfits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateProfits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateProfits(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateProfits", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateOTS
   OperationID: ValidateOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOTS(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateOTS", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateTaskSet
   Description: Validates the task Set Id.
   OperationID: ValidateTaskSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTaskSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateTaskSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValReqRefDes
   Description: Public method to call ValidateReqRefDes method and check the number of
reference designators are equal to the Required Ref Designators defined on QuoteMtl.
   OperationID: ValReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValReqRefDes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValReqRefDes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method WhatIfGetDate
   OperationID: WhatIfGetDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/WhatIfGetDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhatIfGetDate(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfGetDate", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method WhatIfScheduling
   OperationID: WhatIfScheduling
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WhatIfScheduling_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WhatIfScheduling_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhatIfScheduling(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfScheduling", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcConvUOMUnitPrice
   Description: CalcConvUOMUnitPrice
   OperationID: CalcConvUOMUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcConvUOMUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcConvUOMUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcConvUOMUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CalcConvUOMUnitPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FileType
   Description: FileType
   OperationID: FileType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FileType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/FileType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindPart
   Description: FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/FindPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPartFromRowID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfCurrentSiteHasExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIfCurrentSiteHasExternalMES(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetIfCurrentSiteHasExternalMES", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIfRevIsExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfRevIsExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIfRevIsExternalMES_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfRevIsExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIfRevIsExternalMES(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetIfRevIsExternalMES", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RequestEngineeringExternalMESValidation
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: RequestEngineeringExternalMESValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RequestEngineeringExternalMESValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestEngineeringExternalMESValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RequestEngineeringExternalMESValidation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/RequestEngineeringExternalMESValidation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckIfConfigured
   Description: CheckIfConfigured
   OperationID: CheckIfConfigured
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfConfigured_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfConfigured_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfConfigured(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckIfConfigured", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckQuoteDtlContractID
   Description: Validate ContractID is active and approved.
   OperationID: CheckQuoteDtlContractID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteDtlContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteDtlContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckQuoteDtlContractID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckQuoteDtlContractID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPlantConfCtrlUse3rdPartySched
   Description: Get the Use3rdPartySched field from PlantConfCtrl table.
   OperationID: GetPlantConfCtrlUse3rdPartySched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantConfCtrlUse3rdPartySched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPlantConfCtrlUse3rdPartySched(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPlantConfCtrlUse3rdPartySched", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPlantConfCtrlValues
   Description: Get the Use3rdPartySched and Rate Shopping values from PlantConfCtrl table.
   OperationID: GetPlantConfCtrlValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPlantConfCtrlValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantConfCtrlValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPlantConfCtrlValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPlantConfCtrlValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxCode
   OperationID: OnChangeTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeTaxCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRateCode
   OperationID: OnChangeRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRateCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeRateCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfTaxAmt
   Description: This method should be called when the tax amount on the quote tax
record is changed.
   OperationID: OnChangeOfTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfTaxAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeOfTaxAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfReportableAmt
   Description: This method should be called when the tax amount on the quote tax
record is changed.
   OperationID: OnChangeOfReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfReportableAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeOfReportableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxableAmt
   Description: This method should be called when the taxable amount on the invoice tax
record is changed.
   OperationID: OnChangeTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxableAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeTaxableAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfFixedAmount
   Description: This method should be called when the Fixed amount on the invoice tax
record is changed.
   OperationID: OnChangeOfFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfFixedAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeOfFixedAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfTaxPercent
   Description: This method should be called when the percentage amount on the quote tax
record is changed.
   OperationID: OnChangeOfTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfTaxPercent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeOfTaxPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateShippingDate
   Description: Validate the date is a working day as set in the Shipping Calendar.
   OperationID: ValidateShippingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShippingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShippingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShippingDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateShippingDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxRegInPrice
   Description: Retrieve Tax Region and InPrice value from the proposed Ship To and indicated if Quote has created any Tax Record.
   OperationID: GetTaxRegInPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxRegInPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxRegInPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxRegInPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetTaxRegInPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUpdtDtlTaxRgn
   Description: Defines if the system supposed to ask the user about Tax Liability change.
   OperationID: GetUpdtDtlTaxRgn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUpdtDtlTaxRgn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUpdtDtlTaxRgn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUpdtDtlTaxRgn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetUpdtDtlTaxRgn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateECCType
   Description: Validates if customer exists, a dealer licence is active and returns a warning message if current customer has a valid ECC type and the proposed one is invalid
   OperationID: ValidateECCType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateECCType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateECCType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateECCType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateECCType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearQuoteDtlDealerData
   Description: Clears dealer information for all quote lines
   OperationID: ClearQuoteDtlDealerData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearQuoteDtlDealerData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearQuoteDtlDealerData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearQuoteDtlDealerData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ClearQuoteDtlDealerData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteHedSalesRepCodeChanging
   Description: Updates sales rep information when the quote primary salesperson changes
   OperationID: QuoteHedSalesRepCodeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteHedSalesRepCodeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteHedSalesRepCodeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteHedSalesRepCodeChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedSalesRepCodeChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteHedCustomerCustIDAfterChange
   Description: Update customer information after QuoteHed Customer ID has changed
   OperationID: QuoteHedCustomerCustIDAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteHedCustomerCustIDAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteHedCustomerCustIDAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteHedCustomerCustIDAfterChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedCustomerCustIDAfterChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlReadyToQuoteChanging
   Description: Called when Quote Detail Ready To Quote is changing
   OperationID: QuoteDtlReadyToQuoteChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlReadyToQuoteChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlReadyToQuoteChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlReadyToQuoteChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlReadyToQuoteChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateQuoteDtlUnitPrice
   Description: This method will recalculate the Unit Price.  This should be called after the expected unit price (doc or base)
or expected price per code changes.
   OperationID: CalculateQuoteDtlUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateQuoteDtlUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateQuoteDtlUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateQuoteDtlUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CalculateQuoteDtlUnitPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlRefreshPriceListAndQuantities
   Description: Rrefreshes price list and quantities for a quote line.
Called when PriceListCode, BreakListCode, ProdCode, or OverridePriceList are changed.
   OperationID: QuoteDtlRefreshPriceListAndQuantities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlRefreshPriceListAndQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlRefreshPriceListAndQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlRefreshPriceListAndQuantities(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlRefreshPriceListAndQuantities", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMiscellanousChargeType
   Description: Called when a miscellaneous charge type changed.  Sets default values based on the type.
   OperationID: ChangeMiscellanousChargeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscellanousChargeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscellanousChargeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscellanousChargeType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeMiscellanousChargeType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteQtyMaterialMarkupChanged
   Description: Performs recalculations when the material markup value is changed.  Markup type indicates if the (M)aterial or (P)rofit markup value is what changed.
   OperationID: QuoteQtyMaterialMarkupChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteQtyMaterialMarkupChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteQtyMaterialMarkupChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteQtyMaterialMarkupChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQtyMaterialMarkupChanged", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteQtyPercentTypeChanged
   Description: Performs recalculations when quote quantity percent type changed.
   OperationID: QuoteQtyPercentTypeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteQtyPercentTypeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteQtyPercentTypeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteQtyPercentTypeChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQtyPercentTypeChanged", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteQtyValidateAndRecalcWorksheet
   Description: Validates and performs a worksheet recalculation when a field affecting worksheet values is changed.
   OperationID: QuoteQtyValidateAndRecalcWorksheet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteQtyValidateAndRecalcWorksheet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteQtyValidateAndRecalcWorksheet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteQtyValidateAndRecalcWorksheet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQtyValidateAndRecalcWorksheet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxBaseTaxAmtChange
   Description: This method should be called when the base tax amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseTaxAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseTaxAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseTaxAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxBaseTaxAmtChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxBaseTaxAmtChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxDocTaxAmtChange
   Description: This method should be called when the doc tax amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocTaxAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocTaxAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocTaxAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxDocTaxAmtChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxDocTaxAmtChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxBaseTaxableAmtChange
   Description: This method should be called when the base taxable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseTaxableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseTaxableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseTaxableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxBaseTaxableAmtChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxBaseTaxableAmtChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxDocTaxableAmtChange
   Description: This method should be called when the doc taxable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocTaxableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocTaxableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocTaxableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxDocTaxableAmtChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxDocTaxableAmtChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxBaseReportableAmtChange
   Description: This method should be called when the base reportable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseReportableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseReportableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseReportableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxBaseReportableAmtChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxBaseReportableAmtChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxDocReportableAmtChange
   Description: This method should be called when the doc reportable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocReportableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocReportableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocReportableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxDocReportableAmtChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxDocReportableAmtChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxBaseFixedAmountChange
   Description: This method should be called when the base fixed amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseFixedAmountChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseFixedAmountChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseFixedAmountChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxBaseFixedAmountChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxBaseFixedAmountChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlTaxDocFixedAmountChange
   Description: This method should be called when the doc fixed amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocFixedAmountChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocFixedAmountChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocFixedAmountChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlTaxDocFixedAmountChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxDocFixedAmountChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlRevisionNumAfterChange
   Description: Additional updates to QuoteDtl after the revision has changed
   OperationID: QuoteDtlRevisionNumAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlRevisionNumAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlRevisionNumAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlRevisionNumAfterChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlRevisionNumAfterChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlPartNumAfterChange
   Description: Processing after the QuoteDtl XPartNum value has changed
   OperationID: QuoteDtlPartNumAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlPartNumAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlPartNumAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlPartNumAfterChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlPartNumAfterChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteDtlXPartNumAfterChange
   Description: Processing after the QuoteDtl XPartNum value has changed
   OperationID: QuoteDtlXPartNumAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlXPartNumAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlXPartNumAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlXPartNumAfterChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlXPartNumAfterChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QSalesRPPrimeRepChanging
   Description: Called when the primary sales rep flag on a quote salesperson record is changing.
   OperationID: QSalesRPPrimeRepChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QSalesRPPrimeRepChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QSalesRPPrimeRepChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QSalesRPPrimeRepChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPPrimeRepChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSOCreate
   Description: Validation prior to creating a sales order from a quote.
   OperationID: ValidateSOCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSOCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSOCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSOCreate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateSOCreate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalculateLineDiscounts
   Description: Recalculate quote line discounts
   OperationID: RecalculateLineDiscounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalculateLineDiscounts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalculateLineDiscounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalculateLineDiscounts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/RecalculateLineDiscounts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateOrderFromQuote
   Description: Create an order from a quote.  This method will handle kit components internally rather than expecting them to be passed in as part of the dataset.
   OperationID: CreateOrderFromQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrderFromQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderFromQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateOrderFromQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CreateOrderFromQuote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateOrderFromQuoteSaveOTS
   Description: Create an order from a quote and save OTS information.  This method will handle kit components internally rather than expecting them to be passed in as part of the dataset.
   OperationID: CreateOrderFromQuoteSaveOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrderFromQuoteSaveOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderFromQuoteSaveOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateOrderFromQuoteSaveOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CreateOrderFromQuoteSaveOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckQuoteHedChangesBeforeUpdate
   Description: Checks for specific changes in QuoteHed and returns a prompt asking if these changes should be propagated to the quote lines
   OperationID: CheckQuoteHedChangesBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteHedChangesBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteHedChangesBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckQuoteHedChangesBeforeUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckQuoteHedChangesBeforeUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PropagateQuoteHedChangesToQuoteDtl
   Description: Propagates changes to QuoteHed to QuoteDtl from the field list passed in.
   OperationID: PropagateQuoteHedChangesToQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PropagateQuoteHedChangesToQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PropagateQuoteHedChangesToQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PropagateQuoteHedChangesToQuoteDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PropagateQuoteHedChangesToQuoteDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSalesKitComponents
   Description: Gets kit components for a quote line.
   OperationID: GetSalesKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSalesKitComponents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetSalesKitComponents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteCntShipToConNumChanged
   Description: Validates and returns contact information when the contact ShipToNum or ConNum values are changing
   OperationID: QuoteCntShipToConNumChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteCntShipToConNumChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteCntShipToConNumChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteCntShipToConNumChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCntShipToConNumChanged", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteCntShipToConNumChangedInactive
   Description: Validates and returns contact information when the contact ShipToNum or ConNum values are changing
   OperationID: QuoteCntShipToConNumChangedInactive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteCntShipToConNumChangedInactive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteCntShipToConNumChangedInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteCntShipToConNumChangedInactive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCntShipToConNumChangedInactive", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPerConInformation
   Description: Call when Quote Contact PerConID is changing.
returnResult:
When 1: Prompt user asking if the person/contact should be added to customer contacts
When 4: Prompt user asking if a new person/contact record should be created
All other values are handled by this api
   OperationID: GetPerConInformation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConInformation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConInformation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConInformation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPerConInformation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOTSTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateOTSTaxID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteHed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteHedAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteHedAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQSalesRP
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQSalesRP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQSalesRP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQSalesRP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQSalesRP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQSalesRP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteCnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteCnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteCom
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteCom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteCom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteCom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteCom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteCom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteDtlAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteCoPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteCoPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteCoPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteCoPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteCoPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteCoPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteDtlAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtlAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtlAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtlAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteDtlAttrValueSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteDtlAttrValueSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteDtlTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtlTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtlTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtlTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteDtlTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteDtlTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteMsc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteMsc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteQty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQtmmkup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQtmmkup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQtmmkup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQtmmkup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQtmmkup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQtmmkup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQtQtyMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQtQtyMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQtQtyMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQtQtyMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQtQtyMsc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQtQtyMsc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteHedMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHedMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHedMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHedMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteHedMsc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteHedMsc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuoteHedTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHedTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHedTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHedTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteHedTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewQuoteHedTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LaunchGlobalAlerts
   Description: Method called at service invocation to process Quote logic related to information monitored by Global Alerts - Due Dates and/or Follow Up Dates.
   OperationID: LaunchGlobalAlerts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaunchGlobalAlerts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaunchGlobalAlerts(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/LaunchGlobalAlerts", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MinimumDate
   Description: MinimumDate
   OperationID: MinimumDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MinimumDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MinimumDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MinimumDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/MinimumDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Calc_QuoteDtlDiscount
   Description: Calc_QuoteDtlDiscount
   OperationID: Calc_QuoteDtlDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Calc_QuoteDtlDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Calc_QuoteDtlDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Calc_QuoteDtlDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Calc_QuoteDtlDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AllowUndoReadyToQuote
   Description: This method exists soley for the purpose of allowing security for
unchecking the Ready To Quote flag to be defined
   OperationID: AllowUndoReadyToQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowUndoReadyToQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowUndoReadyToQuote(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/AllowUndoReadyToQuote", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApplyOrderBasedDiscount
   Description: This method applys the OrderBased Discount logic
   OperationID: ApplyOrderBasedDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplyOrderBasedDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyOrderBasedDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyOrderBasedDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ApplyOrderBasedDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetDiscountAmountOverride
   OperationID: SetDiscountAmountOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDiscountAmountOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDiscountAmountOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetDiscountAmountOverride(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/SetDiscountAmountOverride", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateQuantityUOMQuoteDtlAttribute
   OperationID: ValidateQuantityUOMQuoteDtlAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQuantityUOMQuoteDtlAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQuantityUOMQuoteDtlAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateQuantityUOMQuoteDtlAttribute(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ValidateQuantityUOMQuoteDtlAttribute", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignQuoteDtlAttributeDispValues
   OperationID: AssignQuoteDtlAttributeDispValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignQuoteDtlAttributeDispValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignQuoteDtlAttributeDispValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignQuoteDtlAttributeDispValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/AssignQuoteDtlAttributeDispValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignAttrSellingExpectedUM
   Description: Assign QuoteDtlAttrValueSet SellingExpectedUM
   OperationID: AssignAttrSellingExpectedUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignAttrSellingExpectedUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignAttrSellingExpectedUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignAttrSellingExpectedUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/AssignAttrSellingExpectedUM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAttrQuantityToOrder
   Description: Call this method when the value QuoteDtlAttrValueSet QuantityToOrder changes.
   OperationID: OnChangeAttrQuantityToOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttrQuantityToOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttrQuantityToOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttrQuantityToOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeAttrQuantityToOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeNumberOfPieces
   Description: Call this method when the Number Of Pieces changes to calculate a new quantity to order
   OperationID: OnChangeNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeNumberOfPieces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsPartPriceList
   OperationID: ExistsPartPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsPartPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsPartPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsPartPriceList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExistsPartPriceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsProductGroupPriceList
   OperationID: ExistsProductGroupPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsProductGroupPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsProductGroupPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsProductGroupPriceList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExistsProductGroupPriceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsProductGroupDiscPriceList
   OperationID: ExistsProductGroupDiscPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsProductGroupDiscPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsProductGroupDiscPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsProductGroupDiscPriceList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExistsProductGroupDiscPriceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsPartDiscPriceList
   OperationID: ExistsPartDiscPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsPartDiscPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsPartDiscPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsPartDiscPriceList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExistsPartDiscPriceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalcMaterialMarkup
   Description: Each part class can have its own material markup percentage
This method calculates the Material Markup from the Qtmmkup table
   OperationID: CalcMaterialMarkup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcMaterialMarkup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcMaterialMarkup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcMaterialMarkup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CalcMaterialMarkup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDiscBreakListCode
   Description: Change the DiscBreakListCode
   OperationID: ChangeDiscBreakListCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDiscBreakListCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDiscBreakListCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDiscBreakListCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeDiscBreakListCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMFCustID
   Description: Method to call when changing the Mark For Customer ID on the QuoteDtl record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeMFCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMFCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeMFCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMFShipToNum
   Description: Update QuoteDtl information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeMFShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMFShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMFShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMFShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeMFShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUseOTMF
   Description: Method to call when changing the UseOTMF field the QuoteDtl record.
Refreshes the address list and contact info
   OperationID: ChangeUseOTMF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUseOTMF(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeUseOTMF", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDocOrderUnitPrice
   Description: Perform the required updates when DocOrderUnitPrice changes.
   OperationID: ChangeDocOrderUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDocOrderUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDocOrderUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDocOrderUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeDocOrderUnitPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDtlReturnLineType
   Description: Method to call when changing the ReturnLineType on the QuoteDtl record.
Clears Warranty column if ReturnLineType is being changed to 'S'.
   OperationID: ChangeDtlReturnLineType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlReturnLineType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlReturnLineType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlReturnLineType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeDtlReturnLineType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDtlContractNum
   Description: Method to call when changing the ContractNum field in the Quote Line record.
Updates the QuoteDtl with values based on the new ContractNum.
   OperationID: ChangeDtlContractNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlContractNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeDtlContractNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDtlRenewalNbr
   Description: Method to call when changing the RenewalNbr field in the Quote Line record.
Updates the QuoteDtl with values based on the new RenewalNbr.
   OperationID: ChangeDtlRenewalNbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlRenewalNbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlRenewalNbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlRenewalNbr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeDtlRenewalNbr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeKitPricing
   Description: Recalculates the parent line's unit price when the kit pricing is set to "P", if the kit pricing is set to "C"
the price will be calculated on the AfterUpdate procedure.
   OperationID: ChangeKitPricing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeKitPricing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeKitPricing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeKitPricing(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeKitPricing", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeKitQtyPer
   Description: Used to recalculate the OrderQty of the component kit line using the parent's OrderQuantity
   OperationID: ChangeKitQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeKitQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeKitQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeKitQtyPer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeKitQtyPer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeManualTaxCalc
   OperationID: ChangeManualTaxCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeManualTaxCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeManualTaxCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeManualTaxCalc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeManualTaxCalc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMiscPercent
   Description: This method recalculates Misc Charges Amounts when Percentage was changed.
   OperationID: ChangeMiscPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscPercent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeMiscPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMiscAmt
   Description: This method recalculates Misc Charges Amounts when Amount was changed.
   OperationID: ChangeMiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeMiscAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMSRP
   Description: This method recalculates MSRP when MSRP was changed.
   OperationID: ChangeMSRP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMSRP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMSRP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMSRP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeMSRP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePromotionalPrice
   Description: This method recalculates PromotionalPrice when PromotionalPrice was changed.
   OperationID: ChangePromotionalPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePromotionalPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePromotionalPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePromotionalPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangePromotionalPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderQty
   Description: Gets the proposed OrderQty and if the current OrderDtl record is a sales kit then it recalculates
the order qty of each component based on the proposed OrderQty amount
   OperationID: ChangeOrderQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeOrderQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOverrideDiscPriceList
   Description: Rerun the price break calculation if the override price list flag is changed from
true to false.
   OperationID: ChangeOverrideDiscPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOverrideDiscPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOverrideDiscPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOverrideDiscPriceList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeOverrideDiscPriceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConfigurationChangePart
   Description: Update Quote Detail, Want to load PriceList Qty breaks and set new unit proce on those,
information when the Part Number is changed by Configuration Part Creation.
   OperationID: ConfigurationChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationChangePart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ConfigurationChangePart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConfigurationRefreshQty
   Description: Update PriceList Qty breaks and set new unit price on those
when the Part Number is changed by Document Rule.
   OperationID: ConfigurationRefreshQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationRefreshQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationRefreshQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationRefreshQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ConfigurationRefreshQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConfigurationChangeUnitPrice
   Description: Update Price fields when the UnitPrice or DocUnitPRice is changed by a Document Rule.
   OperationID: ConfigurationChangeUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangeUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangeUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationChangeUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ConfigurationChangeUnitPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateKBMaxConfigurator
   Description: Update the CPQ Configurator on the given Quote Line.
   OperationID: UpdateKBMaxConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateKBMaxConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateKBMaxConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateKBMaxConfigurator(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/UpdateKBMaxConfigurator", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetKBMaxConfigProdID
   Description: Set the CPQ Quote Product ID on the Quote Line.
This will trigger the loading of the method from CPQ onto the Quote Assembly.
   OperationID: SetKBMaxConfigProdID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetKBMaxConfigProdID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetKBMaxConfigProdID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetKBMaxConfigProdID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/SetKBMaxConfigProdID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PopulateCallContext
   Description: Allows for assigning of a generic CallContext for integrations.
   OperationID: PopulateCallContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateCallContext_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateCallContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PopulateCallContext(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PopulateCallContext", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartRev
   Description: Update Quote Detail information when the Part Revision is changed.
   OperationID: ChangePartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartRev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangePartRev", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartNum
   Description: Update Quote Detail information when the Part Number is changed.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartNumMaster
   Description: Perform all validations associated with the Change of the PartNum field.  This method consolidates all the seperate methods that were being
called when a partNum changes.  a flag for 'suppressUserPrompts' allows the user to suppress returning to the client for user input.  This
may be useful for webservices etc.  The following 3 bools are used to determine which validations should be run (getPartXRefInfo,
checkPartRevisionChange, and checkChangeKitParent).  From the UI, these are originally defaulted to true but if control is returned to the
UI from this method, the UI changes the setting of these fields when it calls it a subsequent time to only run the necessary code.  From
webservices, this allows more control over which validations are run.
   OperationID: ChangePartNumMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNumMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNumMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNumMaster(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangePartNumMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteCntCustID
   Description: This method takes in a proposed CustID, and if valid, updates the customer-
related fields on the QuoteCnt.
   OperationID: ChangeQuoteCntCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteCntCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteCntCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteCntCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeQuoteCntCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteCoPartPartNum
   Description: This method validates the QuoteCoPart.CoPartNum and defaults fields associated with the partnum.
This method should run when the QuoteCoPart.CoPartNum field changes.
   OperationID: ChangeQuoteCoPartPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteCoPartPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteCoPartPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteCoPartPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeQuoteCoPartPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteHedOTSCountryNum
   Description: Method to call when changing the QuoteHed.OTSCountryNum field.
Update Tax Region Code
   OperationID: ChangeQuoteHedOTSCountryNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteHedOTSCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteHedOTSCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteHedOTSCountryNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeQuoteHedOTSCountryNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteHedUseOTS
   Description: Method to call when changing the UseOTS field.
Refreshes the address list
   OperationID: ChangeQuoteHedUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteHedUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteHedUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteHedUseOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeQuoteHedUseOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSellingExpQty
   OperationID: ChangeSellingExpQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSellingExpQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSellingExpQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSellingExpQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeSellingExpQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipToCustID
   Description: Update Ship To Information when Ship To is changed
   OperationID: ChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeShipToCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeStandardPct
   Description: This method updates the QuoteQty markup percents and the Qtmmkup table using
the specified markup record
   OperationID: ChangeStandardPct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStandardPct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStandardPct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStandardPct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeStandardPct", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxRegionCode
   Description: Used to validate change of TaxRegionCode
   OperationID: ChangeTaxRegionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxRegionCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeTaxRegionCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProdCode
   Description: This method assigns Tax Category when changing ProdCode
   OperationID: ChangeProdCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProdCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProdCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProdCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ChangeProdCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBOMErrors
   Description: This method runs through a quote's BOM and returns a list of assembly and/or
materials that are on hold or inactive.  Quote Line cannot be engineered or QuoteHed
cannot be Quoted until these errors are taken care of
   OperationID: CheckBOMErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBOMErrors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBOMErrors_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBOMErrors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckBOMErrors", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCustomerCreditLimit
   Description: The method returns a character string if the customer will go over their credit limit
and the user is given the choice of continuing or not.
   OperationID: CheckCustomerCreditLimit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCustomerCreditLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCustomerCreditLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCustomerCreditLimit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckCustomerCreditLimit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPhaseID
   Description: The method review if phaseid is availble in ProjPhase Table
   OperationID: CheckPhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPhaseID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckPhaseID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPreCustPartInfo
   Description: The method is to be run on leave of the CustPartNum field
before the GetCustPartInfo or Update methods are run.
In case existance of CustomerPart it returns Part Number
which belongs this CustomerPart.
   OperationID: CheckPreCustPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPreCustPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPreCustPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPreCustPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckPreCustPartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPrePartInfo
   Description: The method is to be run on leave of the PartNum, Revision and CustPartNum fields
before the GetCustPartInfo or Update methods are run.  This returns all the questions
that need to be asked before a part can be changed.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPrePartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckPrePartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPreQuoteCoPartInfo
   Description: This method validates the QuoteCoPart.CoPartNum is not serial tracked or a configured part.
   OperationID: CheckPreQuoteCoPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPreQuoteCoPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPreQuoteCoPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPreQuoteCoPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckPreQuoteCoPartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckProjectID
   Description: The method review if projectid is availble in Project Table
   OperationID: CheckProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckProjectID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckQuoteNum
   Description: This method will check if the quote number entered is valid.  If the quote number
that's entered doesn't already exist and the number entered is greater than the number defined
as the starting quote number in company maintenance, then the quote number is invalid.
   OperationID: CheckQuoteNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckQuoteNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckQuoteNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckQuoteSecurity
   OperationID: CheckQuoteSecurity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckQuoteSecurity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckQuoteSecurity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRateGrpCode
   Description: Update Quote Detail information when the Part Number is changed.
   OperationID: CheckRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRateGrpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckRateGrpCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CollapsePhantom
   Description: Collapses any single Quote Assembly except Assembly 0.
   OperationID: CollapsePhantom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CollapsePhantom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollapsePhantom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CollapsePhantom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CollapsePhantom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyLines
   Description: This method copies lines from other Quotes to the current Quote
   OperationID: CopyLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CopyLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method prjWBSPhaseDefinitionIsAllowed
   OperationID: prjWBSPhaseDefinitionIsAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/prjWBSPhaseDefinitionIsAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_prjWBSPhaseDefinitionIsAllowed(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/prjWBSPhaseDefinitionIsAllowed", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExternalCRMIntegrationIsEnabled
   OperationID: GetExternalCRMIntegrationIsEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExternalCRMIntegrationIsEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExternalCRMIntegrationIsEnabled(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetExternalCRMIntegrationIsEnabled", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateOrder
   Description: This method takes the specified QuoteDtl lines and creates a Sales Order
   OperationID: CreateOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CreateOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateOrderSaveOTS
   Description: This method takes the specified QuoteDtl lines and creates a Sales Order
after saving the One Time Ship To as Customer.
   OperationID: CreateOrderSaveOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrderSaveOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderSaveOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateOrderSaveOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CreateOrderSaveOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateQuoteCntNoCustCnt
   Description: Create Quote Contact but no creating Customer Contact
   OperationID: CreateQuoteCntNoCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuoteCntNoCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteCntNoCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateQuoteCntNoCustCnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CreateQuoteCntNoCustCnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateQuoteDtlComplements
   Description: Create new lines for every complement selected for a given Line,
   OperationID: CreateQuoteDtlComplements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuoteDtlComplements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteDtlComplements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateQuoteDtlComplements(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CreateQuoteDtlComplements", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method QuoteCreditAdd
   Description: This method takes the Quote and 'C'redit ReturnLineType quoteLines that were selected
and creates a CreditMemo type invoice and invoice lines.
   OperationID: QuoteCreditAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteCreditAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteCreditAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteCreditAdd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCreditAdd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultOrderFields
   Description: This method takes the Quote and initializes the fields used during CreateOrder.
The user will then update the Quote dataset and then call the CreateOrder method
to actually create the order.
   OperationID: DefaultOrderFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultOrderFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultOrderFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultOrderFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/DefaultOrderFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSpecificPartRevIsApproved
   Description: Checks if the Revision specified is Approved
   OperationID: CheckSpecificPartRevIsApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSpecificPartRevIsApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSpecificPartRevIsApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSpecificPartRevIsApproved(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CheckSpecificPartRevIsApproved", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateQuote
   Description: This method creates a new Quote from an existing quote
   OperationID: DuplicateQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/DuplicateQuote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ETCValidateAddress
   Description: Call tax integration and loads temp tables from the results.
   OperationID: ETCValidateAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCValidateAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCValidateAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ETCValidateAddress(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ETCValidateAddress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ETCAfterAddressValidationOTS
   Description: After the tax integration has been called, update the Quote on one time shipment address if it
was changed.
   OperationID: ETCAfterAddressValidationOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCAfterAddressValidationOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCAfterAddressValidationOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ETCAfterAddressValidationOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ETCAfterAddressValidationOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportQuoteToEST
   Description: ExportQuoteToEST
   OperationID: ExportQuoteToEST
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportQuoteToEST_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportQuoteToEST_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportQuoteToEST(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExportQuoteToEST", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompetitorInfo
   Description: This method returns default information for the competitor.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
   OperationID: GetCompetitorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompetitorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompetitorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompetitorInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetCompetitorInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContactInfo
   Description: This method returns default information for the Contact.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
   OperationID: GetContactInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContactInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContactInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContactInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetContactInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistContact
   Description: This method returns exist contact shipto  Method must use parameters instead of the dataset
   OperationID: ExistContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistContact(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExistContact", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistShipTo
   Description: This method checks if Ship To is exist
   OperationID: ExistShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistShipTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/ExistShipTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustCntInfo
   Description: This method returns default information for the Contact.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
   OperationID: GetCustCntInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustCntInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustCntInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustCntInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetCustCntInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetCurrencyBase", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustomerInfo
   Description: This method returns default information for the Customer.
   OperationID: GetCustomerInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomerInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetCustomerInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustPartInfo
   Description: Defaults Part Information when the Customer Part Number changes
MUST RUN UPDATE AFTER THIS METHOD
   OperationID: GetCustPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetCustPartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlUnitPriceInfo
   Description: This method calls InternalGetDtlUnitPriceInfo.  Need to split this out so configurator
could update the price when part changes from part creation
   OperationID: GetDtlUnitPriceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlUnitPriceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlUnitPriceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlUnitPriceInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetDtlUnitPriceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlUnitPriceInfo_User
   Description: This method updates the QuoteDtl unit price and revenue fields when the
SellingExpextedQty is changed by the user
   OperationID: GetDtlUnitPriceInfo_User
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlUnitPriceInfo_User_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlUnitPriceInfo_User_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlUnitPriceInfo_User(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetDtlUnitPriceInfo_User", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExchangeRate
   Description: This method returns the Exchange Rate information for the selected Currency.  The system
may not have an exchange rate between the Quote and Base so it may use an middle Currency
so that it will go Quote Currency -> Ref Currency -> Base Currency
   OperationID: GetExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExchangeRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetKitComponents
   Description: Calls GetKitComponents from SalesKitting.p, which creates a list of QuoteDtl records
that will be treated as kit components of the given QuoteLine.
   OperationID: GetKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetKitComponents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetKitComponents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListCustom
   Description: This overload of GetList adds Quotes which ShipTo's fall within authorized territories.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetListCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustom
   Description: Invokes GetRows filtering on quotes with the authorized territories
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRowsCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForAuthorizedTerritories
   Description: This overload of GetList adds Quotes which ShipTo's fall within authorized territories.
   OperationID: GetListForAuthorizedTerritories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForAuthorizedTerritories_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForAuthorizedTerritories_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForAuthorizedTerritories(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetListForAuthorizedTerritories", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the Quote records which will be a subset
of the QuoteHEd records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFromSelectedKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetListFromSelectedKeys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMaterialMarkup
   Description: This procedure is used to be called from EQR10.p to get the MaterialMarkupP
and MaterialMarkupM fields since these two fields are external and they're needed
to be displayed on the report.
   OperationID: GetMaterialMarkup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMaterialMarkup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMaterialMarkup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMaterialMarkup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetMaterialMarkup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMiscChrgDefaults
   Description: This method returns default information for the MiscChrg.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
as well as QuoteMsc and QtQtyMsc can the same code
   OperationID: GetMiscChrgDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMiscChrgDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMiscChrgDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMiscChrgDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetMiscChrgDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMktgInfo
   Description: This method updates the description fields for the Marketing Campaign and Event fields
   OperationID: GetMktgInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMktgInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMktgInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMktgInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetMktgInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContractQuoteDtl
   Description: Method to call when adding a new QuoteDtl record for a Service Contract or a Renewal
   OperationID: GetNewContractQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContractQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContractQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContractQuoteDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewContractQuoteDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSalesKit
   Description: GetNewSalesKit
   OperationID: GetNewSalesKit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesKit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesKit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSalesKit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetNewSalesKit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPartXRefInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPerConInfo
   Description: This method returns default information for the QuoteCnt From Persons contact.
   OperationID: GetPerConInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPerConInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPhantomComponents
   Description: GetPhantomComponents
   OperationID: GetPhantomComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPhantomComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPhantomComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPhantomComponents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPhantomComponents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPriceListInfo
   Description: Finds the default pricelist if override field is blank
updates the QuoteDtl record with the new pricebreak information
called when OverridePriceList, BreakListCode or ProdCode fields change
   OperationID: GetPriceListInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceListInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceListInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPriceListInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetPriceListInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDiscountPriceListInfo
   Description: Finds the default Discount Price List if override field is blank
updates the QuoteDtl record with the new Discount break information
called when OverrideDiscPriceList, DiscBreakListCode or ProdCode fields change
   OperationID: GetDiscountPriceListInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDiscountPriceListInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDiscountPriceListInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDiscountPriceListInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetDiscountPriceListInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQtyPriceInfo
   Description: This method updates the unitprice information when the QuoteQty SellingQty has changed
   OperationID: GetQtyPriceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyPriceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyPriceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQtyPriceInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetQtyPriceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQtyPriceInfoCfgPart
   Description: This method updates the unitprice information when the QuoteQty SellingQty has changed
   OperationID: GetQtyPriceInfoCfgPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyPriceInfoCfgPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyPriceInfoCfgPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQtyPriceInfoCfgPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetQtyPriceInfoCfgPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQtyToOrdPrice
   Description: This method takes the QuantityToOrder field and returns the base and doc unit price
   OperationID: GetQtyToOrdPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyToOrdPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyToOrdPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQtyToOrdPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetQtyToOrdPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQuotedInfo
   Description: Updates the DateQuoted,ExpirationDate and FollowUpDate fields based on the Quoted field
   OperationID: GetQuotedInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuotedInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuotedInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuotedInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetQuotedInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQuoteRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Quote
   OperationID: GetQuoteRelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteRelationshipMap(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetQuoteRelationshipMap", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReasonInfo
   Description: This method returns default reason code for the specified ReasonType. Run when
the reasonType field has changed.
   OperationID: GetReasonInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReasonInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReasonInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReasonInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetReasonInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQuotesForCustomer
   Description: Returns quotes for a customer.
   OperationID: GetQuotesForCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuotesForCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuotesForCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuotesForCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetQuotesForCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRowsCustomerTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForCashReceipt
   Description: Invokes GetRows filtering on quotes for the specified Cash Receipt
   OperationID: GetRowsForCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForCashReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRowsForCashReceipt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForInvoice
   Description: Invokes GetRows filtering on quotes for the specified Invoice
   OperationID: GetRowsForInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRowsForInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForSalesOrder
   Description: Invokes GetRows filtering on quotes for the specified Sales Order
   OperationID: GetRowsForSalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForSalesOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRowsForSalesOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForShipment
   Description: Invokes GetRows filtering on quotes for the specified Customer Shipment
   OperationID: GetRowsForShipment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForShipment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRowsForShipment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the Quote records which will be a subset
of the QuoteHEd records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromSelectedKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetRowsFromSelectedKeys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSalesRepInfo
   Description: This method returns default commision information when the SalesRepCode or RoleCode
field(s) change.  Method must use parameters instead of the dataset due to the problem
changing the primary key field
   OperationID: GetSalesRepInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesRepInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesRepInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSalesRepInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetSalesRepInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetShipToInfo
   Description: This method updates the ShipTo information when the ShipToNum field changes
   OperationID: GetShipToInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipToInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetShipToInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSmartString
   Description: Generates the SmartString for kit component configured part
   OperationID: GetSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSmartString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetSmartString", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaskSetInfo
   Description: This method updates the QuoteHed.Stage field when the TaskSetId is changed
   OperationID: GetTaskSetInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskSetInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskSetInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskSetInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetTaskSetInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CompanyTaxConnectStatus
   Description: Returns the current status of Tax Connect on Company Configuration.
   OperationID: CompanyTaxConnectStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyTaxConnectStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CompanyTaxConnectStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/CompanyTaxConnectStatus", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTerrInfo
   Description: This method returns the TaskSetId when the territory ID changes
   OperationID: GetTerrInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTerrInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTerrInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTerrInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetTerrInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWSUnitPrice
   Description: This method updates the Base and Doc Unit Prices when the Quoted Unit Price
or Price Per Code changes on the Quote Worksheet form
   OperationID: GetWSUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWSUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWSUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWSUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/GetWSUnitPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method KitCompPartCreate
   Description: Configured kit component part creation
   OperationID: KitCompPartCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KitCompPartCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KitCompPartCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KitCompPartCreate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/KitCompPartCreate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMktgCamp
   Description: Call this method when the value of MktgCamp changes.
   OperationID: OnChangeMktgCamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMktgCamp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeMktgCamp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMktgEvnt
   Description: Call this method when the value of MktgCamp changes.
   OperationID: OnChangeMktgEvnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMktgEvnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgEvnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMktgEvnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/OnChangeMktgEvnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HedTaxSumRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HedTaxSumRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSubsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartSubsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QSalesRPRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QSalesRPRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtQtyMscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QtQtyMscRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtmmkupRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QtmmkupRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCntRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteCntRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCoPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteCoPartRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteComRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteComRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteDtlAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttrValueSetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteDtlAttrValueSetRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteDtlTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteHedAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteHedListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedMscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteHedMscRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteHedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteHedTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteMscRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteQtyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteQtyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxConnectStatusRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxConnectStatusRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhatIfSchedulingRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WhatIfSchedulingRow[],
}

export interface Erp_Tablesets_HedTaxSumRow{
   "Company":string,
      /**  Currency display switch  */  
   "CurrencySwitch":boolean,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  Document display symbol  */  
   "DocDisplaySymbol":string,
      /**  Document reportable amount.  */  
   "DocReportableAmt":number,
      /**  Document taxable amount.  */  
   "DocTaxableAmt":number,
      /**  Document tax amount.  */  
   "DocTaxAmt":number,
      /**  Order or Quote number this tax summary relates to.  */  
   "HedNum":number,
      /**  Tax percent  */  
   "Percent":number,
      /**  Reportable amount  */  
   "ReportableAmt":number,
      /**  Taxable amount  */  
   "TaxableAmt":number,
      /**  Tax amount  */  
   "TaxAmt":number,
      /**  Tax code  */  
   "TaxCode":string,
      /**  Sales Tax description  */  
   "TaxDescription":string,
   "GroupID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "Rpt1ReportableAmt":number,
   "Rpt2ReportableAmt":number,
   "Rpt3ReportableAmt":number,
   "Rpt1TaxableAmt":number,
   "Rpt2TaxableAmt":number,
   "Rpt3TaxableAmt":number,
   "Rpt1TaxAmt":number,
   "Rpt2TaxAmt":number,
   "Rpt3TaxAmt":number,
      /**  Rate Code on the Header Tax Summary  */  
   "RateCode":string,
      /**  Invoice Number of allocated Deposits  */  
   "AllocDepInvcNum":number,
      /**  Rate Code Description on the Header Tax Summary  */  
   "RateCodeDescription":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartSubsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Part number that this substitute Part is for.  */  
   "PartNum":string,
      /**  Substitute Part  */  
   "SubPart":string,
      /**  Indicates the record type. "S" = Substitute, "C" = Compliment  */  
   "RecType":string,
      /**  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  */  
   "SubType":string,
      /**   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  */  
   "QtyPer":number,
      /**  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  */  
   "SalesUM":string,
      /**  Optional Comment  */  
   "Comment":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DefaultSub":boolean,
      /**  Price for the Suggested Quantity  */  
   "Price":number,
      /**  Suggested Quantity  */  
   "SuggestedQty":number,
      /**  Selected Row  */  
   "Selected":boolean,
      /**  Suggested Quantity for Order Qty in Quote Detail  */  
   "SugOrderQty":number,
   "BitFlag":number,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "SubPartSellingFactor":number,
   "SubPartTrackSerialNum":boolean,
   "SubPartTrackDimension":boolean,
   "SubPartPartDescription":string,
   "SubPartIUM":string,
   "SubPartSalesUM":string,
   "SubPartTrackLots":boolean,
   "SubPartPricePerCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QSalesRPRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The quote that this record is linked to.  */  
   "QuoteNum":number,
      /**  Identifies the Sales Rep linked to the Quote.  */  
   "SalesRepCode":string,
      /**  The Sales Reps Name from the SalesRep table  */  
   "Name":string,
      /**  Identifies the primary sales rep on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  */  
   "PrimeRep":boolean,
      /**  Establishes the defaults sales rep commission rates. Default is the SALESREP.COMMISSIONPERCENT.  */  
   "RepRate":number,
      /**  Split percent is used to calculate the "commissionable"  dollar  amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   "RepSplit":number,
      /**  Link to the RoleCD Table where Roles are defined.  */  
   "RoleCode":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OfficePhone":string,
   "HomePhone":string,
   "ReportsTo":string,
   "EmailAddress":string,
   "Fax":string,
   "MobilePhone":string,
   "SalesRepTitle":string,
   "BitFlag":number,
   "QuoteNumCurrencyCode":string,
   "RoleCodeRoleDescription":string,
   "SalesRepCodePerConID":number,
   "SalesRepCodeName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QtQtyMscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number that this record is linked to.  */  
   "QuoteNum":number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   "QuoteLine":number,
      /**  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  */  
   "QtyNum":number,
      /**  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "MiscAmt":number,
      /**  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DocMiscAmt":number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   "FreqCode":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  Reserved for future use  */  
   "InMiscAmt":number,
      /**  Reserved for future use  */  
   "DocInMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt1InMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt2InMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt3InMiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from QuoteHead  */  
   "CurrSymbol":string,
      /**  CurrencyCode.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DspMiscAmt":number,
      /**  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DocDspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt1DspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt2DspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt3DspMiscAmt":number,
   "BitFlag":number,
   "MiscChrgDescription":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QtmmkupRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QuoteHead.QuoteNum that this record is linked to.  */  
   "QuoteNum":number,
      /**  The QuoteDtl.QuoteLine to which the markup is related to.  */  
   "QuoteLine":number,
      /**  the specific QuoteQty record that this markup is related to.  */  
   "QtyNum":number,
      /**  Descriptive Code assigned by the user to uniquely identify the Part Class master record. This is the unique identifier for Qtmmkup.  */  
   "ClassCode":string,
      /**  Material cost Markup Percent  */  
   "MaterialMarkUp":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if Markup is used by QuoteMtl  */  
   "Used":boolean,
   "BitFlag":number,
   "ClassCodeInactive":boolean,
   "ClassCodeDescription":string,
   "QtyNumMiscCostDesc":string,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteCntRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number. This Quote Contact is linked to this QuoteHed  */  
   "QuoteNum":number,
      /**  The unique internal number assigned to the customer for which the contact is related to.  */  
   "CustNum":number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  */  
   "ShipToNum":string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   "ConNum":number,
      /**  Name of contact.  */  
   "Name":string,
      /**  Primary contact for this quote.  */  
   "PrimeContact":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PerConID  */  
   "PerConID":number,
      /**  CustCnt.Func  */  
   "Func":string,
      /**  CustCnt.PhoneNum  */  
   "PhoneNum":string,
      /**  CustCnt.Fax  */  
   "Fax":string,
      /**  CustCnt.EmailAddress  */  
   "EmailAddress":string,
   "PerConName":string,
   "BitFlag":number,
   "ConNumName":string,
   "ConNumMiddleName":string,
   "ConNumPhoneNum":string,
   "ConNumFirstName":string,
   "ConNumLastName":string,
   "ConNumCorpName":string,
   "ConNumFaxNum":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "CustNumName":string,
   "QuoteNumCurrencyCode":string,
   "ShipToNumName":string,
   "ShipToNumInactive":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteCoPartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  */  
   "CoPartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  */  
   "CoRevisionNum":string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   "PartsPerOp":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "LbrCostBase":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "MtlCostBase":number,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   "IUM":string,
      /**  If true, MRP will not generate change suggestions for the co-part  */  
   "PreventSugg":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "PartMasterPart":boolean,
   "EnablePreventSugg":boolean,
   "ProcessMode":string,
   "BitFlag":number,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteComRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Quote that this QuoteCom is related to.  */  
   "QuoteNum":number,
      /**  The unique key for the CRMComp Master table.  */  
   "CompNum":number,
      /**  Name  */  
   "Name":string,
      /**  Identifies the primary Competitor on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  */  
   "PrimeComp":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CRMComp  */  
   "FaxNum":string,
      /**  CRMCall.PhoneNum  */  
   "PhoneNum":string,
      /**  CRMCall.EmailAddress  */  
   "EmailAddress":string,
      /**  CRMCall.CompURL  */  
   "CompURL":string,
   "BitFlag":number,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteDtlAttchRow{
   "Company":string,
   "QuoteNum":number,
   "QuoteLine":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteDtlAttrValueSetRow{
      /**  Company identifier.  */  
   "Company":string,
      /**  Quote number to which this line attribute set record is associated with.  */  
   "QuoteNum":number,
      /**  Quote number to which this line attribute set record is associated with.  */  
   "QuoteLine":number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   "AttributeValueSeq":number,
      /**  Dynamic Attribute Value Set ID for this receipt detail.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure).  */  
   "OrderQty":number,
      /**  The quantity expected to be ordered. (In selling unit of measure).  */  
   "SellingExpectedQty":number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  */  
   "SellingExpectedUM":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Unit of measure for the NumberOfPieces.  */  
   "NumberOfPiecesUOM":string,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
   "QuantityToOrder":number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
      /**  Unit of measure for the NumberOfPieces.  */  
   "DispNumberOfPiecesUOM":string,
   "BitFlag":number,
   "DynAttrValueSetShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   "Ordered":boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   "XPartNum":string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   "QuoteComment":string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   "LeadTime":string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   "Template":boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   "JobComment":string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   "MfgDetail":boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   "TaxCatID":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   "CustNum":number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Quoted":boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Expired":boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIStartHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueHour":number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   "SellingExpectedQty":number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SellingExpectedUM":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   "ConfidencePct":number,
      /**  The date this line was last updated  */  
   "LastUpdate":string,
      /**  The last User Is that updated this Quote  */  
   "LastDcdUserID":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   "DocDiscount":number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "ExpectedRevenue":number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "DocExpectedRevenue":number,
      /**  The requested ship date for the sales order  */  
   "ReqShipDate":string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   "OrderQty":number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingExpFactor":number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   "MultiRel":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   "SalesCatID":string,
      /**  Replicated from QuoteHed to easier sorting  */  
   "TerritoryID":string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   "CreatedFrom":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitPrice":number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitPrice":number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  This is the unit price based on the expected quantity.  */  
   "ExpUnitPrice":number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   "DocExpUnitPrice":number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   "ExpPricePerCode":string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   "MiscQtyNum":number,
      /**  The Quote Line has been Engineered.  */  
   "Engineer":boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   "ReadyToQuote":boolean,
      /**  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  */  
   "KitShipComplete":boolean,
      /**  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  */  
   "KitBackFlush":boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   "KitPrintCompsInv":boolean,
      /**  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  */  
   "KitPricing":string,
      /**  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  */  
   "KitParentLine":number,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  */  
   "KitQtyPer":number,
      /**  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  */  
   "DisplaySeq":number,
      /**  Project ID of linked project.  Must exist on the Project table. Can be blank.  */  
   "ProjectID":string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  To indicate whether or not the line is make direct  */  
   "MakeDirect":boolean,
      /**  Must exist on ProjPhase table if entered  */  
   "PhaseID":string,
      /**   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  */  
   "KitsLoaded":boolean,
      /**  Non-blank value prevents taxes from being calculated for this line item  */  
   "TaxExempt":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrdBasedPrice":number,
      /**  Extended Price for the quote line, rounded according to the Base currency Round rule  */  
   "ExtPriceDtl":number,
      /**  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPriceDtl":number,
      /**  Reserved for future use  */  
   "InDiscount":number,
      /**  Reserved for future use  */  
   "DocInDiscount":number,
      /**  Reserved for future use  */  
   "InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "DocInExpectedRevenue":number,
      /**  Reserved for future use  */  
   "InListPrice":number,
      /**  Reserved for future use  */  
   "DocInListPrice":number,
      /**  Reserved for future use  */  
   "InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "DocInOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "DocInExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt2InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt3InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt1InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt2InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt3InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt1InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "DocInExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt1InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt2InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt3InExtPriceDtl":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   "WorstCsPct":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   "BestCsPct":number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   "WorstCsRevenue":number,
      /**  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   "DocWorstCsRevenue":number,
   "Rpt1WorstCsRevenue":number,
   "Rpt2WorstCsRevenue":number,
   "Rpt3WorstCsRevenue":number,
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   "BestCsRevenue":number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   "DocBestCsRevenue":number,
   "Rpt1BestCsRevenue":number,
   "Rpt2BestCsRevenue":number,
   "Rpt3BestCsRevenue":number,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   "KitCompOrigSeq":number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   "KitCompOrigPart":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
   "DiscBreakListCode":string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
   "DiscListPrice":number,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
   "OverrideDiscPriceList":boolean,
      /**  Demand Contract Line  */  
   "DemandContractLine":number,
      /**  Demand Header sequence number to which this record is related.  */  
   "DemandHedSeq":number,
      /**  Demand Detail Sequence number to which this record is related.  */  
   "DemandDtlSeq":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  Indicates if this quote line is linked to an inter-company PO line.  */  
   "Linked":boolean,
      /**  Indicates if the price of the quote line can be changed.  */  
   "LockPrice":boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Indicates that the line item was closed before any shipments were made against it.  */  
   "VoidLine":boolean,
      /**  Indicate that the item or the product group has a warranty.  */  
   "Warranty":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  EstimateGUID  */  
   "EstimateGUID":string,
      /**  RFQCurrBaseEst  */  
   "RFQCurrBaseEst":string,
      /**  RFQTemplate  */  
   "RFQTemplate":string,
      /**  CreateEstimate  */  
   "CreateEstimate":boolean,
      /**  Rating  */  
   "Rating":string,
      /**  EstimateUserID  */  
   "EstimateUserID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  NeedByDate  */  
   "NeedByDate":string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   "ProcessMode":string,
      /**  ECC Quote Number  */  
   "ECCQuoteNum":string,
      /**  ECC Quote Line  */  
   "ECCQuoteLine":number,
      /**  ECC Comment Ref  */  
   "ECCCmmtRef":string,
      /**  ECCComment  */  
   "ECCComment":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Tax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "DocTax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Rpt1Tax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Rpt2Tax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Rpt3Tax":number,
      /**  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  Indicates if no tax recalculation by the system is supposed to be done.  */  
   "NoTaxRecalc":boolean,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "TotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "DocTotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "Rpt1TotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "Rpt2TotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "Rpt3TotalSATax":number,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  This field holds the id of this quote line in the External CRM  */  
   "ExternalCRMQuoteLineID":string,
      /**  Type for returns: Blank, (C)redit or (S)tandard  */  
   "ReturnLineType":string,
      /**  Base price before any price breaks and discounts  */  
   "MSRP":number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   "DocMSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   "Rpt1MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   "Rpt2MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   "Rpt3MSRP":number,
      /**  Distributor end customer price.  */  
   "EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   "DocEndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   "Rpt1EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   "Rpt2EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   "Rpt3EndCustomerPrice":number,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  Mark For ShipToNum  */  
   "MFShipToNum":string,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   "UseOTMF":boolean,
      /**  One Time Mark For Contact Name  */  
   "OTMFName":string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   "OTMFAddress1":string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   "OTMFAddress2":string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   "OTMFAddress3":string,
      /**  City portion of the One Time Mark For address.  */  
   "OTMFCity":string,
      /**  The state or province portion of the One Time Mark For address.  */  
   "OTMFState":string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   "OTMFZIP":string,
      /**  One Time Mark For Contact Name  */  
   "OTMFContact":string,
      /**  Fax number for the One Time Mark For.  */  
   "OTMFFaxNum":string,
      /**  Phone number for the One Time Mark For  */  
   "OTMFPhoneNum":string,
      /**  Country number for the One Time Mark For  */  
   "OTMFCountryNum":number,
      /**  Promotional Price offered to Dealer and Distributors  */  
   "PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   "DocPromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   "Rpt1PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   "Rpt2PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   "Rpt3PromotionalPrice":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   "AttributeSetID":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   "KBOriginalConfigProdID":number,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
   "BaseExtPrice":number,
   "BaseMiscAmt":number,
   "BasePotential":number,
      /**  If yes, then a new non-standard part was added with no description and validation needs to be run again  */  
   "CheckPartDescription":boolean,
      /**  PLM Flag  */  
   "CodePLM":boolean,
      /**  Valid values are "win" "lose" "next" "next" is the default  */  
   "Conclusion":string,
   "ConfigType":string,
      /**  Indicates whether the part is/can be configured  */  
   "Configured":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   "CurrSymbol":string,
      /**  Date that the quoter considered the quoting process for this quote complete.  */  
   "DateQuoted":string,
      /**  Indicates if the discount fields should be disabled for the current quote line detail.  */  
   "DisableDiscounts":boolean,
      /**  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DocDspDiscount":number,
      /**  Display Document unit price based on the expected quantity.  */  
   "DocDspExpUnitPrice":number,
   "DocExtPrice":number,
   "DocMiscAmt":number,
   "DocOrderUnitPrice":number,
   "DocPotential":number,
   "DocTotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "DocTotalQuote":number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   "DocTotalWHTax":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DspDiscount":number,
      /**  Used to displayed UOM for expected quantity for detail line  */  
   "DspExpectedUM":string,
   "EnableRenewalNbr":boolean,
      /**  The date when this quote expires.  */  
   "ExpirationDate":string,
      /**  Indicates whether the part has at least one Complement  */  
   "HasComplement":boolean,
   "HasCoParts":boolean,
      /**  Indicates if this Quote line has an associated credit memo (only for dealer portal)  */  
   "HasCreditMemo":boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   "HasDowngrade":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasSubstitute":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasUpgrade":boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   "KitChangeParms":boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   "KitDisable":boolean,
      /**  The description for Kit Flag. "P" = Parent, "C" = Component.  */  
   "KitFlagDescription":string,
   "KitOrderQtyUOM":string,
   "LineStatus":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
   "MFCustID":string,
   "OrderUM":string,
   "OrderUnitPrice":number,
      /**  If yes, the line will be copied to the Order  */  
   "OrderWorthy":boolean,
      /**  Internal flag to identify if the Part is an Inventory Part.  */  
   "PartExists":boolean,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
   "QtyBearing":boolean,
   "QuantityToOrder":number,
      /**  Indicates whether to Refresh the QuoteQty table  */  
   "RefreshQty":boolean,
      /**  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  */  
   "RemoveManAdTax":boolean,
   "Rpt1BaseExtPrice":number,
   "Rpt1BaseMiscAmt":number,
   "Rpt1BasePotential":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1DspDiscount":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt1DspExpUnitPrice":number,
   "Rpt1OrderUnitPrice":number,
   "Rpt1TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "Rpt1TotalQuote":number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   "Rpt1TotalWHTax":number,
   "Rpt2BaseExtPrice":number,
   "Rpt2BaseMiscAmt":number,
   "Rpt2BasePotential":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2DspDiscount":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt2DspExpUnitPrice":number,
   "Rpt2OrderUnitPrice":number,
   "Rpt2TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "Rpt2TotalQuote":number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   "Rpt2TotalWHTax":number,
   "Rpt3BaseExtPrice":number,
   "Rpt3BaseMiscAmt":number,
   "Rpt3BasePotential":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3DspDiscount":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt3DspExpUnitPrice":number,
   "Rpt3OrderUnitPrice":number,
   "Rpt3TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "Rpt3TotalQuote":number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   "Rpt3TotalWHTax":number,
      /**  Selected row  */  
   "Selected":boolean,
   "ShipByDate":string,
   "TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "TotalQuote":number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   "TotalWHTax":number,
      /**   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  */  
   "UpdateReq":boolean,
      /**  Indicates that the Quote should be used as the BOM when creating a job for the linked order  */  
   "UseQuoteBOM":boolean,
      /**  Delimited list of Available Price Lists  */  
   "AvailPriceLists":string,
      /**  Display unit price based on the expected quantity.  */  
   "DspExpUnitPrice":number,
   "ECCLineCRQ":number,
      /**  Allow enable/disable for the Dynamic Attributes button on a Quote Line  */  
   "EnableDynAttrButton":boolean,
      /**  Flag indicating whether to enable CodePLM or not  */  
   "EnablePLM":boolean,
   "MarkForAddressFormatted":string,
   "InventoryAttributeSetID":number,
      /**  The amount of discount for display  */  
   "LessDiscount":number,
      /**  The amount of discount for display in Doc currency  */  
   "DocLessDiscount":number,
      /**  The amount of discount for display in reporting currency  */  
   "Rpt1LessDiscount":number,
      /**  The amount of discount for display in reporting currency  */  
   "Rpt2LessDiscount":number,
      /**  The amount of discount for display in reporting currency  */  
   "Rpt3LessDiscount":number,
      /**   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  */  
   "AllowTaxCodeUpd":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "DiscBreakListCodeListDescription":string,
   "DiscBreakListCodeEndDate":string,
   "DiscBreakListCodeStartDate":string,
   "MFShipToNumInactive":boolean,
   "OTMFCountryDescription":string,
   "PartNumDefaultAttributeSetID":number,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PriceBreakListDescription":string,
   "PriceGroupDescription":string,
   "ProdCodeDescription":string,
   "QuoteNumInPrice":boolean,
   "QuoteNumCurrencyCode":string,
   "SalesCatIDDescription":string,
   "TaxCatIDDescription":string,
   "TaxRegionDescription":string,
   "TaxRegionTaxConnectCalc":boolean,
   "TerritoryIDTerritoryDesc":string,
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteDtlTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote Number  */  
   "QuoteNum":number,
      /**  Quote Line related to the Tax Record  */  
   "QuoteLine":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an quote. When the sales tax field EcAquisition is checked then 2 quote tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   "TaxableAmt":number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this quote. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  The user ID for the user who created this record.  */  
   "CreatedBy":string,
      /**  The date and time of creating.  */  
   "CreatedOn":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  A flat discount amount for the tax.  */  
   "Discount":number,
      /**  A flat discount amount for the tax converted to the customers currency.  */  
   "DocDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Tax Rate Date  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  Document display symbol  */  
   "DocDisplaySymbol":string,
      /**  Currency switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
   "BitFlag":number,
   "RateCodeDescription":string,
   "SalesTaxDescDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteHedAttchRow{
   "Company":string,
   "QuoteNum":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   "QuoteNum":number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   "CustNum":number,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   "DueDate":string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   "Quoted":boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   "DateQuoted":string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   "ExpirationDate":string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   "FollowUpDate":string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   "Reference":string,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   "Expired":boolean,
      /**  Full Description for CurrentStage field  */  
   "CurrentStageDesc":string,
      /**  Link to the territory Id for this LOQ  */  
   "TerritoryID":string,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Bill to customer id.  */  
   "BTCustID":string,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  Bill to customer name.  */  
   "BTCustomerName":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
   "CustomerName":string,
   "TerritoryTerritoryDesc":string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   "ReasonType":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   "ConfidencePct":number,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   "MktgCampaignID":string,
      /**  Link to the marketing event associated with this record.  */  
   "MktgEvntSeq":number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   "Ordered":boolean,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteHedMscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number that this record is linked to.  */  
   "QuoteNum":number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   "QuoteLine":number,
      /**  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  */  
   "QtyNum":number,
      /**  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "MiscAmt":number,
      /**  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DocMiscAmt":number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   "FreqCode":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  Reserved for future use  */  
   "InMiscAmt":number,
      /**  Reserved for future use  */  
   "DocInMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt1InMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt2InMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt3InMiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from QuoteHedMsc  */  
   "CurrSymbol":string,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DspMiscAmt":number,
      /**  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DocDspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt1DspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt2DspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt3DspMiscAmt":number,
   "BitFlag":number,
   "MiscCodeDescription":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   "QuoteNum":number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   "CustNum":number,
      /**  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  */  
   "EntryDate":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Contains comments about the overall Quote. These will be printed on the Quote form.  */  
   "QuoteComment":string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   "DueDate":string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   "Quoted":boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   "DateQuoted":string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   "ExpirationDate":string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   "FollowUpDate":string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   "Reference":string,
      /**   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff1":boolean,
      /**  Optional check off # 2.  */  
   "CheckOff2":boolean,
      /**  Optional check off # 3.  */  
   "CheckOff3":boolean,
      /**  Optional check off # 4.  */  
   "CheckOff4":boolean,
      /**  Optional check off # 5.  */  
   "CheckOff5":boolean,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   "Expired":boolean,
      /**  System maintained flag - set to yes when the quote follow up alert has been sent.  */  
   "FlwAlrtSnt":boolean,
      /**  System maintained flag - set to yes when the quote due date alert has been sent.  */  
   "DueAlrtSnt":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  A = High, Z = Low  */  
   "LeadRating":string,
      /**  Link to the territory Id for this LOQ  */  
   "TerritoryID":string,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  */  
   "ParentQuoteNum":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  The date this quote is expected to close.  */  
   "ExpectedClose":string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   "ReasonType":string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   "ReasonCode":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   "ConfidencePct":number,
      /**  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  */  
   "DiscountPercent":number,
      /**  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  This quote is no longer updatable.  */  
   "QuoteClosed":boolean,
      /**  The date that the Quote was closed.  */  
   "ClosedDate":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   "MktgCampaignID":string,
      /**  Link to the marketing event associated with this record.  */  
   "MktgEvntSeq":number,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   "CallTypeCode":string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   "TermsCode":string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   "Ordered":boolean,
      /**  Indicates if order based discounting needs to be applied to the quote.  */  
   "ApplyOrderBasedDisc":boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  The help desk case that created this quote.  */  
   "HDCaseNum":number,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  */  
   "LockRate":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  */  
   "ReadyToCalc":boolean,
      /**  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   "ExportRequested":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  */  
   "QuoteAmt":number,
      /**  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   "DocQuoteAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1QuoteAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2QuoteAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3QuoteAmt":number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   "WorstCsPct":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   "BestCsPct":number,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  Demand Header sequence number to which this record is related.  */  
   "DemandHeadSeq":number,
      /**  Defines if this document is marked as EDI Ready.  */  
   "EDIReady":boolean,
      /**  Quote created from EDI interfaced module.  */  
   "EDIQuote":boolean,
      /**  Updated from EDI module this type of document is created.  */  
   "EDIAck":boolean,
      /**  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  */  
   "OutboundQuoteDocCtr":number,
      /**  Date in which the related demand was last processed.  */  
   "DemandProcessDate":string,
      /**  System Time when demand was last processed.  */  
   "DemandProcessTime":number,
      /**  EDI Transaction Control Number  */  
   "LastTCtrlNum":string,
      /**  EDI Batch Control Number  */  
   "LastBatchNum":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "DocTotalSATax":number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "DocTotalTax":number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "DocTotalWHTax":number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt1TotalSATax":number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt1TotalTax":number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt1TotalWHTax":number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt2TotalSATax":number,
      /**   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt2TotalTax":number,
      /**   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt2TotalWHTax":number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt3TotalSATax":number,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt3TotalTax":number,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt3TotalWHTax":number,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  Freight charges will not be returned if 'yes'  */  
   "DropShip":boolean,
      /**   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "TotalSATax":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "TotalTax":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "TotalWHTax":number,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   "ICPONum":number,
      /**  Indicates if this quote header is linked to an inter-company PO header.  */  
   "Linked":boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  */  
   "NeedByDate":string,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   "OTSCustSaved":boolean,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   "OverrideService":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  */  
   "RequestDate":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Indicates that the Quote item was closed before any shipments were made against it.  */  
   "VoidQuote":boolean,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Total discount percent.  */  
   "TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "TotalExpected":number,
   "TotalGrossValue":number,
   "TotalMiscAmt":number,
   "TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "DocTotalBestCs":number,
   "DocTotalDiscount":number,
      /**  Total discount percent.  */  
   "DocTotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "DocTotalExpected":number,
   "DocTotalGrossValue":number,
   "DocTotalMiscAmt":number,
   "DocTotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "DocTotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "Rpt1TotalBestCs":number,
   "Rpt1TotalDiscount":number,
      /**  Total discount percent.  */  
   "Rpt1TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "Rpt1TotalExpected":number,
   "Rpt1TotalGrossValue":number,
   "Rpt1TotalMiscAmt":number,
   "Rpt1TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "Rpt1TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "Rpt2TotalBestCs":number,
   "Rpt2TotalDiscount":number,
      /**  Total discount percent.  */  
   "Rpt2TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "Rpt2TotalExpected":number,
   "Rpt2TotalGrossValue":number,
   "Rpt2TotalMiscAmt":number,
   "Rpt2TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "Rpt2TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "Rpt3TotalBestCs":number,
   "Rpt3TotalDiscount":number,
      /**  Total discount percent.  */  
   "Rpt3TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "Rpt3TotalExpected":number,
   "Rpt3TotalGrossValue":number,
   "Rpt3TotalMiscAmt":number,
   "Rpt3TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "Rpt3TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "TotalBestCs":number,
   "TotalDiscount":number,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  LOQPrepressText  */  
   "LOQPrepressText":string,
      /**  LOQNewPageOnQuoteLine  */  
   "LOQNewPageOnQuoteLine":boolean,
      /**  LOQBookPCFinishing  */  
   "LOQBookPCFinishing":boolean,
      /**  LOQBookPCPaper  */  
   "LOQBookPCPaper":boolean,
      /**  LOQBookPCPress  */  
   "LOQBookPCPress":boolean,
      /**  LOQBookPCPlates  */  
   "LOQBookPCPlates":boolean,
      /**  LOQVariations  */  
   "LOQVariations":boolean,
      /**  AEPLOQType  */  
   "AEPLOQType":string,
      /**  LOQPrepressStyle  */  
   "LOQPrepressStyle":string,
      /**  QuoteCSR  */  
   "QuoteCSR":string,
      /**  DueHour  */  
   "DueHour":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Quote was confirmed/rejected by ECC Web  */  
   "ECCConfirmed":boolean,
      /**  Quote was confirmed/rejected by this ECC user  */  
   "ECCConfirmedBy":string,
      /**  ECC quote message: RFQ or GQR  */  
   "ECCMsgType":string,
      /**  Quote is ready to be approved by user via ECC web site.  */  
   "ECCWebReady":boolean,
      /**  ECC Quote Number  */  
   "ECCQuoteNum":string,
      /**  ECC Comment Reference Number  */  
   "ECCCmmtRef":string,
      /**  ECCComment  */  
   "ECCComment":string,
      /**  ECC Quote Status  */  
   "ECCStatus":string,
      /**  ECC Expiration Date  */  
   "ECCExpirationDate":string,
      /**  ECCCmmtRefSK  */  
   "ECCCmmtRefSK":string,
      /**  This field defines if the Quote  is synchronized to an External CRM.  */  
   "ExternalCRMQuote":boolean,
      /**  This field holds the  id of this quote in the External CRM  */  
   "ExternalCRMQuoteID":string,
      /**  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  */  
   "ExternalCRMOrderID":string,
      /**  Web Sales Rep ID  */  
   "ECCSalesRepID":string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Tax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "DocTax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Rpt1Tax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Rpt2Tax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Rpt3Tax":number,
      /**  HdrTaxNoUpdt  */  
   "HdrTaxNoUpdt":boolean,
      /**  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSync":string,
      /**  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  */  
   "ExternalCRMSyncRequired":boolean,
      /**  Total of claims credit lines  */  
   "TotalClaimsCredit":number,
      /**  Total of claims credit lines in customer currency  */  
   "DocTotalClaimsCredit":number,
      /**  Total of claims credit lines in report currency  */  
   "Rpt1TotalClaimsCredit":number,
      /**  Total of claims credit lines in report currency  */  
   "Rpt2TotalClaimsCredit":number,
      /**  Total of claims credit lines in report currency  */  
   "Rpt3TotalClaimsCredit":number,
      /**  Total Quote claims credit Invoice Taxes.  */  
   "TotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in customer currency.  */  
   "DocTotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   "Rpt1TotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   "Rpt2TotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   "Rpt3TotalClaimsTax":number,
      /**  Total Quote claims credit Self Assessed Taxes.  */  
   "TotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "DocTotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "Rpt1TotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "Rpt2TotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "Rpt3TotalClaimsSATax":number,
      /**  Total Quote claims credit Withholding Taxes.  */  
   "TotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in customer currency.  */  
   "DocTotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   "Rpt1TotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   "Rpt2TotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   "Rpt3TotalClaimsWHTax":number,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  Incoterm Code  */  
   "IncotermCode":string,
      /**  Incoterm Location  */  
   "IncotermLocation":string,
   "AddrList":string,
   "BaseCurrencyID":string,
      /**  Bill To Customer Name.  */  
   "BTCustomerName":string,
      /**  Audit Log change description  */  
   "ChangeDescription":string,
   "CheckOffLabel1":string,
   "CheckOffLabel2":string,
   "CheckOffLabel3":string,
   "CheckOffLabel4":string,
   "CheckOffLabel5":string,
   "Conclusion":string,
      /**  Primary Contact Name  */  
   "ConName":string,
   "CurrencySwitch":boolean,
      /**  Full Description of the CurrentStage field  */  
   "CurrentStageDesc":string,
      /**  Value of the Customer.AllowOTS (customer allows one time shipment)  */  
   "CustAllowOTS":boolean,
   "CustOnCreditHold":boolean,
      /**  Number of days Quote has been open  */  
   "DaysOpen":number,
      /**   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  */  
   "DiscountPercentCalc":number,
      /**  Total tax in Doc currency. The sum of all the tax details for the quote.  */  
   "DocTaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "DocTotalQuote":number,
      /**  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   "dspBTCustID":string,
   "EmailAddress":string,
      /**  Indicates if it's okay to enable OrderBased Pricing  */  
   "EnableOrderBasedDisc":boolean,
      /**   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  */  
   "ExpectedCsPct":number,
   "FaxNum":string,
   "FOB":string,
   "FOBDescription":string,
      /**  Used by IU to disabled Currency Code  */  
   "HasQuoteLines":boolean,
      /**  EqSyst.LogChanges  */  
   "LogChanges":boolean,
      /**  Order Date  */  
   "OrderDate":string,
   "OrderDiscount":number,
   "OrderPONum":string,
   "OrderShipVia":string,
   "OrderTerms":string,
   "OTSSaved":boolean,
   "OTSShipToNum":string,
   "PhoneNum":string,
   "PreventQQChange":boolean,
      /**  Label for ExchangeRate  */  
   "RateLabel":string,
   "Rpt1TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "Rpt1TotalQuote":number,
   "Rpt2TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "Rpt2TotalQuote":number,
   "Rpt3TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "Rpt3TotalQuote":number,
   "SalesRepCode":string,
   "SalesRepName":string,
   "ShipByDate":string,
   "ShipToAddrList":string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "TotalQuote":number,
      /**   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  */  
   "WorseCsPctCalc":number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   "BaseCurrSymbol":string,
      /**   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  */  
   "BestCsPctCalc":number,
      /**  Bill To Address List.  */  
   "BTAddressList":string,
      /**  Customer ID of the bill to customer.  */  
   "BTCustID":string,
      /**  Indicates if the order contains any credit type line  */  
   "HasCreditLines":boolean,
      /**  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  */  
   "IsValidECC":boolean,
      /**  Flag indicating whether to enable CaseNum or not  */  
   "EnableHDCaseNum":boolean,
      /**  Indicates if the quote can be updated  */  
   "UpdateAllowed":boolean,
      /**  Formatted address  */  
   "AddressFormatted":string,
      /**  Ship To Address formatted  */  
   "ShipToAddressFormatted":string,
      /**  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  */  
   "PromptTaxRegionCode":boolean,
      /**  Indicates a customer referenced on the quote is inactive.  */  
   "InactiveCustomer":boolean,
      /**  Update primary contact on save of the quote header  */  
   "UpdatePrimContact":boolean,
      /**  Flag indicating whether to enable Incoterm Location  */  
   "EnableIncotermLocation":boolean,
   "BitFlag":number,
   "ActiveTaskTaskDescription":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyBaseCurr":boolean,
   "CustomerAllowShipTo3":boolean,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "CustomerName":string,
   "CustomerCheckDuplicatePO":boolean,
   "HDCaseDescription":string,
   "IncotermsDescription":string,
   "LastTaskTaskDescription":string,
   "MktgCpgnCampDescription":string,
   "MktgEventEvntDescription":string,
   "OTSCountryNumISOCode":string,
   "OTSCountryNumDescription":string,
   "OTSCountryNumEUMember":boolean,
   "OTSTaxRegionCodeDescription":string,
   "RateGrpDescription":string,
   "ReasonDescription":string,
   "ResponseCallTypeDesc":string,
   "ShipToBTName":string,
   "ShipToCustID":string,
   "ShipToName":string,
   "ShipToNumName":string,
   "ShipToNumInactive":boolean,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
   "ShipViaInactive":boolean,
   "TaskSetTaskSetDescription":string,
   "TaskSetWorkflowType":string,
   "TaxRegionTaxConnectCalc":boolean,
   "TaxRegionDescription":string,
   "TermsDescription":string,
   "TerritoryTerritoryDesc":string,
   "XbSystCalcQuoteTax":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteHedTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote Number  */  
   "QuoteNum":number,
      /**  Tax ID from Sales Tax  */  
   "TaxCode":string,
      /**  Rate Code on the Header Tax Summary  */  
   "RateCode":string,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Taxable Amount for this quote  */  
   "TaxableAmt":number,
      /**  The reportable sales amount for this quote  */  
   "ReportableAmt":number,
      /**  Calculated Tax Percent  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "DocTaxAmt":number,
      /**  Taxable Amount for this quote  */  
   "DocTaxableAmt":number,
      /**  The reportable sales amount for this quote  */  
   "DocReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  The user ID for the user who created this record.  */  
   "CreatedBy":string,
      /**  The date and time of creating.  */  
   "CreatedOn":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangedOn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Tax for claims credit tax.  This tax should not be included with regular tax.  */  
   "ClaimsTax":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  Currency switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
      /**  Document display symbol  */  
   "DocDisplaySymbol":string,
   "BitFlag":number,
   "QuoteHedCurrencyCode":string,
   "RateCodeDescription":string,
   "SalesTaxDescDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteMscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number that this record is linked to.  */  
   "QuoteNum":number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   "QuoteLine":number,
      /**  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  */  
   "QtyNum":number,
      /**  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "MiscAmt":number,
      /**  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DocMiscAmt":number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   "FreqCode":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  Reserved for future use  */  
   "InMiscAmt":number,
      /**  Reserved for future use  */  
   "DocInMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt1InMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt2InMiscAmt":number,
      /**  Reserved for future use  */  
   "Rpt3InMiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   "CurrSymbol":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DspMiscAmt":number,
      /**  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "DocDspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt1DspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt2DspMiscAmt":number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   "Rpt3DspMiscAmt":number,
   "BitFlag":number,
   "MiscCodeDescription":string,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteQtyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote # that this record is linked to.  */  
   "QuoteNum":number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   "QuoteLine":number,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  */  
   "QtyNum":number,
      /**  Represents one of the requested Quote Quantities for the line item using QuoteQty.IUM.  */  
   "OurQuantity":number,
      /**  Quoted unit price for the given quantity. This value is entered by the user.  */  
   "UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed).
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteQty.Quantity by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   "PricePerCode":string,
      /**  Material Bur Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   "MtlBurMarkUp":number,
      /**  Material Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   "MaterialMarkUp":number,
      /**  SubContract Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   "SubcontractMarkUp":number,
      /**  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   "LaborMarkUp":number,
      /**  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   "BurdenMarkUp":number,
      /**  Miscellaneous Cost description.  */  
   "MiscCostDesc":string,
      /**  Miscellaneous Cost amount that will be considered in the unit price calculations.  */  
   "MiscCost":number,
      /**  Miscellaneous Cost Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   "MiscCostMarkUp":number,
      /**  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  */  
   "CommissionPct":number,
      /**  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values. Prices can be calculated either as a straight markup of cost ( Cost + (Cost *  x %)) or a percent of profit ( Cost / (100% -  x%).   PercentType "M" = straight markup, "P" = Profit Percent. Defaulted from referenced QMarkup, from EQSyst.PercentType if not blank, else default as "M".  */  
   "PercentType":string,
      /**  Unit of Measure (how it is stocked).  Use the default Part.IUM if its a valid part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "IUM":string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Represents one of the requested Quote Quantities for the line item using QuoteQty.SUM.  */  
   "SellingQuantity":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Unique identifier of this material markup. Defaults from its parent table Qmarkup.  */  
   "MarkUpID":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Reserved for future use  */  
   "InUnitPrice":number,
      /**  Reserved for future use  */  
   "DocInUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InUnitPrice":number,
      /**  PriceSource  */  
   "PriceSource":string,
      /**  PricePerAdl1000  */  
   "PricePerAdl1000":number,
      /**  TotalSellPrice  */  
   "TotalSellPrice":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DocPricePerAdl1000  */  
   "DocPricePerAdl1000":number,
      /**  DocTotalSellPrice  */  
   "DocTotalSellPrice":number,
      /**  Indicates if the unit price for the qty break has been manually modified  */  
   "UserChangedUnitPrice":boolean,
      /**  Worksheet field  */  
   "CalcProfit":number,
      /**  CalcProfit Profit calculation  */  
   "CalcProfitProfit":number,
      /**  Worksheet field  */  
   "CalcUnitCost":number,
      /**  Worksheet field  */  
   "CalcUnitPriceMarkup":number,
      /**  Worksheet field  */  
   "CalcUnitPriceProfit":number,
      /**  Worksheet field  */  
   "CalcUPCommMarkup":number,
      /**  Worksheet field  */  
   "CalcUPCommProfit":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   "CurrSymbol":string,
      /**  Flag to indicate when to disable/enable material markup field  */  
   "DisableMtlMarkup":boolean,
      /**  External field for MaterialMarkup Markup calculations  */  
   "MaterialMarkupM":number,
      /**  External field for MaterialMarkup Profit calculations  */  
   "MaterialMarkupP":number,
      /**  Indicates if the record has a miscellaneous charge associated with it  */  
   "MiscChrg":string,
      /**  Worksheet field  */  
   "PriceBurMarkup":number,
      /**  Worksheet field  */  
   "PriceBurProfit":number,
      /**  Worksheet field  */  
   "PriceLbrMarkup":number,
      /**  Worksheet field  */  
   "PriceLbrProfit":number,
      /**  Worksheet field  */  
   "PriceMscChrgMarkup":number,
      /**  Worksheet field  */  
   "PriceMscChrgProfit":number,
      /**  Worksheet field  */  
   "PriceMtlBurMarkup":number,
      /**  Worksheet field  */  
   "PriceMtlBurProfit":number,
      /**  Worksheet field  */  
   "PriceMtlMarkup":number,
      /**  Worksheet field  */  
   "PriceMtlProfit":number,
      /**  Integer value of the PricePerCode field (for calculations)  */  
   "PricePerFactor":number,
      /**  Worksheet field  */  
   "PriceSubMarkup":number,
      /**  Worksheet field  */  
   "PriceSubProfit":number,
      /**  Worksheet field  */  
   "PriceTotalCommMarkup":number,
      /**  Worksheet field  */  
   "PriceTotalCommProfit":number,
      /**  Worksheet field  */  
   "PriceTotalMarkup":number,
      /**  Worksheet field  */  
   "PriceTotalProfit":number,
      /**  Worksheet field  */  
   "QuotedMarkup":number,
      /**  Worksheet field  */  
   "QuotedProfit":number,
      /**  If marked then the totals are not updated and a ?Roll up costs? is needed.  */  
   "RollUpCostNeeded":boolean,
      /**  QuoteCst.TotalBurCost - Worksheet temp field  */  
   "TotalBurCost":number,
      /**  Worksheet field  */  
   "TotalCommission":number,
      /**  Total Commision Profit calculation  */  
   "TotalCommProfit":number,
      /**  Worksheet field  */  
   "TotalCost":number,
      /**  QuoteCst.TotalLbrCost - Worksheet temp field  */  
   "TotalLbrCost":number,
      /**  Worksheet field  */  
   "TotalMarkup":number,
      /**  QuoteCst.TotalMtlBurCost - Worksheet temp field  */  
   "TotalMtlBurCost":number,
      /**  QuoteCst.TotalMtlCost - Worksheet temp field  */  
   "TotalMtlCost":number,
      /**  QuoteCst.TotalProdBurHrs - Worksheet temp field  */  
   "TotalProdBurHrs":number,
      /**  QuoteCst.TotalProdLbrHrs - Worksheet temp field  */  
   "TotalProdLbrHrs":number,
      /**  Worksheet field  */  
   "TotalProfit":number,
      /**  Worksheet field  */  
   "TotalQuotedPrice":number,
      /**  QuoteCst.TotalSetupBurHrs - Worksheet temp field  */  
   "TotalSetupBurHrs":number,
      /**  QuoteCst.TotalSetupLbrHrs - Worksheet temp field  */  
   "TotalSetupLbrHrs":number,
      /**  QuoteCst.TotalSubCost - Worksheet temp field  */  
   "TotalSubCost":number,
      /**  Worksheet Quoted Unit Price  */  
   "WQUnitPrice":number,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  Worksheet field  */  
   "CalcMarkup":number,
      /**  CalcMarkup Profit calculation  */  
   "CalcMarkupProfit":number,
   "BitFlag":number,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxConnectStatusRow{
      /**  Company  */  
   "Company":string,
      /**  If true, service is down. If false, service is up.  */  
   "ETCOffline":boolean,
      /**  Error message returned from the call to the tax service.  */  
   "ErrorMessage":string,
      /**  This is the success/failure status of the call to tax connect. If false, the call failed, if true it was successful  */  
   "TCStatus":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WhatIfSchedulingRow{
   "CompletionDate":string,
   "ConsiderLeadTime":boolean,
      /**  Production Qty  */  
   "ProdQty":number,
   "ProdStartDate":string,
   "SchedFinitely":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface AllowUndoReadyToQuote_output{
}

   /** Required : 
      @param quoteNum
   */  
export interface ApplyOrderBasedDiscount_input{
      /**  The current QuoteHed.QuoteNum field  */  
   quoteNum:number,
}

export interface ApplyOrderBasedDiscount_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param quoteNum
      @param quoteLines
      @param quoteFields
   */  
export interface ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_input{
   quoteNum:number,
   quoteLines:string,
   quoteFields:string,
}

export interface ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param sellingExpectedUM
      @param ds
   */  
export interface AssignAttrSellingExpectedUM_input{
      /**  QuoteNum  */  
   quoteNum:number,
      /**  QuoteNum  */  
   quoteLine:number,
      /**  Quote sellingExpectedUM  */  
   sellingExpectedUM:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface AssignAttrSellingExpectedUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param ds
   */  
export interface AssignQuoteDtlAttributeDispValues_input{
      /**  QuoteNum  */  
   quoteNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface AssignQuoteDtlAttributeDispValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param inQuoteQtyUM
      @param inPartNum
      @param inSellingUM
      @param inKitParentUnitPrice
      @param inquantity
   */  
export interface CalcConvUOMUnitPrice_input{
   inQuoteQtyUM:string,
   inPartNum:string,
   inSellingUM:string,
   inKitParentUnitPrice:number,
   inquantity:number,
}

export interface CalcConvUOMUnitPrice_output{
   returnObj:number,
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param qtyNum
      @param ds
   */  
export interface CalcMaterialMarkup_input{
      /**  Quote Num  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Quote Qty Number  */  
   qtyNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CalcMaterialMarkup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param quantityToOrder
      @param sellingUM
      @param OrderHedDiscountPercent
      @param ds
   */  
export interface Calc_QuoteDtlDiscount_input{
   quoteNum:number,
   quoteLine:number,
   quantityToOrder:number,
   sellingUM:string,
   OrderHedDiscountPercent:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface Calc_QuoteDtlDiscount_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CalculateQuoteDtlUnitPrice_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CalculateQuoteDtlUnitPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDiscBreakListCode_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeDiscBreakListCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param newDocOrderUnitPrice
      @param ds
   */  
export interface ChangeDocOrderUnitPrice_input{
      /**  The new DocOrderUnitPrice value.  */  
   newDocOrderUnitPrice:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeDocOrderUnitPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipContractNum
      @param ds
   */  
export interface ChangeDtlContractNum_input{
      /**  Proposed Contract Number  */  
   ipContractNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeDtlContractNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipRenewalNbr
      @param ds
   */  
export interface ChangeDtlRenewalNbr_input{
      /**  Proposed Renewal Number  */  
   ipRenewalNbr:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeDtlRenewalNbr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipReturnLineType
      @param ds
   */  
export interface ChangeDtlReturnLineType_input{
      /**  The proposed Return Line Type  */  
   ipReturnLineType:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeDtlReturnLineType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeKitPricing_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeKitPricing_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeKitQtyPer_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeKitQtyPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipMFCustID
      @param ds
   */  
export interface ChangeMFCustID_input{
      /**  The proposed Mark For Customer ID  */  
   ipMFCustID:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeMFCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param proposedMFShipToNum
      @param ds
   */  
export interface ChangeMFShipToNum_input{
      /**  The Proposed ShipToNum  */  
   proposedMFShipToNum:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeMFShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeMSRP_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeMSRP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param TaxCode
      @param RateCode
      @param ds
   */  
export interface ChangeManualTaxCalc_input{
      /**  Quote Number.  */  
   QuoteNum:number,
      /**  Quote line number.  */  
   QuoteLine:number,
      /**  Tax Code  */  
   TaxCode:string,
      /**  Rate code  */  
   RateCode:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeManualTaxCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param tableName
   */  
export interface ChangeMiscAmt_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  name of table being passed in  */  
   tableName:string,
}

export interface ChangeMiscAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param tableName
   */  
export interface ChangeMiscPercent_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  name of table being passed in  */  
   tableName:string,
}

export interface ChangeMiscPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param tableName
      @param ds
   */  
export interface ChangeMiscellanousChargeType_input{
      /**  The name of the table  */  
   tableName:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeMiscellanousChargeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOrderQty_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeOrderQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOverrideDiscPriceList_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeOverrideDiscPriceList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param partNum
      @param lIsPhantom
      @param lIsSalesKit
      @param uomCode
      @param rowType
      @param SysRowID
      @param salesKitView
      @param removeKitComponents
      @param suppressUserPrompts
      @param runChkPrePartInfo
      @param getPartXRefInfo
      @param checkChangeKitParent
      @param ds
   */  
export interface ChangePartNumMaster_input{
      /**  proposed PartNum  */  
   partNum:string,
      /**  bool which identifies whether this is a phantom part.  set in 'getPartXRefInfo' logic  */  
   lIsPhantom:boolean,
      /**  bool which identifies whether this is a saleskit part.  set in 'getPartXRefInfo' logic  */  
   lIsSalesKit:boolean,
      /**  associated uomCode for this part.  maybe overwritten in chkPartXRefInfo  */  
   uomCode:string,
      /**  part Type for this row  */  
   rowType:string,
      /**  sysRowID for current row  */  
   SysRowID:string,
      /**  flag to identify whether this OrderDtl record is from salesKitView (or OrderDtlView)  */  
   salesKitView:boolean,
      /**  flag (set by user unless suppressUserPrompts is true) to ok removing kit components if kit parent changes  */  
   removeKitComponents:boolean,
      /**  flag to determine is user wants to be able to respond to messages and return to UI  */  
   suppressUserPrompts:boolean,
      /**  flag to determine whether the logic in runChkPrePartInfo is run  */  
   runChkPrePartInfo:boolean,
      /**  flag to determine whether a particular part of validation logic is run  */  
   getPartXRefInfo:boolean,
      /**  flag to determine whether a particular part of validation logic is run  */  
   checkChangeKitParent:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangePartNumMaster_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   lIsPhantom:boolean,
   lIsSalesKit:boolean,
   uomCode:string,
   vMessage:string,
   vPMessage:string,
   vBMessage:string,
   vSubAvail:boolean,
   vMsgType:string,
   cDeleteComponentsMessage:string,
   multipleMatch:boolean,
   promptToExplodeBOM:boolean,
   explodeBOMerrMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param lSubstitutePartsExist
      @param uomCode
   */  
export interface ChangePartNum_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  Flag to indicate if a substitute part exists  */  
   lSubstitutePartsExist:boolean,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePartRev_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangePartRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param prodCode
   */  
export interface ChangeProdCode_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  product group  */  
   prodCode:string,
}

export interface ChangeProdCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePromotionalPrice_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangePromotionalPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param pcCustID
      @param ds
   */  
export interface ChangeQuoteCntCustID_input{
      /**  Proposed Customer ID  */  
   pcCustID:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeQuoteCntCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteCoPartPartNum_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeQuoteCoPartPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteHedOTSCountryNum_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeQuoteHedOTSCountryNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuoteHedUseOTS_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeQuoteHedUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSellingExpQty_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeSellingExpQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param iShipToCustID
      @param ds
   */  
export interface ChangeShipToCustID_input{
      /**  Ship To Customer ID  */  
   iShipToCustID:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param markupId
      @param quoteNum
      @param quoteLine
      @param qtyNum
      @param ds
   */  
export interface ChangeStandardPct_input{
      /**  Standard Percent Markup Id  */  
   markupId:string,
      /**  Quote Number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Quote Quantity Number  */  
   qtyNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeStandardPct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param FromTable
      @param ipNewCode
   */  
export interface ChangeTaxRegionCode_input{
   ds:Erp_Tablesets_QuoteTableset[],
   FromTable:string,
   ipNewCode:string,
}

export interface ChangeTaxRegionCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   promptTaxRegionCodeMsg:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUseOTMF_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ChangeUseOTMF_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
   */  
export interface CheckBOMErrors_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  QuoteLine, 0 for all lines, otherwise only looks a specific line  */  
   quoteLine:number,
}

export interface CheckBOMErrors_output{
parameters : {
      /**  output parameters  */  
   errorList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckCustomerCreditLimit_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CheckCustomerCreditLimit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   cCreditLimitMessage:string,
}
}

   /** Required : 
      @param relatedToTable
      @param relatedSysRowID
   */  
export interface CheckIfConfigured_input{
   relatedToTable:string,
   relatedSysRowID:string,
}

export interface CheckIfConfigured_output{
parameters : {
      /**  output parameters  */  
   isConfigured:boolean,
   groupSeq:number,
}
}

   /** Required : 
      @param ipProjectID
      @param ipPhaseID
   */  
export interface CheckPhaseID_input{
      /**  Project ID  */  
   ipProjectID:string,
      /**  Phase ID  */  
   ipPhaseID:string,
}

export interface CheckPhaseID_output{
parameters : {
      /**  output parameters  */  
   opProjMsg:string,
}
}

   /** Required : 
      @param xPartNum
      @param custNum
      @param partNum
   */  
export interface CheckPreCustPartInfo_input{
      /**  The new Customenr Part Number  */  
   xPartNum:string,
      /**  The current QuoteHed.CustNum  */  
   custNum:number,
      /**  The new Part Num for this Customer Part  */  
   partNum:string,
}

export interface CheckPreCustPartInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param fieldName
      @param partNum
   */  
export interface CheckPrePartInfo_input{
      /**  The current QuoteHed.QuoteNum field  */  
   quoteNum:number,
      /**  The current QuoteDtl.QuoteLine field  */  
   quoteLine:number,
      /**  The name of the field you are leaving  */  
   fieldName:string,
      /**  The new PartNum if a substitute part is found, partNum will be the substitute part  */  
   partNum:string,
}

export interface CheckPrePartInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   vMessage:string,
   vBMessage:string,
   vPMessage:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param ipProposedPartNum
      @param ds
   */  
export interface CheckPreQuoteCoPartInfo_input{
      /**  The new proposed QuoteCoPart.CoPartNum value  */  
   ipProposedPartNum:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CheckPreQuoteCoPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param ipProjectID
   */  
export interface CheckProjectID_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  Project ID  */  
   ipProjectID:string,
}

export interface CheckProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   ipProjectID:string,
   opProjMsg:string,
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param ipContractID
   */  
export interface CheckQuoteDtlContractID_input{
   QuoteNum:number,
   QuoteLine:number,
      /**  Contract ID to return  */  
   ipContractID:string,
}

export interface CheckQuoteDtlContractID_output{
parameters : {
      /**  output parameters  */  
   ipContractID:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckQuoteHedChangesBeforeUpdate_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CheckQuoteHedChangesBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   propagateChangesMessage:string,
   fieldsToPropagate:string,
}
}

   /** Required : 
      @param quoteNum
   */  
export interface CheckQuoteNum_input{
      /**  Quote Number  */  
   quoteNum:number,
}

export interface CheckQuoteNum_output{
}

   /** Required : 
      @param ipquoteNum
   */  
export interface CheckQuoteSecurity_input{
      /**  The current QuoteHed.QuoteNum field  */  
   ipquoteNum:number,
}

export interface CheckQuoteSecurity_output{
}

   /** Required : 
      @param ipRateGrpCode
      @param ds
   */  
export interface CheckRateGrpCode_input{
      /**  Currency Rate Group Code  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CheckRateGrpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface CheckSpecificPartRevIsApproved_input{
   partNum:string,
   revisionNum:string,
   altMethod:string,
}

export interface CheckSpecificPartRevIsApproved_output{
   returnObj:boolean,
}

   /** Required : 
      @param quoteNum
      @param ds
   */  
export interface ClearQuoteDtlDealerData_input{
      /**  The quote number  */  
   quoteNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ClearQuoteDtlDealerData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipAsmSeq
   */  
export interface CollapsePhantom_input{
   ipQuoteNum:number,
   ipQuoteLine:number,
   ipAsmSeq:number,
}

export interface CollapsePhantom_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

export interface CompanyTaxConnectStatus_output{
   returnObj:boolean,
}

   /** Required : 
      @param QuoteDtlSysRowID
   */  
export interface ConfigurationChangePart_input{
      /**  QuoteDtl SysRowID  */  
   QuoteDtlSysRowID:string,
}

export interface ConfigurationChangePart_output{
}

   /** Required : 
      @param quoteDtlSysRowID
      @param commitValues
      @param currencySwitch
   */  
export interface ConfigurationChangeUnitPrice_input{
      /**  QuoteDtl SysRowID  */  
   quoteDtlSysRowID:string,
      /**  True to indicate if the changes should be committed to the DB. False if the logic only needs to compare the entity before and after the changes without commit them.  */  
   commitValues:boolean,
      /**  Flag to indicate which currency was affected by the Document Rule, true for Base Currency and false for Document Currency.  */  
   currencySwitch:boolean,
}

export interface ConfigurationChangeUnitPrice_output{
}

   /** Required : 
      @param QuoteDtlSysRowID
   */  
export interface ConfigurationRefreshQty_input{
      /**  QuoteDtl SysRowID  */  
   QuoteDtlSysRowID:string,
}

export interface ConfigurationRefreshQty_output{
}

   /** Required : 
      @param targetQuoteNum
      @param sourceQuoteLines
      @param mtlCosts
      @param opStds
      @param ds
   */  
export interface CopyLines_input{
      /**  The Quote to write the lines to  */  
   targetQuoteNum:number,
      /**  A delimited list of quote lines to be copied.  Format - QuoteNum tick QuoteLine tilde QuoteNum tick QuoteLine  */  
   sourceQuoteLines:string,
      /**  Indicates if Material/Operation Costs should be refreshed  */  
   mtlCosts:boolean,
      /**  Indicates if Operation Standards should be refreshed  */  
   opStds:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CopyLines_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param otsDS
      @param recalculateDiscount
      @param ds
   */  
export interface CreateOrderFromQuoteSaveOTS_input{
   otsDS:Erp_Tablesets_SaveQuoteOTSParamsTableset[],
      /**  Recalculate discount percent  */  
   recalculateDiscount:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CreateOrderFromQuoteSaveOTS_output{
parameters : {
      /**  output parameters  */  
   orderNum:number,
   newOrderMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param recalculateDiscount
      @param ds
   */  
export interface CreateOrderFromQuote_input{
      /**  Recalculate discount percent  */  
   recalculateDiscount:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CreateOrderFromQuote_output{
parameters : {
      /**  output parameters  */  
   orderNum:number,
   newOrderMessage:string,
   warningMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param ds1
   */  
export interface CreateOrderSaveOTS_input{
   ds:Erp_Tablesets_SaveQuoteOTSParamsTableset[],
   ds1:Erp_Tablesets_QuoteTableset[],
}

export interface CreateOrderSaveOTS_output{
parameters : {
      /**  output parameters  */  
   ds1:Erp_Tablesets_QuoteTableset[],
   orderNum:number,
}
}

   /** Required : 
      @param ds
   */  
export interface CreateOrder_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CreateOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   orderNum:number,
   warningMessage:string,
}
}

   /** Required : 
      @param quoteNum
      @param custNum
      @param perConID
      @param ds
   */  
export interface CreateQuoteCntNoCustCnt_input{
   quoteNum:number,
   custNum:number,
   perConID:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CreateQuoteCntNoCustCnt_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param iQuoteNum
      @param ds
   */  
export interface CreateQuoteDtlComplements_input{
      /**  The Quote Number  */  
   iQuoteNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface CreateQuoteDtlComplements_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
   */  
export interface DefaultOrderFields_input{
      /**  Quote Number  */  
   quoteNum:number,
}

export interface DefaultOrderFields_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
parameters : {
      /**  output parameters  */  
   creditMessage:string,
}
}

   /** Required : 
      @param quoteNum
   */  
export interface DeleteByID_input{
   quoteNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param sourceQuote
      @param sourceLines
      @param mtlCosts
      @param opStds
   */  
export interface DuplicateQuote_input{
      /**  The Quote to duplicate  */  
   sourceQuote:number,
      /**  List of lines from the source Quote to be copied. If blank
            all lines will be copied Format:QuoteLine~QuoteLine  */  
   sourceLines:string,
      /**  Indicates if Material/Operation Costs should be refreshed  */  
   mtlCosts:boolean,
      /**  Indicates if Operation Standards should be refreshed  */  
   opStds:boolean,
}

export interface DuplicateQuote_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param ds
      @param ds1
      @param quoteNum
   */  
export interface ETCAfterAddressValidationOTS_input{
   ds:Erp_Tablesets_QuoteTableset[],
   ds1:Erp_Tablesets_ETCAddrValidationTableset[],
      /**  QuoteHed.QuoteNum  */  
   quoteNum:number,
}

export interface ETCAfterAddressValidationOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
   */  
export interface ETCValidateAddress_input{
      /**  QuoteHed.QuoteNum  */  
   quoteNum:number,
      /**  QuoteDtl.QuoteLine  */  
   quoteLine:number,
}

export interface ETCValidateAddress_output{
   returnObj:Erp_Tablesets_ETCAddrValidationTableset[],
parameters : {
      /**  output parameters  */  
   statusFlag:boolean,
   errorFlag:boolean,
   errorMsg:string,
}
}

export interface Erp_Tablesets_ETCAddrValidationTableset{
   ETCAddress:Erp_Tablesets_ETCAddressRow[],
   ETCMessage:Erp_Tablesets_ETCMessageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ETCAddressRow{
      /**  Company  */  
   Company:string,
      /**  City name  */  
   City:string,
      /**  Country name  */  
   Country:string,
      /**  Address line 1  */  
   Line1:string,
      /**  Address line 2  */  
   Line2:string,
      /**  Address line 3  */  
   Line3:string,
      /**  Postal or ZIP code  */  
   PostalCode:string,
      /**  State or province name  */  
   Region:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  */  
   UpdateAddr:boolean,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  */  
   TransactionID:string,
      /**  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  */  
   UpdateAllowed:boolean,
      /**  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  */  
   RequestID:string,
      /**  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  */  
   AddressCode:string,
      /**  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  */  
   AddressType:string,
      /**  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  */  
   CarrierRoute:string,
      /**  City name  */  
   ValidCity:string,
      /**  Country name  */  
   ValidCountry:string,
      /**  County name  */  
   County:string,
      /**  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  */  
   FipsCode:string,
      /**  Line one of the valid address returned by the tax integration.  */  
   ValidLine1:string,
      /**  Line two of the valid address returned by the tax integration.  */  
   ValidLine2:string,
      /**  Line three of the valid address returned by the tax integration.  */  
   ValidLine3:string,
      /**  Line four of the valid address returned by the tax integration.  */  
   ValidLine4:string,
      /**  Postal code returned by the tax integration.  */  
   ValidPostalCode:string,
      /**  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  */  
   PostNet:string,
      /**  State or province name or abbreviation returned by the tax integration.  */  
   ValidRegion:string,
      /**  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   ResultCode:string,
      /**  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  */  
   ResultSeq:number,
      /**  Carrier Route description  */  
   CarrierRouteDesc:string,
      /**  Address type description  */  
   AddressTypeDesc:string,
   OTSCountry:string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  */  
   ACWPercentage:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ETCMessageRow{
      /**  Company  */  
   Company:string,
   Details:string,
      /**  URL to help page for this message  */  
   Helplink:string,
      /**  Gets the name of the message  */  
   Name:string,
      /**  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  */  
   RefersTo:string,
      /**  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   Severity:string,
      /**  source of the message  */  
   Source:string,
      /**  concise summary of the message  */  
   Summary:string,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  */  
   TransactionID:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  Programitically assigned.  */  
   RequestID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HedTaxSumRow{
   Company:string,
      /**  Currency display switch  */  
   CurrencySwitch:boolean,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  Document display symbol  */  
   DocDisplaySymbol:string,
      /**  Document reportable amount.  */  
   DocReportableAmt:number,
      /**  Document taxable amount.  */  
   DocTaxableAmt:number,
      /**  Document tax amount.  */  
   DocTaxAmt:number,
      /**  Order or Quote number this tax summary relates to.  */  
   HedNum:number,
      /**  Tax percent  */  
   Percent:number,
      /**  Reportable amount  */  
   ReportableAmt:number,
      /**  Taxable amount  */  
   TaxableAmt:number,
      /**  Tax amount  */  
   TaxAmt:number,
      /**  Tax code  */  
   TaxCode:string,
      /**  Sales Tax description  */  
   TaxDescription:string,
   GroupID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   Rpt1ReportableAmt:number,
   Rpt2ReportableAmt:number,
   Rpt3ReportableAmt:number,
   Rpt1TaxableAmt:number,
   Rpt2TaxableAmt:number,
   Rpt3TaxableAmt:number,
   Rpt1TaxAmt:number,
   Rpt2TaxAmt:number,
   Rpt3TaxAmt:number,
      /**  Rate Code on the Header Tax Summary  */  
   RateCode:string,
      /**  Invoice Number of allocated Deposits  */  
   AllocDepInvcNum:number,
      /**  Rate Code Description on the Header Tax Summary  */  
   RateCodeDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartSubsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Part number that this substitute Part is for.  */  
   PartNum:string,
      /**  Substitute Part  */  
   SubPart:string,
      /**  Indicates the record type. "S" = Substitute, "C" = Compliment  */  
   RecType:string,
      /**  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  */  
   SubType:string,
      /**   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  */  
   QtyPer:number,
      /**  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  */  
   SalesUM:string,
      /**  Optional Comment  */  
   Comment:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DefaultSub:boolean,
      /**  Price for the Suggested Quantity  */  
   Price:number,
      /**  Suggested Quantity  */  
   SuggestedQty:number,
      /**  Selected Row  */  
   Selected:boolean,
      /**  Suggested Quantity for Order Qty in Quote Detail  */  
   SugOrderQty:number,
   BitFlag:number,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   SubPartSellingFactor:number,
   SubPartTrackSerialNum:boolean,
   SubPartTrackDimension:boolean,
   SubPartPartDescription:string,
   SubPartIUM:string,
   SubPartSalesUM:string,
   SubPartTrackLots:boolean,
   SubPartPricePerCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QSalesRPRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The quote that this record is linked to.  */  
   QuoteNum:number,
      /**  Identifies the Sales Rep linked to the Quote.  */  
   SalesRepCode:string,
      /**  The Sales Reps Name from the SalesRep table  */  
   Name:string,
      /**  Identifies the primary sales rep on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  */  
   PrimeRep:boolean,
      /**  Establishes the defaults sales rep commission rates. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate:number,
      /**  Split percent is used to calculate the "commissionable"  dollar  amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit:number,
      /**  Link to the RoleCD Table where Roles are defined.  */  
   RoleCode:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OfficePhone:string,
   HomePhone:string,
   ReportsTo:string,
   EmailAddress:string,
   Fax:string,
   MobilePhone:string,
   SalesRepTitle:string,
   BitFlag:number,
   QuoteNumCurrencyCode:string,
   RoleCodeRoleDescription:string,
   SalesRepCodePerConID:number,
   SalesRepCodeName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QtQtyMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number that this record is linked to.  */  
   QuoteNum:number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   QuoteLine:number,
      /**  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  */  
   QtyNum:number,
      /**  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DocMiscAmt:number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   FreqCode:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  Reserved for future use  */  
   InMiscAmt:number,
      /**  Reserved for future use  */  
   DocInMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt1InMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt2InMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt3InMiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from QuoteHead  */  
   CurrSymbol:string,
      /**  CurrencyCode.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DspMiscAmt:number,
      /**  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DocDspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt1DspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt2DspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt3DspMiscAmt:number,
   BitFlag:number,
   MiscChrgDescription:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QtmmkupRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QuoteHead.QuoteNum that this record is linked to.  */  
   QuoteNum:number,
      /**  The QuoteDtl.QuoteLine to which the markup is related to.  */  
   QuoteLine:number,
      /**  the specific QuoteQty record that this markup is related to.  */  
   QtyNum:number,
      /**  Descriptive Code assigned by the user to uniquely identify the Part Class master record. This is the unique identifier for Qtmmkup.  */  
   ClassCode:string,
      /**  Material cost Markup Percent  */  
   MaterialMarkUp:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if Markup is used by QuoteMtl  */  
   Used:boolean,
   BitFlag:number,
   ClassCodeInactive:boolean,
   ClassCodeDescription:string,
   QtyNumMiscCostDesc:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number. This Quote Contact is linked to this QuoteHed  */  
   QuoteNum:number,
      /**  The unique internal number assigned to the customer for which the contact is related to.  */  
   CustNum:number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  */  
   ShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   ConNum:number,
      /**  Name of contact.  */  
   Name:string,
      /**  Primary contact for this quote.  */  
   PrimeContact:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PerConID  */  
   PerConID:number,
      /**  CustCnt.Func  */  
   Func:string,
      /**  CustCnt.PhoneNum  */  
   PhoneNum:string,
      /**  CustCnt.Fax  */  
   Fax:string,
      /**  CustCnt.EmailAddress  */  
   EmailAddress:string,
   PerConName:string,
   BitFlag:number,
   ConNumName:string,
   ConNumMiddleName:string,
   ConNumPhoneNum:string,
   ConNumFirstName:string,
   ConNumLastName:string,
   ConNumCorpName:string,
   ConNumFaxNum:string,
   CustNumCustID:string,
   CustNumBTName:string,
   CustNumName:string,
   QuoteNumCurrencyCode:string,
   ShipToNumName:string,
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteCoPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  */  
   CoPartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  */  
   CoRevisionNum:string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   PartsPerOp:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   LbrCostBase:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   MtlCostBase:number,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   IUM:string,
      /**  If true, MRP will not generate change suggestions for the co-part  */  
   PreventSugg:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   PartMasterPart:boolean,
   EnablePreventSugg:boolean,
   ProcessMode:string,
   BitFlag:number,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteComRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Quote that this QuoteCom is related to.  */  
   QuoteNum:number,
      /**  The unique key for the CRMComp Master table.  */  
   CompNum:number,
      /**  Name  */  
   Name:string,
      /**  Identifies the primary Competitor on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  */  
   PrimeComp:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CRMComp  */  
   FaxNum:string,
      /**  CRMCall.PhoneNum  */  
   PhoneNum:string,
      /**  CRMCall.EmailAddress  */  
   EmailAddress:string,
      /**  CRMCall.CompURL  */  
   CompURL:string,
   BitFlag:number,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteCustTrkRow{
      /**  from QuoteHed.QuoteNum  */  
   QuoteNum:number,
      /**  from QuoteHed.Quoted  */  
   Quoted:boolean,
      /**  from QuoteHed.Expired  */  
   Expired:boolean,
      /**  from QuoteHed.ExpirationDate  */  
   ExpirationDate:string,
      /**  from QuoteHed.Company  */  
   Company:string,
      /**  form QuoteHed.CustomerCustID  */  
   CustomerCustID:string,
      /**  from QuoteHed.CustomeName  */  
   CustomerName:string,
      /**  from QuoteDtl.PartNum  */  
   PartNum:string,
      /**  from QuoteDtl.LineDesc  */  
   LineDesc:string,
      /**  from QuoteHed.CurrentStage  */  
   CurrentStage:string,
      /**  from QuoteHed.EntryDate  */  
   EntryDate:string,
      /**  from QuoteHed.DueDate  */  
   DueDate:string,
      /**  from QuoteHed.MktgCampaignID  */  
   MktgCampaignID:string,
      /**  from QuoteDlt.DocExpectedRevenue  */  
   DocExpectedRevenue:number,
      /**  from QuoteDtl.ExpectedRevenue  */  
   ExpectedRevenue:number,
      /**  from QuoteHed.MktgEvntSeq  */  
   MktgEvntSeq:number,
      /**  from QuoteHed.ShipToNum  */  
   ShipToNum:string,
      /**  from QuoteHed.PrcConNum  */  
   PrcConNum:number,
      /**  from QuoteDtl.QuoteLine  */  
   QuoteLine:number,
      /**  from QuoteDtl.TerritoryID  */  
   TerritoryID:string,
      /**  from QuoteDtl.ProdCode  */  
   ProdCode:string,
      /**  from QuoteDtl.ProdCodeDescription  */  
   ProdCodeDescription:string,
      /**  from QuoteHed.CustNum  */  
   CustNum:number,
      /**  from QuoteHed.ShipConNum  */  
   ShipConNum:number,
      /**  from QuoteHed.Reference  */  
   Reference:string,
      /**  from QuoteHed.CurrentStageDesc  */  
   CurrentStageDesc:string,
      /**  from QuoteDtl.RevisionNum  */  
   RevisionNum:string,
      /**  from QuoteDtl.xPartNum  */  
   XPartNum:string,
      /**  from QuoteDtl.XRevisionNum  */  
   XRevisionNum:string,
      /**  Bill to customer number  */  
   BTCustNum:number,
      /**  Bill to customer ID  */  
   BTCustID:string,
      /**  Bill to customer name.  */  
   BTCustomerName:string,
      /**  Bill to address list  */  
   BTAddressList:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteCustTrkTableset{
   QuoteCustTrk:Erp_Tablesets_QuoteCustTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuoteDtlAttchRow{
   Company:string,
   QuoteNum:number,
   QuoteLine:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteDtlAttrValueSetRow{
      /**  Company identifier.  */  
   Company:string,
      /**  Quote number to which this line attribute set record is associated with.  */  
   QuoteNum:number,
      /**  Quote number to which this line attribute set record is associated with.  */  
   QuoteLine:number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   AttributeValueSeq:number,
      /**  Dynamic Attribute Value Set ID for this receipt detail.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure).  */  
   OrderQty:number,
      /**  The quantity expected to be ordered. (In selling unit of measure).  */  
   SellingExpectedQty:number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  */  
   SellingExpectedUM:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
   QuantityToOrder:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Unit of measure for the NumberOfPieces.  */  
   DispNumberOfPiecesUOM:string,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   Ordered:boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   XPartNum:string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   LeadTime:string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   JobComment:string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   MfgDetail:boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   TaxCatID:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   CustNum:number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Quoted:boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Expired:boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   SellingExpectedQty:number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SellingExpectedUM:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   ConfidencePct:number,
      /**  The date this line was last updated  */  
   LastUpdate:string,
      /**  The last User Is that updated this Quote  */  
   LastDcdUserID:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   DocDiscount:number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   ExpectedRevenue:number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   DocExpectedRevenue:number,
      /**  The requested ship date for the sales order  */  
   ReqShipDate:string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   OrderQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingExpFactor:number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   MultiRel:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   SalesCatID:string,
      /**  Replicated from QuoteHed to easier sorting  */  
   TerritoryID:string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   CreatedFrom:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This is the unit price based on the expected quantity.  */  
   ExpUnitPrice:number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   DocExpUnitPrice:number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   ExpPricePerCode:string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   MiscQtyNum:number,
      /**  The Quote Line has been Engineered.  */  
   Engineer:boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   ReadyToQuote:boolean,
      /**  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  */  
   KitPricing:string,
      /**  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  */  
   KitQtyPer:number,
      /**  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  Project ID of linked project.  Must exist on the Project table. Can be blank.  */  
   ProjectID:string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  To indicate whether or not the line is make direct  */  
   MakeDirect:boolean,
      /**  Must exist on ProjPhase table if entered  */  
   PhaseID:string,
      /**   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  */  
   KitsLoaded:boolean,
      /**  Non-blank value prevents taxes from being calculated for this line item  */  
   TaxExempt:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the quote line, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Reserved for future use  */  
   InDiscount:number,
      /**  Reserved for future use  */  
   DocInDiscount:number,
      /**  Reserved for future use  */  
   InExpectedRevenue:number,
      /**  Reserved for future use  */  
   DocInExpectedRevenue:number,
      /**  Reserved for future use  */  
   InListPrice:number,
      /**  Reserved for future use  */  
   DocInListPrice:number,
      /**  Reserved for future use  */  
   InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   DocInOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExpUnitPrice:number,
      /**  Reserved for future use  */  
   DocInExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InDiscount:number,
      /**  Reserved for future use  */  
   Rpt2InDiscount:number,
      /**  Reserved for future use  */  
   Rpt3InDiscount:number,
      /**  Reserved for future use  */  
   Rpt1InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt2InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt3InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt1InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt2InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt3InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InListPrice:number,
      /**  Reserved for future use  */  
   Rpt2InListPrice:number,
      /**  Reserved for future use  */  
   Rpt3InListPrice:number,
      /**  Reserved for future use  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExtPriceDtl:number,
      /**  Reserved for future use  */  
   DocInExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt1InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt2InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt3InExtPriceDtl:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   WorstCsPct:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   BestCsPct:number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   WorstCsRevenue:number,
      /**  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   DocWorstCsRevenue:number,
   Rpt1WorstCsRevenue:number,
   Rpt2WorstCsRevenue:number,
   Rpt3WorstCsRevenue:number,
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   BestCsRevenue:number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   DocBestCsRevenue:number,
   Rpt1BestCsRevenue:number,
   Rpt2BestCsRevenue:number,
   Rpt3BestCsRevenue:number,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
   DiscBreakListCode:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscListPrice:number,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
   OverrideDiscPriceList:boolean,
      /**  Demand Contract Line  */  
   DemandContractLine:number,
      /**  Demand Header sequence number to which this record is related.  */  
   DemandHedSeq:number,
      /**  Demand Detail Sequence number to which this record is related.  */  
   DemandDtlSeq:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  Indicates if this quote line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Indicates if the price of the quote line can be changed.  */  
   LockPrice:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates that the line item was closed before any shipments were made against it.  */  
   VoidLine:boolean,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  EstimateGUID  */  
   EstimateGUID:string,
      /**  RFQCurrBaseEst  */  
   RFQCurrBaseEst:string,
      /**  RFQTemplate  */  
   RFQTemplate:string,
      /**  CreateEstimate  */  
   CreateEstimate:boolean,
      /**  Rating  */  
   Rating:string,
      /**  EstimateUserID  */  
   EstimateUserID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   ProcessMode:string,
      /**  ECC Quote Number  */  
   ECCQuoteNum:string,
      /**  ECC Quote Line  */  
   ECCQuoteLine:number,
      /**  ECC Comment Ref  */  
   ECCCmmtRef:string,
      /**  ECCComment  */  
   ECCComment:string,
      /**  ContractID  */  
   ContractID:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   DocTax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt1Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt2Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt3Tax:number,
      /**  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  Indicates if no tax recalculation by the system is supposed to be done.  */  
   NoTaxRecalc:boolean,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   DocTotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt1TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt2TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt3TotalSATax:number,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  This field holds the id of this quote line in the External CRM  */  
   ExternalCRMQuoteLineID:string,
      /**  Type for returns: Blank, (C)redit or (S)tandard  */  
   ReturnLineType:string,
      /**  Base price before any price breaks and discounts  */  
   MSRP:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocMSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt1MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt2MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt3MSRP:number,
      /**  Distributor end customer price.  */  
   EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocEndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt1EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt2EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt3EndCustomerPrice:number,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Mark For ShipToNum  */  
   MFShipToNum:string,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Contact Name  */  
   OTMFName:string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   OTMFAddress1:string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   OTMFAddress2:string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   OTMFAddress3:string,
      /**  City portion of the One Time Mark For address.  */  
   OTMFCity:string,
      /**  The state or province portion of the One Time Mark For address.  */  
   OTMFState:string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   OTMFZIP:string,
      /**  One Time Mark For Contact Name  */  
   OTMFContact:string,
      /**  Fax number for the One Time Mark For.  */  
   OTMFFaxNum:string,
      /**  Phone number for the One Time Mark For  */  
   OTMFPhoneNum:string,
      /**  Country number for the One Time Mark For  */  
   OTMFCountryNum:number,
      /**  Promotional Price offered to Dealer and Distributors  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocPromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt1PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt2PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt3PromotionalPrice:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
   BaseExtPrice:number,
   BaseMiscAmt:number,
   BasePotential:number,
      /**  If yes, then a new non-standard part was added with no description and validation needs to be run again  */  
   CheckPartDescription:boolean,
      /**  PLM Flag  */  
   CodePLM:boolean,
      /**  Valid values are "win" "lose" "next" "next" is the default  */  
   Conclusion:string,
   ConfigType:string,
      /**  Indicates whether the part is/can be configured  */  
   Configured:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   CurrSymbol:string,
      /**  Date that the quoter considered the quoting process for this quote complete.  */  
   DateQuoted:string,
      /**  Indicates if the discount fields should be disabled for the current quote line detail.  */  
   DisableDiscounts:boolean,
      /**  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDspDiscount:number,
      /**  Display Document unit price based on the expected quantity.  */  
   DocDspExpUnitPrice:number,
   DocExtPrice:number,
   DocMiscAmt:number,
   DocOrderUnitPrice:number,
   DocPotential:number,
   DocTotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   DocTotalQuote:number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   DocTotalWHTax:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DspDiscount:number,
      /**  Used to displayed UOM for expected quantity for detail line  */  
   DspExpectedUM:string,
   EnableRenewalNbr:boolean,
      /**  The date when this quote expires.  */  
   ExpirationDate:string,
      /**  Indicates whether the part has at least one Complement  */  
   HasComplement:boolean,
   HasCoParts:boolean,
      /**  Indicates if this Quote line has an associated credit memo (only for dealer portal)  */  
   HasCreditMemo:boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   HasDowngrade:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasSubstitute:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasUpgrade:boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   KitChangeParms:boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  The description for Kit Flag. "P" = Parent, "C" = Component.  */  
   KitFlagDescription:string,
   KitOrderQtyUOM:string,
   LineStatus:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
   OrderUM:string,
   OrderUnitPrice:number,
      /**  If yes, the line will be copied to the Order  */  
   OrderWorthy:boolean,
      /**  Internal flag to identify if the Part is an Inventory Part.  */  
   PartExists:boolean,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
   QtyBearing:boolean,
   QuantityToOrder:number,
      /**  Indicates whether to Refresh the QuoteQty table  */  
   RefreshQty:boolean,
      /**  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  */  
   RemoveManAdTax:boolean,
   Rpt1BaseExtPrice:number,
   Rpt1BaseMiscAmt:number,
   Rpt1BasePotential:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1DspDiscount:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt1DspExpUnitPrice:number,
   Rpt1OrderUnitPrice:number,
   Rpt1TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   Rpt1TotalQuote:number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   Rpt1TotalWHTax:number,
   Rpt2BaseExtPrice:number,
   Rpt2BaseMiscAmt:number,
   Rpt2BasePotential:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2DspDiscount:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt2DspExpUnitPrice:number,
   Rpt2OrderUnitPrice:number,
   Rpt2TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   Rpt2TotalQuote:number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   Rpt2TotalWHTax:number,
   Rpt3BaseExtPrice:number,
   Rpt3BaseMiscAmt:number,
   Rpt3BasePotential:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3DspDiscount:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt3DspExpUnitPrice:number,
   Rpt3OrderUnitPrice:number,
   Rpt3TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   Rpt3TotalQuote:number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   Rpt3TotalWHTax:number,
      /**  Selected row  */  
   Selected:boolean,
   ShipByDate:string,
   TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   TotalQuote:number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   TotalWHTax:number,
      /**   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  */  
   UpdateReq:boolean,
      /**  Indicates that the Quote should be used as the BOM when creating a job for the linked order  */  
   UseQuoteBOM:boolean,
      /**  Delimited list of Available Price Lists  */  
   AvailPriceLists:string,
      /**  Display unit price based on the expected quantity.  */  
   DspExpUnitPrice:number,
   ECCLineCRQ:number,
      /**  Allow enable/disable for the Dynamic Attributes button on a Quote Line  */  
   EnableDynAttrButton:boolean,
      /**  Flag indicating whether to enable CodePLM or not  */  
   EnablePLM:boolean,
   MarkForAddressFormatted:string,
   InventoryAttributeSetID:number,
      /**  The amount of discount for display  */  
   LessDiscount:number,
      /**  The amount of discount for display in Doc currency  */  
   DocLessDiscount:number,
      /**  The amount of discount for display in reporting currency  */  
   Rpt1LessDiscount:number,
      /**  The amount of discount for display in reporting currency  */  
   Rpt2LessDiscount:number,
      /**  The amount of discount for display in reporting currency  */  
   Rpt3LessDiscount:number,
      /**   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  */  
   AllowTaxCodeUpd:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   DiscBreakListCodeListDescription:string,
   DiscBreakListCodeEndDate:string,
   DiscBreakListCodeStartDate:string,
   MFShipToNumInactive:boolean,
   OTMFCountryDescription:string,
   PartNumDefaultAttributeSetID:number,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PriceBreakListDescription:string,
   PriceGroupDescription:string,
   ProdCodeDescription:string,
   QuoteNumInPrice:boolean,
   QuoteNumCurrencyCode:string,
   SalesCatIDDescription:string,
   TaxCatIDDescription:string,
   TaxRegionDescription:string,
   TaxRegionTaxConnectCalc:boolean,
   TerritoryIDTerritoryDesc:string,
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteDtlTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote Number  */  
   QuoteNum:number,
      /**  Quote Line related to the Tax Record  */  
   QuoteLine:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an quote. When the sales tax field EcAquisition is checked then 2 quote tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   TaxableAmt:number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this quote. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  The user ID for the user who created this record.  */  
   CreatedBy:string,
      /**  The date and time of creating.  */  
   CreatedOn:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  A flat discount amount for the tax.  */  
   Discount:number,
      /**  A flat discount amount for the tax converted to the customers currency.  */  
   DocDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Tax Rate Date  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  Document display symbol  */  
   DocDisplaySymbol:string,
      /**  Currency switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
   BitFlag:number,
   RateCodeDescription:string,
   SalesTaxDescDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteHedAttchRow{
   Company:string,
   QuoteNum:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   QuoteNum:number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   CustNum:number,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   DueDate:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   Quoted:boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   DateQuoted:string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   ExpirationDate:string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   FollowUpDate:string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   Reference:string,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   Expired:boolean,
      /**  Full Description for CurrentStage field  */  
   CurrentStageDesc:string,
      /**  Link to the territory Id for this LOQ  */  
   TerritoryID:string,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Bill to customer id.  */  
   BTCustID:string,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  Bill to customer name.  */  
   BTCustomerName:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
   CustomerName:string,
   TerritoryTerritoryDesc:string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   ReasonType:string,
   CustomerCustID:string,
   CustomerBTName:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   ConfidencePct:number,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this record.  */  
   MktgEvntSeq:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   Ordered:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteHedListTableset{
   QuoteHedList:Erp_Tablesets_QuoteHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuoteHedMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number that this record is linked to.  */  
   QuoteNum:number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   QuoteLine:number,
      /**  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  */  
   QtyNum:number,
      /**  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DocMiscAmt:number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   FreqCode:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  Reserved for future use  */  
   InMiscAmt:number,
      /**  Reserved for future use  */  
   DocInMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt1InMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt2InMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt3InMiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from QuoteHedMsc  */  
   CurrSymbol:string,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DspMiscAmt:number,
      /**  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DocDspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt1DspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt2DspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt3DspMiscAmt:number,
   BitFlag:number,
   MiscCodeDescription:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   QuoteNum:number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   CustNum:number,
      /**  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  */  
   EntryDate:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Contains comments about the overall Quote. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   DueDate:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   Quoted:boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   DateQuoted:string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   ExpirationDate:string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   FollowUpDate:string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   Reference:string,
      /**   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**  Optional check off # 2.  */  
   CheckOff2:boolean,
      /**  Optional check off # 3.  */  
   CheckOff3:boolean,
      /**  Optional check off # 4.  */  
   CheckOff4:boolean,
      /**  Optional check off # 5.  */  
   CheckOff5:boolean,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   Expired:boolean,
      /**  System maintained flag - set to yes when the quote follow up alert has been sent.  */  
   FlwAlrtSnt:boolean,
      /**  System maintained flag - set to yes when the quote due date alert has been sent.  */  
   DueAlrtSnt:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  A = High, Z = Low  */  
   LeadRating:string,
      /**  Link to the territory Id for this LOQ  */  
   TerritoryID:string,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  */  
   ParentQuoteNum:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  The date this quote is expected to close.  */  
   ExpectedClose:string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   ReasonType:string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   ReasonCode:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   ConfidencePct:number,
      /**  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  */  
   DiscountPercent:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  This quote is no longer updatable.  */  
   QuoteClosed:boolean,
      /**  The date that the Quote was closed.  */  
   ClosedDate:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this record.  */  
   MktgEvntSeq:number,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   CallTypeCode:string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   TermsCode:string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   Ordered:boolean,
      /**  Indicates if order based discounting needs to be applied to the quote.  */  
   ApplyOrderBasedDisc:boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  The help desk case that created this quote.  */  
   HDCaseNum:number,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  */  
   LockRate:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  */  
   ReadyToCalc:boolean,
      /**  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   ExportRequested:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  */  
   QuoteAmt:number,
      /**  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   DocQuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1QuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2QuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3QuoteAmt:number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   WorstCsPct:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   BestCsPct:number,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  Demand Header sequence number to which this record is related.  */  
   DemandHeadSeq:number,
      /**  Defines if this document is marked as EDI Ready.  */  
   EDIReady:boolean,
      /**  Quote created from EDI interfaced module.  */  
   EDIQuote:boolean,
      /**  Updated from EDI module this type of document is created.  */  
   EDIAck:boolean,
      /**  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  */  
   OutboundQuoteDocCtr:number,
      /**  Date in which the related demand was last processed.  */  
   DemandProcessDate:string,
      /**  System Time when demand was last processed.  */  
   DemandProcessTime:number,
      /**  EDI Transaction Control Number  */  
   LastTCtrlNum:string,
      /**  EDI Batch Control Number  */  
   LastBatchNum:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalSATax:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalWHTax:number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalSATax:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalWHTax:number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalSATax:number,
      /**   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalWHTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalSATax:number,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalWHTax:number,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Freight charges will not be returned if 'yes'  */  
   DropShip:boolean,
      /**   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalSATax:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalTax:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalWHTax:number,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   ICPONum:number,
      /**  Indicates if this quote header is linked to an inter-company PO header.  */  
   Linked:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  */  
   NeedByDate:string,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   OTSCustSaved:boolean,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  */  
   RequestDate:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Indicates that the Quote item was closed before any shipments were made against it.  */  
   VoidQuote:boolean,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Total discount percent.  */  
   TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   TotalExpected:number,
   TotalGrossValue:number,
   TotalMiscAmt:number,
   TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   DocTotalBestCs:number,
   DocTotalDiscount:number,
      /**  Total discount percent.  */  
   DocTotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   DocTotalExpected:number,
   DocTotalGrossValue:number,
   DocTotalMiscAmt:number,
   DocTotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   DocTotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt1TotalBestCs:number,
   Rpt1TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt1TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt1TotalExpected:number,
   Rpt1TotalGrossValue:number,
   Rpt1TotalMiscAmt:number,
   Rpt1TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt1TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt2TotalBestCs:number,
   Rpt2TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt2TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt2TotalExpected:number,
   Rpt2TotalGrossValue:number,
   Rpt2TotalMiscAmt:number,
   Rpt2TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt2TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt3TotalBestCs:number,
   Rpt3TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt3TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt3TotalExpected:number,
   Rpt3TotalGrossValue:number,
   Rpt3TotalMiscAmt:number,
   Rpt3TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt3TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   TotalBestCs:number,
   TotalDiscount:number,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  LOQPrepressText  */  
   LOQPrepressText:string,
      /**  LOQNewPageOnQuoteLine  */  
   LOQNewPageOnQuoteLine:boolean,
      /**  LOQBookPCFinishing  */  
   LOQBookPCFinishing:boolean,
      /**  LOQBookPCPaper  */  
   LOQBookPCPaper:boolean,
      /**  LOQBookPCPress  */  
   LOQBookPCPress:boolean,
      /**  LOQBookPCPlates  */  
   LOQBookPCPlates:boolean,
      /**  LOQVariations  */  
   LOQVariations:boolean,
      /**  AEPLOQType  */  
   AEPLOQType:string,
      /**  LOQPrepressStyle  */  
   LOQPrepressStyle:string,
      /**  QuoteCSR  */  
   QuoteCSR:string,
      /**  DueHour  */  
   DueHour:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Quote was confirmed/rejected by ECC Web  */  
   ECCConfirmed:boolean,
      /**  Quote was confirmed/rejected by this ECC user  */  
   ECCConfirmedBy:string,
      /**  ECC quote message: RFQ or GQR  */  
   ECCMsgType:string,
      /**  Quote is ready to be approved by user via ECC web site.  */  
   ECCWebReady:boolean,
      /**  ECC Quote Number  */  
   ECCQuoteNum:string,
      /**  ECC Comment Reference Number  */  
   ECCCmmtRef:string,
      /**  ECCComment  */  
   ECCComment:string,
      /**  ECC Quote Status  */  
   ECCStatus:string,
      /**  ECC Expiration Date  */  
   ECCExpirationDate:string,
      /**  ECCCmmtRefSK  */  
   ECCCmmtRefSK:string,
      /**  This field defines if the Quote  is synchronized to an External CRM.  */  
   ExternalCRMQuote:boolean,
      /**  This field holds the  id of this quote in the External CRM  */  
   ExternalCRMQuoteID:string,
      /**  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  */  
   ExternalCRMOrderID:string,
      /**  Web Sales Rep ID  */  
   ECCSalesRepID:string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   DocTax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt1Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt2Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt3Tax:number,
      /**  HdrTaxNoUpdt  */  
   HdrTaxNoUpdt:boolean,
      /**  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSync:string,
      /**  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  */  
   ExternalCRMSyncRequired:boolean,
      /**  Total of claims credit lines  */  
   TotalClaimsCredit:number,
      /**  Total of claims credit lines in customer currency  */  
   DocTotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt1TotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt2TotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt3TotalClaimsCredit:number,
      /**  Total Quote claims credit Invoice Taxes.  */  
   TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in customer currency.  */  
   DocTotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt1TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt2TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt3TotalClaimsTax:number,
      /**  Total Quote claims credit Self Assessed Taxes.  */  
   TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   DocTotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt1TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt2TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt3TotalClaimsSATax:number,
      /**  Total Quote claims credit Withholding Taxes.  */  
   TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in customer currency.  */  
   DocTotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt1TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt2TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt3TotalClaimsWHTax:number,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
   AddrList:string,
   BaseCurrencyID:string,
      /**  Bill To Customer Name.  */  
   BTCustomerName:string,
      /**  Audit Log change description  */  
   ChangeDescription:string,
   CheckOffLabel1:string,
   CheckOffLabel2:string,
   CheckOffLabel3:string,
   CheckOffLabel4:string,
   CheckOffLabel5:string,
   Conclusion:string,
      /**  Primary Contact Name  */  
   ConName:string,
   CurrencySwitch:boolean,
      /**  Full Description of the CurrentStage field  */  
   CurrentStageDesc:string,
      /**  Value of the Customer.AllowOTS (customer allows one time shipment)  */  
   CustAllowOTS:boolean,
   CustOnCreditHold:boolean,
      /**  Number of days Quote has been open  */  
   DaysOpen:number,
      /**   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  */  
   DiscountPercentCalc:number,
      /**  Total tax in Doc currency. The sum of all the tax details for the quote.  */  
   DocTaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   DocTotalQuote:number,
      /**  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   dspBTCustID:string,
   EmailAddress:string,
      /**  Indicates if it's okay to enable OrderBased Pricing  */  
   EnableOrderBasedDisc:boolean,
      /**   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  */  
   ExpectedCsPct:number,
   FaxNum:string,
   FOB:string,
   FOBDescription:string,
      /**  Used by IU to disabled Currency Code  */  
   HasQuoteLines:boolean,
      /**  EqSyst.LogChanges  */  
   LogChanges:boolean,
      /**  Order Date  */  
   OrderDate:string,
   OrderDiscount:number,
   OrderPONum:string,
   OrderShipVia:string,
   OrderTerms:string,
   OTSSaved:boolean,
   OTSShipToNum:string,
   PhoneNum:string,
   PreventQQChange:boolean,
      /**  Label for ExchangeRate  */  
   RateLabel:string,
   Rpt1TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   Rpt1TotalQuote:number,
   Rpt2TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   Rpt2TotalQuote:number,
   Rpt3TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   Rpt3TotalQuote:number,
   SalesRepCode:string,
   SalesRepName:string,
   ShipByDate:string,
   ShipToAddrList:string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   TotalQuote:number,
      /**   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  */  
   WorseCsPctCalc:number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   BaseCurrSymbol:string,
      /**   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  */  
   BestCsPctCalc:number,
      /**  Bill To Address List.  */  
   BTAddressList:string,
      /**  Customer ID of the bill to customer.  */  
   BTCustID:string,
      /**  Indicates if the order contains any credit type line  */  
   HasCreditLines:boolean,
      /**  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  */  
   IsValidECC:boolean,
      /**  Flag indicating whether to enable CaseNum or not  */  
   EnableHDCaseNum:boolean,
      /**  Indicates if the quote can be updated  */  
   UpdateAllowed:boolean,
      /**  Formatted address  */  
   AddressFormatted:string,
      /**  Ship To Address formatted  */  
   ShipToAddressFormatted:string,
      /**  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  */  
   PromptTaxRegionCode:boolean,
      /**  Indicates a customer referenced on the quote is inactive.  */  
   InactiveCustomer:boolean,
      /**  Update primary contact on save of the quote header  */  
   UpdatePrimContact:boolean,
      /**  Flag indicating whether to enable Incoterm Location  */  
   EnableIncotermLocation:boolean,
   BitFlag:number,
   ActiveTaskTaskDescription:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyBaseCurr:boolean,
   CustomerAllowShipTo3:boolean,
   CustomerBTName:string,
   CustomerCustID:string,
   CustomerName:string,
   CustomerCheckDuplicatePO:boolean,
   HDCaseDescription:string,
   IncotermsDescription:string,
   LastTaskTaskDescription:string,
   MktgCpgnCampDescription:string,
   MktgEventEvntDescription:string,
   OTSCountryNumISOCode:string,
   OTSCountryNumDescription:string,
   OTSCountryNumEUMember:boolean,
   OTSTaxRegionCodeDescription:string,
   RateGrpDescription:string,
   ReasonDescription:string,
   ResponseCallTypeDesc:string,
   ShipToBTName:string,
   ShipToCustID:string,
   ShipToName:string,
   ShipToNumName:string,
   ShipToNumInactive:boolean,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
   ShipViaInactive:boolean,
   TaskSetTaskSetDescription:string,
   TaskSetWorkflowType:string,
   TaxRegionTaxConnectCalc:boolean,
   TaxRegionDescription:string,
   TermsDescription:string,
   TerritoryTerritoryDesc:string,
   XbSystCalcQuoteTax:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteHedTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote Number  */  
   QuoteNum:number,
      /**  Tax ID from Sales Tax  */  
   TaxCode:string,
      /**  Rate Code on the Header Tax Summary  */  
   RateCode:string,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Taxable Amount for this quote  */  
   TaxableAmt:number,
      /**  The reportable sales amount for this quote  */  
   ReportableAmt:number,
      /**  Calculated Tax Percent  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   DocTaxAmt:number,
      /**  Taxable Amount for this quote  */  
   DocTaxableAmt:number,
      /**  The reportable sales amount for this quote  */  
   DocReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  The user ID for the user who created this record.  */  
   CreatedBy:string,
      /**  The date and time of creating.  */  
   CreatedOn:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Tax for claims credit tax.  This tax should not be included with regular tax.  */  
   ClaimsTax:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  Currency switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  Document display symbol  */  
   DocDisplaySymbol:string,
   BitFlag:number,
   QuoteHedCurrencyCode:string,
   RateCodeDescription:string,
   SalesTaxDescDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number that this record is linked to.  */  
   QuoteNum:number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   QuoteLine:number,
      /**  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  */  
   QtyNum:number,
      /**  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DocMiscAmt:number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   FreqCode:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  Reserved for future use  */  
   InMiscAmt:number,
      /**  Reserved for future use  */  
   DocInMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt1InMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt2InMiscAmt:number,
      /**  Reserved for future use  */  
   Rpt3InMiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   CurrSymbol:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DspMiscAmt:number,
      /**  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   DocDspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt1DspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt2DspMiscAmt:number,
      /**  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  */  
   Rpt3DspMiscAmt:number,
   BitFlag:number,
   MiscCodeDescription:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteQtyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote # that this record is linked to.  */  
   QuoteNum:number,
      /**  The QuoteLine to which this QuoteQty record is related to.  */  
   QuoteLine:number,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  */  
   QtyNum:number,
      /**  Represents one of the requested Quote Quantities for the line item using QuoteQty.IUM.  */  
   OurQuantity:number,
      /**  Quoted unit price for the given quantity. This value is entered by the user.  */  
   UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed).
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteQty.Quantity by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   PricePerCode:string,
      /**  Material Bur Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   MtlBurMarkUp:number,
      /**  Material Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   MaterialMarkUp:number,
      /**  SubContract Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   SubcontractMarkUp:number,
      /**  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   LaborMarkUp:number,
      /**  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   BurdenMarkUp:number,
      /**  Miscellaneous Cost description.  */  
   MiscCostDesc:string,
      /**  Miscellaneous Cost amount that will be considered in the unit price calculations.  */  
   MiscCost:number,
      /**  Miscellaneous Cost Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  */  
   MiscCostMarkUp:number,
      /**  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  */  
   CommissionPct:number,
      /**  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values. Prices can be calculated either as a straight markup of cost ( Cost + (Cost *  x %)) or a percent of profit ( Cost / (100% -  x%).   PercentType "M" = straight markup, "P" = Profit Percent. Defaulted from referenced QMarkup, from EQSyst.PercentType if not blank, else default as "M".  */  
   PercentType:string,
      /**  Unit of Measure (how it is stocked).  Use the default Part.IUM if its a valid part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   IUM:string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Represents one of the requested Quote Quantities for the line item using QuoteQty.SUM.  */  
   SellingQuantity:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Unique identifier of this material markup. Defaults from its parent table Qmarkup.  */  
   MarkUpID:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Reserved for future use  */  
   InUnitPrice:number,
      /**  Reserved for future use  */  
   DocInUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt2InUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt3InUnitPrice:number,
      /**  PriceSource  */  
   PriceSource:string,
      /**  PricePerAdl1000  */  
   PricePerAdl1000:number,
      /**  TotalSellPrice  */  
   TotalSellPrice:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DocPricePerAdl1000  */  
   DocPricePerAdl1000:number,
      /**  DocTotalSellPrice  */  
   DocTotalSellPrice:number,
      /**  Indicates if the unit price for the qty break has been manually modified  */  
   UserChangedUnitPrice:boolean,
      /**  Worksheet field  */  
   CalcProfit:number,
      /**  CalcProfit Profit calculation  */  
   CalcProfitProfit:number,
      /**  Worksheet field  */  
   CalcUnitCost:number,
      /**  Worksheet field  */  
   CalcUnitPriceMarkup:number,
      /**  Worksheet field  */  
   CalcUnitPriceProfit:number,
      /**  Worksheet field  */  
   CalcUPCommMarkup:number,
      /**  Worksheet field  */  
   CalcUPCommProfit:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   CurrSymbol:string,
      /**  Flag to indicate when to disable/enable material markup field  */  
   DisableMtlMarkup:boolean,
      /**  External field for MaterialMarkup Markup calculations  */  
   MaterialMarkupM:number,
      /**  External field for MaterialMarkup Profit calculations  */  
   MaterialMarkupP:number,
      /**  Indicates if the record has a miscellaneous charge associated with it  */  
   MiscChrg:string,
      /**  Worksheet field  */  
   PriceBurMarkup:number,
      /**  Worksheet field  */  
   PriceBurProfit:number,
      /**  Worksheet field  */  
   PriceLbrMarkup:number,
      /**  Worksheet field  */  
   PriceLbrProfit:number,
      /**  Worksheet field  */  
   PriceMscChrgMarkup:number,
      /**  Worksheet field  */  
   PriceMscChrgProfit:number,
      /**  Worksheet field  */  
   PriceMtlBurMarkup:number,
      /**  Worksheet field  */  
   PriceMtlBurProfit:number,
      /**  Worksheet field  */  
   PriceMtlMarkup:number,
      /**  Worksheet field  */  
   PriceMtlProfit:number,
      /**  Integer value of the PricePerCode field (for calculations)  */  
   PricePerFactor:number,
      /**  Worksheet field  */  
   PriceSubMarkup:number,
      /**  Worksheet field  */  
   PriceSubProfit:number,
      /**  Worksheet field  */  
   PriceTotalCommMarkup:number,
      /**  Worksheet field  */  
   PriceTotalCommProfit:number,
      /**  Worksheet field  */  
   PriceTotalMarkup:number,
      /**  Worksheet field  */  
   PriceTotalProfit:number,
      /**  Worksheet field  */  
   QuotedMarkup:number,
      /**  Worksheet field  */  
   QuotedProfit:number,
      /**  If marked then the totals are not updated and a ?Roll up costs? is needed.  */  
   RollUpCostNeeded:boolean,
      /**  QuoteCst.TotalBurCost - Worksheet temp field  */  
   TotalBurCost:number,
      /**  Worksheet field  */  
   TotalCommission:number,
      /**  Total Commision Profit calculation  */  
   TotalCommProfit:number,
      /**  Worksheet field  */  
   TotalCost:number,
      /**  QuoteCst.TotalLbrCost - Worksheet temp field  */  
   TotalLbrCost:number,
      /**  Worksheet field  */  
   TotalMarkup:number,
      /**  QuoteCst.TotalMtlBurCost - Worksheet temp field  */  
   TotalMtlBurCost:number,
      /**  QuoteCst.TotalMtlCost - Worksheet temp field  */  
   TotalMtlCost:number,
      /**  QuoteCst.TotalProdBurHrs - Worksheet temp field  */  
   TotalProdBurHrs:number,
      /**  QuoteCst.TotalProdLbrHrs - Worksheet temp field  */  
   TotalProdLbrHrs:number,
      /**  Worksheet field  */  
   TotalProfit:number,
      /**  Worksheet field  */  
   TotalQuotedPrice:number,
      /**  QuoteCst.TotalSetupBurHrs - Worksheet temp field  */  
   TotalSetupBurHrs:number,
      /**  QuoteCst.TotalSetupLbrHrs - Worksheet temp field  */  
   TotalSetupLbrHrs:number,
      /**  QuoteCst.TotalSubCost - Worksheet temp field  */  
   TotalSubCost:number,
      /**  Worksheet Quoted Unit Price  */  
   WQUnitPrice:number,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  Worksheet field  */  
   CalcMarkup:number,
      /**  CalcMarkup Profit calculation  */  
   CalcMarkupProfit:number,
   BitFlag:number,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteTableset{
   QuoteHed:Erp_Tablesets_QuoteHedRow[],
   QuoteHedAttch:Erp_Tablesets_QuoteHedAttchRow[],
   QSalesRP:Erp_Tablesets_QSalesRPRow[],
   QuoteCnt:Erp_Tablesets_QuoteCntRow[],
   QuoteCom:Erp_Tablesets_QuoteComRow[],
   QuoteDtl:Erp_Tablesets_QuoteDtlRow[],
   QuoteDtlAttch:Erp_Tablesets_QuoteDtlAttchRow[],
   QuoteCoPart:Erp_Tablesets_QuoteCoPartRow[],
   QuoteDtlAttrValueSet:Erp_Tablesets_QuoteDtlAttrValueSetRow[],
   QuoteDtlTax:Erp_Tablesets_QuoteDtlTaxRow[],
   QuoteMsc:Erp_Tablesets_QuoteMscRow[],
   QuoteQty:Erp_Tablesets_QuoteQtyRow[],
   Qtmmkup:Erp_Tablesets_QtmmkupRow[],
   QtQtyMsc:Erp_Tablesets_QtQtyMscRow[],
   QuoteHedMsc:Erp_Tablesets_QuoteHedMscRow[],
   QuoteHedTax:Erp_Tablesets_QuoteHedTaxRow[],
   HedTaxSum:Erp_Tablesets_HedTaxSumRow[],
   PartSubs:Erp_Tablesets_PartSubsRow[],
   TaxConnectStatus:Erp_Tablesets_TaxConnectStatusRow[],
   WhatIfScheduling:Erp_Tablesets_WhatIfSchedulingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SaveOTSParamsRow{
   OTSAddress1:string,
   OTSAddress2:string,
   OTSAddress3:string,
   OTSCity:string,
   OTSContact:string,
   OTSCountryNum:number,
   OTSCustSaved:boolean,
   OTSFaxNum:string,
   OTSName:string,
   OTSPhoneNum:string,
   OTSResaleID:string,
   OTSSaveAs:string,
   OTSSaveCustID:string,
   OTSSaved:boolean,
   OTSShipToNum:string,
   OTSState:string,
   OTSTaxRegionCode:string,
   OTSZIP:string,
   OTSOverride:boolean,
   OTSTaxValidationStatus:number,
   OTSTaxValidationDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SaveQuoteOTSParamsTableset{
   SaveOTSParams:Erp_Tablesets_SaveOTSParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaxConnectStatusRow{
      /**  Company  */  
   Company:string,
      /**  If true, service is down. If false, service is up.  */  
   ETCOffline:boolean,
      /**  Error message returned from the call to the tax service.  */  
   ErrorMessage:string,
      /**  This is the success/failure status of the call to tax connect. If false, the call failed, if true it was successful  */  
   TCStatus:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtQuoteTableset{
   QuoteHed:Erp_Tablesets_QuoteHedRow[],
   QuoteHedAttch:Erp_Tablesets_QuoteHedAttchRow[],
   QSalesRP:Erp_Tablesets_QSalesRPRow[],
   QuoteCnt:Erp_Tablesets_QuoteCntRow[],
   QuoteCom:Erp_Tablesets_QuoteComRow[],
   QuoteDtl:Erp_Tablesets_QuoteDtlRow[],
   QuoteDtlAttch:Erp_Tablesets_QuoteDtlAttchRow[],
   QuoteCoPart:Erp_Tablesets_QuoteCoPartRow[],
   QuoteDtlAttrValueSet:Erp_Tablesets_QuoteDtlAttrValueSetRow[],
   QuoteDtlTax:Erp_Tablesets_QuoteDtlTaxRow[],
   QuoteMsc:Erp_Tablesets_QuoteMscRow[],
   QuoteQty:Erp_Tablesets_QuoteQtyRow[],
   Qtmmkup:Erp_Tablesets_QtmmkupRow[],
   QtQtyMsc:Erp_Tablesets_QtQtyMscRow[],
   QuoteHedMsc:Erp_Tablesets_QuoteHedMscRow[],
   QuoteHedTax:Erp_Tablesets_QuoteHedTaxRow[],
   HedTaxSum:Erp_Tablesets_HedTaxSumRow[],
   PartSubs:Erp_Tablesets_PartSubsRow[],
   TaxConnectStatus:Erp_Tablesets_TaxConnectStatusRow[],
   WhatIfScheduling:Erp_Tablesets_WhatIfSchedulingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WhatIfSchedulingRow{
   CompletionDate:string,
   ConsiderLeadTime:boolean,
      /**  Production Qty  */  
   ProdQty:number,
   ProdStartDate:string,
   SchedFinitely:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param quoteNum
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface ExistContact_input{
      /**  QuoteNum of the QuoteCnt record  */  
   quoteNum:number,
      /**  Customer Number of the QuoteCnt record  */  
   custNum:number,
      /**  ShipTo Number of the QuoteCnt record  */  
   shipToNum:string,
      /**  Contact Number of the QuoteCnt record  */  
   conNum:number,
}

export interface ExistContact_output{
   returnObj:boolean,
}

   /** Required : 
      @param custNum
      @param shipToNum
   */  
export interface ExistShipTo_input{
      /**  Customer Number of the QuoteCnt record  */  
   custNum:number,
      /**  ShipTo Number of the QuoteCnt record  */  
   shipToNum:string,
}

export interface ExistShipTo_output{
}

   /** Required : 
      @param returnLineType
      @param quoteNum
      @param quoteLine
   */  
export interface ExistsCreditMemo_input{
      /**  Return type selected  */  
   returnLineType:string,
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote line number  */  
   quoteLine:number,
}

export interface ExistsCreditMemo_output{
   returnObj:boolean,
}

   /** Required : 
      @param quoteNum
      @param partNum
      @param sellingExpectedUM
   */  
export interface ExistsPartDiscPriceList_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Part Number  */  
   partNum:string,
      /**  Selling Expected Unit Of Measure  */  
   sellingExpectedUM:string,
}

export interface ExistsPartDiscPriceList_output{
   returnObj:boolean,
}

   /** Required : 
      @param quoteNum
      @param partNum
      @param sellingExpectedUM
   */  
export interface ExistsPartPriceList_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Part Number  */  
   partNum:string,
      /**  Selling Expected Unit Of Measure  */  
   sellingExpectedUM:string,
}

export interface ExistsPartPriceList_output{
   returnObj:boolean,
}

   /** Required : 
      @param quoteNum
      @param prodCode
      @param sellingExpectedUM
   */  
export interface ExistsProductGroupDiscPriceList_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Product Group  */  
   prodCode:string,
      /**  Selling Expected Unit Of Measure  */  
   sellingExpectedUM:string,
}

export interface ExistsProductGroupDiscPriceList_output{
   returnObj:boolean,
}

   /** Required : 
      @param quoteNum
      @param prodCode
      @param sellingExpectedUM
   */  
export interface ExistsProductGroupPriceList_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Product Group  */  
   prodCode:string,
      /**  Selling Expected Unit Of Measure  */  
   sellingExpectedUM:string,
}

export interface ExistsProductGroupPriceList_output{
   returnObj:boolean,
}

   /** Required : 
      @param quoteNum
   */  
export interface ExportQuoteToEST_input{
   quoteNum:number,
}

export interface ExportQuoteToEST_output{
}

   /** Required : 
      @param FileInfo
   */  
export interface FileType_input{
   FileInfo:string,
}

export interface FileType_output{
   returnObj:string,
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param quoteNum
   */  
export interface GetByID_input{
   quoteNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param quoteNum
      @param compNum
   */  
export interface GetCompetitorInfo_input{
      /**  QuoteNum of the QuoteCom record  */  
   quoteNum:number,
      /**  Competitor Number of the QuoteCom record  */  
   compNum:number,
}

export interface GetCompetitorInfo_output{
parameters : {
      /**  output parameters  */  
   name:string,
   faxNum:string,
   phoneNum:string,
   emailAddress:string,
   compURL:string,
}
}

   /** Required : 
      @param quoteNum
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface GetContactInfo_input{
      /**  QuoteNum of the QuoteCom record  */  
   quoteNum:number,
      /**  Customr Number of the QuoteCom record  */  
   custNum:number,
      /**  ShipTo Number of the QuoteCom record  */  
   shipToNum:string,
      /**  Contact Number of the QuoteCom record  */  
   conNum:number,
}

export interface GetContactInfo_output{
parameters : {
      /**  output parameters  */  
   perConID:number,
   perConName:string,
   name:string,
   func:string,
   phoneNum:string,
   fax:string,
   emailAddress:string,
}
}

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
}
}

   /** Required : 
      @param quoteNum
      @param custNum
      @param shipToNum
      @param conNum
      @param perConID
      @param ds
   */  
export interface GetCustCntInfo_input{
      /**  QuoteNum of the QuoteCom record  */  
   quoteNum:number,
      /**  Customr Number of the QuoteCom record  */  
   custNum:number,
      /**  input - output - ShipTo Number of the QuoteCom record  */  
   shipToNum:string,
      /**  input output - Contact Number of the QuoteCom record  */  
   conNum:number,
      /**  input output - The Contact PerConID  */  
   perConID:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetCustCntInfo_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetCustPartInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetCustPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetCustomerInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetCustomerInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetDiscountPriceListInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetDiscountPriceListInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param skipDiscLookup
      @param preserveAmt
      @param pIsGridPasting
      @param pChangedByUser
      @param ds
   */  
export interface GetDtlUnitPriceInfo_User_input{
      /**  Skip lookup of DiscPercent  */  
   skipDiscLookup:boolean,
      /**  Preserve the DiscountAmt  */  
   preserveAmt:boolean,
      /**  Is a Paste Insert in the Grid  */  
   pIsGridPasting:boolean,
      /**  The user typed the Unit Price  */  
   pChangedByUser:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetDtlUnitPriceInfo_User_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param skipDiscLookup
      @param preserveAmt
      @param ds
   */  
export interface GetDtlUnitPriceInfo_input{
      /**  Skip lookup of DiscPercent  */  
   skipDiscLookup:boolean,
      /**  Preserve the DiscountAmt  */  
   preserveAmt:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetDtlUnitPriceInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param vCurrencyCode
      @param vRateGrpCode
   */  
export interface GetExchangeRate_input{
      /**  Currency selected for the Quote  */  
   vCurrencyCode:string,
      /**  Currency Rate Group selected for the quote  */  
   vRateGrpCode:string,
}

export interface GetExchangeRate_output{
parameters : {
      /**  output parameters  */  
   vExchangeRate:number,
   vXRateLabel:string,
}
}

export interface GetExternalCRMIntegrationIsEnabled_output{
   returnObj:boolean,
}

export interface GetIfCurrentSiteHasExternalMES_output{
   returnObj:boolean,
}

   /** Required : 
      @param PartNum
      @param RevisionNum
   */  
export interface GetIfRevIsExternalMES_input{
   PartNum:string,
   RevisionNum:string,
}

export interface GetIfRevIsExternalMES_output{
   returnObj:boolean,
}

   /** Required : 
      @param iPartNum
      @param iRevisionNum
      @param iAltMethod
      @param iTargetAsm
      @param quoteNum
      @param quoteLine
      @param iUseMethodForParts
      @param regenerateKit
      @param errorMsg
      @param ds
   */  
export interface GetKitComponents_input{
      /**  Part Number of the given QuoteLine  */  
   iPartNum:string,
      /**  Revision Number selected for the given PartNum  */  
   iRevisionNum:string,
      /**  Aletrnate Method of the given Part number  */  
   iAltMethod:string,
      /**  Target assembly to be exploded (usually asm 0)  */  
   iTargetAsm:number,
      /**  Quote number to be exploded  */  
   quoteNum:number,
      /**  Quote line which will be the Kit Parent  */  
   quoteLine:number,
      /**  -  */  
   iUseMethodForParts:boolean,
      /**  If TRUE then it will delete all components before getting them again  */  
   regenerateKit:boolean,
      /**  Input-Output parameter that will hold the error messages in case something went wrong  */  
   errorMsg:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetKitComponents_output{
parameters : {
      /**  output parameters  */  
   errorMsg:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param whereClause
      @param whereClauseDtl
      @param pageSize
      @param absolutePage
      @param customClause
   */  
export interface GetListCustom_input{
      /**  The search criteria  */  
   whereClause:string,
      /**  The search criteria  */  
   whereClauseDtl:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
      /**  Custom WhereClause  */  
   customClause:string,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_QuoteHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListForAuthorizedTerritories_input{
      /**  The search criteria  */  
   whereClause:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetListForAuthorizedTerritories_output{
   returnObj:Erp_Tablesets_QuoteHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetListFromSelectedKeys_input{
   ds:Erp_Tablesets_QuoteHedListTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetListFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteHedListTableset[],
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_QuoteHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param qtyNum
   */  
export interface GetMaterialMarkup_input{
      /**  Quote Num  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Quote Qty Number  */  
   qtyNum:number,
}

export interface GetMaterialMarkup_output{
parameters : {
      /**  output parameters  */  
   mtlMarkupP:number,
   mtlMarkupM:number,
}
}

   /** Required : 
      @param ds
      @param tableName
   */  
export interface GetMiscChrgDefaults_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  name of table being passed in  */  
   tableName:string,
}

export interface GetMiscChrgDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetMktgInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetMktgInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param ipQuoteNum
   */  
export interface GetNewContractQuoteDtl_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  The quote number to add the line to  */  
   ipQuoteNum:number,
}

export interface GetNewContractQuoteDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
   */  
export interface GetNewQSalesRP_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
}

export interface GetNewQSalesRP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param qtyNum
   */  
export interface GetNewQtQtyMsc_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
   qtyNum:number,
}

export interface GetNewQtQtyMsc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param qtyNum
   */  
export interface GetNewQtmmkup_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
   qtyNum:number,
}

export interface GetNewQtmmkup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface GetNewQuoteCnt_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   custNum:number,
   shipToNum:string,
   conNum:number,
}

export interface GetNewQuoteCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
   */  
export interface GetNewQuoteCoPart_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
}

export interface GetNewQuoteCoPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
   */  
export interface GetNewQuoteCom_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
}

export interface GetNewQuoteCom_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
   */  
export interface GetNewQuoteDtlAttch_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
}

export interface GetNewQuoteDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
   */  
export interface GetNewQuoteDtlAttrValueSet_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
}

export interface GetNewQuoteDtlAttrValueSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param rateCode
   */  
export interface GetNewQuoteDtlTax_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewQuoteDtlTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
   */  
export interface GetNewQuoteDtl_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
}

export interface GetNewQuoteDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
   */  
export interface GetNewQuoteHedAttch_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
}

export interface GetNewQuoteHedAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param qtyNum
   */  
export interface GetNewQuoteHedMsc_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
   qtyNum:number,
}

export interface GetNewQuoteHedMsc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param taxCode
      @param rateCode
   */  
export interface GetNewQuoteHedTax_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewQuoteHedTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewQuoteHed_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetNewQuoteHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
      @param qtyNum
   */  
export interface GetNewQuoteMsc_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
   qtyNum:number,
}

export interface GetNewQuoteMsc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param quoteLine
   */  
export interface GetNewQuoteQty_input{
   ds:Erp_Tablesets_QuoteTableset[],
   quoteNum:number,
   quoteLine:number,
}

export interface GetNewQuoteQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param ds
   */  
export interface GetNewSalesKit_input{
   quoteNum:number,
   quoteLine:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetNewSalesKit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
   ipRowType:string,
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param partNum
      @param SysRowID
      @param rowType
      @param uomCode
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param quoteNum
      @param custNum
      @param shipToNum
      @param conNum
      @param ipPerConID
   */  
export interface GetPerConInfo_input{
      /**  QuoteNum of the QuoteCom record  */  
   quoteNum:number,
      /**  Customr Number of the QuoteCom record  */  
   custNum:number,
      /**  ShipTo Number of the QuoteCom record  */  
   shipToNum:string,
      /**  Contact Number of the QuoteCom record  */  
   conNum:number,
      /**  the Contact PerConID  */  
   ipPerConID:number,
}

export interface GetPerConInfo_output{
parameters : {
      /**  output parameters  */  
   perConName:string,
   name:string,
   func:string,
   phoneNum:string,
   fax:string,
   emailAddress:string,
}
}

   /** Required : 
      @param perConID
      @param ds
   */  
export interface GetPerConInformation_input{
      /**  Person/Contact ID  */  
   perConID:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetPerConInformation_output{
parameters : {
      /**  output parameters  */  
   result:number,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param phPartNum
      @param quoteNum
      @param quoteLine
      @param errMessage
      @param ds
   */  
export interface GetPhantomComponents_input{
   phPartNum:string,
   quoteNum:number,
   quoteLine:number,
   errMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetPhantomComponents_output{
parameters : {
      /**  output parameters  */  
   errMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

export interface GetPlantConfCtrlUse3rdPartySched_output{
      /**  bool: the value  */  
   returnObj:boolean,
}

   /** Required : 
      @param ipCompanyID
      @param ipPlant
   */  
export interface GetPlantConfCtrlValues_input{
      /**  The company for the quote  */  
   ipCompanyID:string,
      /**  The login plant for the session  */  
   ipPlant:string,
}

export interface GetPlantConfCtrlValues_output{
parameters : {
      /**  output parameters  */  
   opUse3rdPartySched:boolean,
   opEnableManifestRateShopping:boolean,
   opManifestRateShoppingURL:string,
}
}

   /** Required : 
      @param ds
      @param refreshQty
   */  
export interface GetPriceListInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  Indicate if the app needs to refresh the Quantity Breaks  */  
   refreshQty:boolean,
}

export interface GetPriceListInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetQtyPriceInfoCfgPart_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetQtyPriceInfoCfgPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   hasPriceBreak:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetQtyPriceInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetQtyPriceInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   hasPriceBreak:boolean,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param quantityToOrder
      @param sellingUM
   */  
export interface GetQtyToOrdPrice_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Quantity used to create order  */  
   quantityToOrder:number,
      /**  Selling UM  */  
   sellingUM:string,
}

export interface GetQtyToOrdPrice_output{
parameters : {
      /**  output parameters  */  
   orderUnitPrice:number,
   docOrderUnitPrice:number,
}
}

   /** Required : 
      @param quoteNum
      @param maxNumOfCards
   */  
export interface GetQuoteRelationshipMap_input{
   quoteNum:number,
   maxNumOfCards:number,
}

export interface GetQuoteRelationshipMap_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetQuotedInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetQuotedInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetQuotesForCustomer_input{
      /**  Where clause for quote retrieval.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetQuotesForCustomer_output{
   returnObj:Erp_Tablesets_QuoteCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param vReasonType
      @param vQuoteNum
      @param vOrdered
      @param vReasonCode
   */  
export interface GetReasonInfo_input{
      /**  ReasonType of the Quote (Win, Task)  */  
   vReasonType:string,
      /**  Unique key of the Quote  */  
   vQuoteNum:number,
      /**  Flag indicating if an order has been created from the quote  */  
   vOrdered:boolean,
      /**  Default ReasonCode for the Quote Task/ReasonType  */  
   vReasonCode:string,
}

export interface GetReasonInfo_output{
parameters : {
      /**  output parameters  */  
   vReasonCode:string,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param whereClauseQuoteHedAttch
      @param whereClauseQSalesRP
      @param whereClauseQuoteCnt
      @param whereClauseQuoteCom
      @param whereClauseQuoteDtl
      @param whereClauseQuoteDtlAttch
      @param whereClauseQuoteCoPart
      @param whereClauseQuoteDtlAttrValueSet
      @param whereClauseQuoteDtlTax
      @param whereClauseQuoteMsc
      @param whereClauseQuoteQty
      @param whereClauseQtmmkup
      @param whereClauseQtQtyMsc
      @param whereClauseQuoteHedMsc
      @param whereClauseQuoteHedTax
      @param whereClauseHedTaxSum
      @param whereClausePartSubs
      @param whereClauseTaxConnectStatus
      @param whereClauseWhatIfScheduling
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
   whereClauseQuoteHed:string,
   whereClauseQuoteHedAttch:string,
   whereClauseQSalesRP:string,
   whereClauseQuoteCnt:string,
   whereClauseQuoteCom:string,
   whereClauseQuoteDtl:string,
   whereClauseQuoteDtlAttch:string,
   whereClauseQuoteCoPart:string,
   whereClauseQuoteDtlAttrValueSet:string,
   whereClauseQuoteDtlTax:string,
   whereClauseQuoteMsc:string,
   whereClauseQuoteQty:string,
   whereClauseQtmmkup:string,
   whereClauseQtQtyMsc:string,
   whereClauseQuoteHedMsc:string,
   whereClauseQuoteHedTax:string,
   whereClauseHedTaxSum:string,
   whereClausePartSubs:string,
   whereClauseTaxConnectStatus:string,
   whereClauseWhatIfScheduling:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param whereClauseQuoteHedAttch
      @param whereClauseQSalesRP
      @param whereClauseQuoteCnt
      @param whereClauseQuoteCom
      @param whereClauseQuoteDtl
      @param whereClauseQuoteDtlAttch
      @param whereClauseQuoteMsc
      @param whereClauseQuoteHedMsc
      @param whereClauseQuoteQty
      @param whereClauseQtmmkup
      @param whereClauseQtQtyMsc
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for QuoteHed table.  */  
   whereClauseQuoteHed:string,
      /**  Whereclause for QuoteHedAttch table.  */  
   whereClauseQuoteHedAttch:string,
      /**  Whereclause for QSalesRP table.  */  
   whereClauseQSalesRP:string,
      /**  Whereclause for QuoteCnt table.  */  
   whereClauseQuoteCnt:string,
      /**  Whereclause for QuoteCom table.  */  
   whereClauseQuoteCom:string,
      /**  Whereclause for QuoteDtl table.  */  
   whereClauseQuoteDtl:string,
      /**  Whereclause for QuoteDtlAt table.  */  
   whereClauseQuoteDtlAttch:string,
      /**  Whereclause for QuoteMsc table.  */  
   whereClauseQuoteMsc:string,
      /**  Whereclause for QuoteHedMsc table.  */  
   whereClauseQuoteHedMsc:string,
      /**  Whereclause for QuoteQty table.  */  
   whereClauseQuoteQty:string,
      /**  Whereclause for Qtmmkup table.  */  
   whereClauseQtmmkup:string,
      /**  Whereclause for QtQtyMsc table.  */  
   whereClauseQtQtyMsc:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_QuoteCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param whereClauseQuoteHedAttch
      @param whereClauseQSalesRP
      @param whereClauseQuoteCnt
      @param whereClauseQuoteCom
      @param whereClauseQuoteDtl
      @param whereClauseQuoteDtlAttch
      @param whereClauseQuoteCoPart
      @param whereClauseQuoteDtlAttrValueSet
      @param whereClauseQuoteDtlTax
      @param whereClauseQuoteMsc
      @param whereClauseQuoteQty
      @param whereClauseQtmmkup
      @param whereClauseQtQtyMsc
      @param whereClauseQuoteHedMsc
      @param whereClauseQuoteHedTax
      @param whereClauseHedTaxSum
      @param whereClausePartSubs
      @param whereClauseTaxConnectStatus
      @param whereClauseWhatIfScheduling
      @param groupID
      @param headNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForCashReceipt_input{
   whereClauseQuoteHed:string,
   whereClauseQuoteHedAttch:string,
   whereClauseQSalesRP:string,
   whereClauseQuoteCnt:string,
   whereClauseQuoteCom:string,
   whereClauseQuoteDtl:string,
   whereClauseQuoteDtlAttch:string,
   whereClauseQuoteCoPart:string,
   whereClauseQuoteDtlAttrValueSet:string,
   whereClauseQuoteDtlTax:string,
   whereClauseQuoteMsc:string,
   whereClauseQuoteQty:string,
   whereClauseQtmmkup:string,
   whereClauseQtQtyMsc:string,
   whereClauseQuoteHedMsc:string,
   whereClauseQuoteHedTax:string,
   whereClauseHedTaxSum:string,
   whereClausePartSubs:string,
   whereClauseTaxConnectStatus:string,
   whereClauseWhatIfScheduling:string,
   groupID:string,
   headNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForCashReceipt_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param whereClauseQuoteHedAttch
      @param whereClauseQSalesRP
      @param whereClauseQuoteCnt
      @param whereClauseQuoteCom
      @param whereClauseQuoteDtl
      @param whereClauseQuoteDtlAttch
      @param whereClauseQuoteCoPart
      @param whereClauseQuoteDtlAttrValueSet
      @param whereClauseQuoteDtlTax
      @param whereClauseQuoteMsc
      @param whereClauseQuoteQty
      @param whereClauseQtmmkup
      @param whereClauseQtQtyMsc
      @param whereClauseQuoteHedMsc
      @param whereClauseQuoteHedTax
      @param whereClauseHedTaxSum
      @param whereClausePartSubs
      @param whereClauseTaxConnectStatus
      @param whereClauseWhatIfScheduling
      @param invoiceNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForInvoice_input{
   whereClauseQuoteHed:string,
   whereClauseQuoteHedAttch:string,
   whereClauseQSalesRP:string,
   whereClauseQuoteCnt:string,
   whereClauseQuoteCom:string,
   whereClauseQuoteDtl:string,
   whereClauseQuoteDtlAttch:string,
   whereClauseQuoteCoPart:string,
   whereClauseQuoteDtlAttrValueSet:string,
   whereClauseQuoteDtlTax:string,
   whereClauseQuoteMsc:string,
   whereClauseQuoteQty:string,
   whereClauseQtmmkup:string,
   whereClauseQtQtyMsc:string,
   whereClauseQuoteHedMsc:string,
   whereClauseQuoteHedTax:string,
   whereClauseHedTaxSum:string,
   whereClausePartSubs:string,
   whereClauseTaxConnectStatus:string,
   whereClauseWhatIfScheduling:string,
   invoiceNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForInvoice_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param whereClauseQuoteHedAttch
      @param whereClauseQSalesRP
      @param whereClauseQuoteCnt
      @param whereClauseQuoteCom
      @param whereClauseQuoteDtl
      @param whereClauseQuoteDtlAttch
      @param whereClauseQuoteCoPart
      @param whereClauseQuoteDtlAttrValueSet
      @param whereClauseQuoteDtlTax
      @param whereClauseQuoteMsc
      @param whereClauseQuoteQty
      @param whereClauseQtmmkup
      @param whereClauseQtQtyMsc
      @param whereClauseQuoteHedMsc
      @param whereClauseQuoteHedTax
      @param whereClauseHedTaxSum
      @param whereClausePartSubs
      @param whereClauseTaxConnectStatus
      @param whereClauseWhatIfScheduling
      @param orderNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForSalesOrder_input{
   whereClauseQuoteHed:string,
   whereClauseQuoteHedAttch:string,
   whereClauseQSalesRP:string,
   whereClauseQuoteCnt:string,
   whereClauseQuoteCom:string,
   whereClauseQuoteDtl:string,
   whereClauseQuoteDtlAttch:string,
   whereClauseQuoteCoPart:string,
   whereClauseQuoteDtlAttrValueSet:string,
   whereClauseQuoteDtlTax:string,
   whereClauseQuoteMsc:string,
   whereClauseQuoteQty:string,
   whereClauseQtmmkup:string,
   whereClauseQtQtyMsc:string,
   whereClauseQuoteHedMsc:string,
   whereClauseQuoteHedTax:string,
   whereClauseHedTaxSum:string,
   whereClausePartSubs:string,
   whereClauseTaxConnectStatus:string,
   whereClauseWhatIfScheduling:string,
   orderNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForSalesOrder_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param whereClauseQuoteHedAttch
      @param whereClauseQSalesRP
      @param whereClauseQuoteCnt
      @param whereClauseQuoteCom
      @param whereClauseQuoteDtl
      @param whereClauseQuoteDtlAttch
      @param whereClauseQuoteCoPart
      @param whereClauseQuoteDtlAttrValueSet
      @param whereClauseQuoteDtlTax
      @param whereClauseQuoteMsc
      @param whereClauseQuoteQty
      @param whereClauseQtmmkup
      @param whereClauseQtQtyMsc
      @param whereClauseQuoteHedMsc
      @param whereClauseQuoteHedTax
      @param whereClauseHedTaxSum
      @param whereClausePartSubs
      @param whereClauseTaxConnectStatus
      @param whereClauseWhatIfScheduling
      @param packNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForShipment_input{
   whereClauseQuoteHed:string,
   whereClauseQuoteHedAttch:string,
   whereClauseQSalesRP:string,
   whereClauseQuoteCnt:string,
   whereClauseQuoteCom:string,
   whereClauseQuoteDtl:string,
   whereClauseQuoteDtlAttch:string,
   whereClauseQuoteCoPart:string,
   whereClauseQuoteDtlAttrValueSet:string,
   whereClauseQuoteDtlTax:string,
   whereClauseQuoteMsc:string,
   whereClauseQuoteQty:string,
   whereClauseQtmmkup:string,
   whereClauseQtQtyMsc:string,
   whereClauseQuoteHedMsc:string,
   whereClauseQuoteHedTax:string,
   whereClauseHedTaxSum:string,
   whereClausePartSubs:string,
   whereClauseTaxConnectStatus:string,
   whereClauseWhatIfScheduling:string,
   packNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForShipment_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsFromSelectedKeys_input{
   ds:Erp_Tablesets_QuoteTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRowsFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param whereClauseQuoteHedAttch
      @param whereClauseQSalesRP
      @param whereClauseQuoteCnt
      @param whereClauseQuoteCom
      @param whereClauseQuoteDtl
      @param whereClauseQuoteDtlAttch
      @param whereClauseQuoteCoPart
      @param whereClauseQuoteDtlAttrValueSet
      @param whereClauseQuoteDtlTax
      @param whereClauseQuoteMsc
      @param whereClauseQuoteQty
      @param whereClauseQtmmkup
      @param whereClauseQtQtyMsc
      @param whereClauseQuoteHedMsc
      @param whereClauseQuoteHedTax
      @param whereClauseHedTaxSum
      @param whereClausePartSubs
      @param whereClauseTaxConnectStatus
      @param whereClauseWhatIfScheduling
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseQuoteHed:string,
   whereClauseQuoteHedAttch:string,
   whereClauseQSalesRP:string,
   whereClauseQuoteCnt:string,
   whereClauseQuoteCom:string,
   whereClauseQuoteDtl:string,
   whereClauseQuoteDtlAttch:string,
   whereClauseQuoteCoPart:string,
   whereClauseQuoteDtlAttrValueSet:string,
   whereClauseQuoteDtlTax:string,
   whereClauseQuoteMsc:string,
   whereClauseQuoteQty:string,
   whereClauseQtmmkup:string,
   whereClauseQtQtyMsc:string,
   whereClauseQuoteHedMsc:string,
   whereClauseQuoteHedTax:string,
   whereClauseHedTaxSum:string,
   whereClausePartSubs:string,
   whereClauseTaxConnectStatus:string,
   whereClauseWhatIfScheduling:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param regenerateKits
      @param ds
   */  
export interface GetSalesKitComponents_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote line  */  
   quoteLine:number,
      /**  Regenerate kits  */  
   regenerateKits:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetSalesKitComponents_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   returnMessage:string,
}
}

   /** Required : 
      @param defaultRoleCode
      @param quoteNum
      @param salesRepCode
      @param roleCode
   */  
export interface GetSalesRepInfo_input{
      /**  Indicates whether to default the RoleCode from the SalesRep  */  
   defaultRoleCode:boolean,
      /**  QuoteNum of the QSalesRP record  */  
   quoteNum:number,
      /**  Salesperson of the QSalesRP record  */  
   salesRepCode:string,
      /**  RoleCode of the QSalesRP record, if defaultRoleCode is checked, then
            a different value may be returned  */  
   roleCode:string,
}

export interface GetSalesRepInfo_output{
parameters : {
      /**  output parameters  */  
   roleCode:string,
   name:string,
   repRate:number,
   repSplit:number,
   officePhone:string,
   homePhone:string,
   reportsTo:string,
   emailAddress:string,
   fax:string,
   mobilePhone:string,
   salesRepTitle:string,
   roleCodeRoleDescription:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetShipToInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetShipToInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param PartNum
      @param RevisionNum
   */  
export interface GetSmartString_input{
      /**  Kit component quote number  */  
   QuoteNum:number,
      /**  Kit component quote line  */  
   QuoteLine:number,
      /**  The part being configured  */  
   PartNum:string,
      /**  The revision being configured  */  
   RevisionNum:string,
}

export interface GetSmartString_output{
parameters : {
      /**  output parameters  */  
   SmartString:string,
   CreatePart:boolean,
   PromptForPartNum:boolean,
   NotifyOfExistingPart:boolean,
   NewPartNum:string,
   CreateCustPart:boolean,
   PromptForCustPartNum:boolean,
   NewCustPartNum:string,
   PromptForAutoCreatePart:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetTaskSetInfo_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetTaskSetInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipCompanyID
      @param ipQuoteNum
      @param ipCustNum
      @param ipShipToNum
   */  
export interface GetTaxRegInPrice_input{
   ipCompanyID:string,
   ipQuoteNum:number,
   ipCustNum:number,
   ipShipToNum:string,
}

export interface GetTaxRegInPrice_output{
parameters : {
      /**  output parameters  */  
   opTaxRegionCode:string,
   opInPrice:boolean,
   opTaxRecords:boolean,
}
}

   /** Required : 
      @param vQuoteNum
      @param vTerritoryID
      @param vActiveTaskID
      @param vTaskSetId
   */  
export interface GetTerrInfo_input{
      /**  The current QuoteHed.QuoteNum field  */  
   vQuoteNum:number,
      /**  The QuoteHed.TerritoryID  */  
   vTerritoryID:string,
      /**  The QuoteHed.ActiveTaskID  */  
   vActiveTaskID:string,
      /**  Returns the correct TaskSet for the Territory  */  
   vTaskSetId:string,
}

export interface GetTerrInfo_output{
parameters : {
      /**  output parameters  */  
   vTaskSetId:string,
}
}

   /** Required : 
      @param ipCompanyID
      @param ipQuoteNum
      @param ipCustNum
      @param ipShipToNum
   */  
export interface GetUpdtDtlTaxRgn_input{
   ipCompanyID:string,
   ipQuoteNum:number,
   ipCustNum:number,
   ipShipToNum:string,
}

export interface GetUpdtDtlTaxRgn_output{
parameters : {
      /**  output parameters  */  
   opUpdtDtlTaxRgn:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetWSUnitPrice_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface GetWSUnitPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param PartNum
      @param RevisionNum
      @param SmartString
      @param NewPartNum
      @param NewCustPartNum
      @param ResponseAutoCrtPart
   */  
export interface KitCompPartCreate_input{
      /**  Kit component quote number  */  
   QuoteNum:number,
      /**  Kit component quote line  */  
   QuoteLine:number,
      /**  The part being configured  */  
   PartNum:string,
      /**  The revision being configured  */  
   RevisionNum:string,
      /**  The generated smartstring of the configuration  */  
   SmartString:string,
      /**  The Part Number to be used for a new part creation.  If blank, a part will not be created.  */  
   NewPartNum:string,
      /**  The Customer Part Number to stored on the quote line.  */  
   NewCustPartNum:string,
      /**  Answer to the question presented to user about auto creating a part.  */  
   ResponseAutoCrtPart:boolean,
}

export interface KitCompPartCreate_output{
parameters : {
      /**  output parameters  */  
   NewPartAlreadyExists:boolean,
}
}

export interface LaunchGlobalAlerts_output{
}

   /** Required : 
      @param date1
      @param date2
   */  
export interface MinimumDate_input{
   date1:string,
   date2:string,
}

export interface MinimumDate_output{
   returnObj:string,
}

   /** Required : 
      @param attributeValueSeq
      @param quantityToOrder
      @param ds
   */  
export interface OnChangeAttrQuantityToOrder_input{
      /**  Attribute Value Sequence  */  
   attributeValueSeq:number,
      /**  Quantity To Order  */  
   quantityToOrder:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeAttrQuantityToOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param incotermCode
   */  
export interface OnChangeIncotermCode_input{
      /**  Incoterm Code  */  
   incotermCode:string,
}

export interface OnChangeIncotermCode_output{
parameters : {
      /**  output parameters  */  
   incotermLocation:string,
   enableIncotermLocation:boolean,
}
}

   /** Required : 
      @param mktgCampID
      @param ds
   */  
export interface OnChangeMktgCamp_input{
      /**  The CampID  */  
   mktgCampID:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeMktgCamp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param mktgEvntSeq
      @param ds
   */  
export interface OnChangeMktgEvnt_input{
      /**  The EvntSeq  */  
   mktgEvntSeq:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeMktgEvnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param attributeValueSeq
      @param numberOfPieces
      @param ds
   */  
export interface OnChangeNumberOfPieces_input{
      /**  Attribute Value Sequence  */  
   attributeValueSeq:number,
      /**  Number Of Pieces  */  
   numberOfPieces:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param TaxCode
      @param RateCode
      @param NewFixedAmount
      @param ds
   */  
export interface OnChangeOfFixedAmount_input{
   QuoteNum:number,
   QuoteLine:number,
   TaxCode:string,
   RateCode:string,
   NewFixedAmount:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeOfFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param TaxCode
      @param NewReportableAmt
      @param ds
   */  
export interface OnChangeOfReportableAmt_input{
   QuoteNum:number,
   QuoteLine:number,
   TaxCode:string,
   NewReportableAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeOfReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param TaxCode
      @param NewTaxAmt
      @param ds
   */  
export interface OnChangeOfTaxAmt_input{
   QuoteNum:number,
   QuoteLine:number,
   TaxCode:string,
   NewTaxAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeOfTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param TaxCode
      @param NewPercent
      @param ds
   */  
export interface OnChangeOfTaxPercent_input{
   QuoteNum:number,
   QuoteLine:number,
   TaxCode:string,
   NewPercent:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeOfTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param proposedRateCode
      @param ds
   */  
export interface OnChangeRateCode_input{
   proposedRateCode:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
      @param ipTaxCode
      @param ds
   */  
export interface OnChangeTaxCode_input{
   ipQuoteNum:number,
   ipQuoteLine:number,
   ipTaxCode:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
      @param TaxCode
      @param RateCode
      @param NewTaxableAmt
      @param ds
   */  
export interface OnChangeTaxableAmt_input{
   QuoteNum:number,
   QuoteLine:number,
   TaxCode:string,
   RateCode:string,
   NewTaxableAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param newBillToCustID
      @param ds
   */  
export interface OnChangeofBTCustID_input{
      /**  Proposed bill to custid  */  
   newBillToCustID:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeofBTCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param newReadyToQuote
      @param ds
   */  
export interface OnChangeofEngineered_input{
      /**  Proposed ReadyToQuote  */  
   newReadyToQuote:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface OnChangeofEngineered_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param QuoteNum
      @param QuoteLine
   */  
export interface OnChangeofLineExemptTax_input{
      /**  Quote Number.  */  
   QuoteNum:number,
      /**  Quote line number.  */  
   QuoteLine:number,
}

export interface OnChangeofLineExemptTax_output{
parameters : {
      /**  output parameters  */  
   AskManualQuestion:boolean,
}
}

   /** Required : 
      @param quoteNum
      @param closeQuote
   */  
export interface OpenCloseQuote_input{
      /**  QuoteNum to be opened or closed  */  
   quoteNum:number,
      /**  Yes to close Quote, no to open Quote  */  
   closeQuote:boolean,
}

export interface OpenCloseQuote_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param assemblySeq
   */  
export interface PopulateCallContext_input{
   quoteNum:number,
   quoteLine:number,
   assemblySeq:number,
}

export interface PopulateCallContext_output{
parameters : {
      /**  output parameters  */  
   callContext:string,
}
}

   /** Required : 
      @param quoteNum
      @param closeQuote
   */  
export interface PreOpenCloseQuote_input{
      /**  The current QuoteHed.QuoteNum field  */  
   quoteNum:number,
      /**  Yes to close Quote, no to open Quote  */  
   closeQuote:boolean,
}

export interface PreOpenCloseQuote_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreRefreshQty_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface PreRefreshQty_output{
parameters : {
      /**  output parameters  */  
   strquestion:string,
}
}

   /** Required : 
      @param ipQuoteNum
   */  
export interface PreSOCreate_input{
      /**  Quote number  */  
   ipQuoteNum:number,
}

export interface PreSOCreate_output{
parameters : {
      /**  output parameters  */  
   ouAskMess:string,
}
}

   /** Required : 
      @param quoteNum
      @param fieldList
   */  
export interface PropagateQuoteHedChangesToQuoteDtl_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  List of fields to propagate  */  
   fieldList:string,
}

export interface PropagateQuoteHedChangesToQuoteDtl_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param proposedPrimRep
      @param ds
   */  
export interface QSalesRPPrimeRepChanging_input{
   proposedPrimRep:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QSalesRPPrimeRepChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface QuoteCntShipToConNumChangedInactive_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Customer number  */  
   custNum:number,
      /**  Ship To Number  */  
   shipToNum:string,
      /**  Contact Number  */  
   conNum:number,
}

export interface QuoteCntShipToConNumChangedInactive_output{
parameters : {
      /**  output parameters  */  
   perConID:number,
   perConName:string,
   name:string,
   contactFunc:string,
   phoneNum:string,
   faxNum:string,
   emailAddress:string,
   shipToInactive:boolean,
}
}

   /** Required : 
      @param quoteNum
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface QuoteCntShipToConNumChanged_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Customer number  */  
   custNum:number,
      /**  Ship To Number  */  
   shipToNum:string,
      /**  Contact Number  */  
   conNum:number,
}

export interface QuoteCntShipToConNumChanged_output{
parameters : {
      /**  output parameters  */  
   perConID:number,
   perConName:string,
   name:string,
   contactFunc:string,
   phoneNum:string,
   faxNum:string,
   emailAddress:string,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLines
   */  
export interface QuoteCreditAdd_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  delimited list of quotelines (e.g., "1~2~3"  */  
   quoteLines:string,
}

export interface QuoteCreditAdd_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   newInvoiceNum:number,
   opErrMsg:string,
}
}

   /** Required : 
      @param partHasSubstitutes
      @param uomCode
      @param ds
   */  
export interface QuoteDtlPartNumAfterChange_input{
      /**  Does the part have substitutes  */  
   partHasSubstitutes:boolean,
      /**  Unit of measure code  */  
   uomCode:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlPartNumAfterChange_output{
parameters : {
      /**  output parameters  */  
   returnMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param readyToQuote
      @param ds
   */  
export interface QuoteDtlReadyToQuoteChanging_input{
      /**  The propoesd Ready To Quote value  */  
   readyToQuote:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlReadyToQuoteChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   returnMessage:string,
}
}

   /** Required : 
      @param refreshQty
      @param getDiscountPriceListInfo
      @param clearQuoteQty
      @param ds
   */  
export interface QuoteDtlRefreshPriceListAndQuantities_input{
      /**  Refresh quantities  */  
   refreshQty:boolean,
      /**  Get discount price list info  */  
   getDiscountPriceListInfo:boolean,
      /**  Clear quote quanities before refresh  */  
   clearQuoteQty:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlRefreshPriceListAndQuantities_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface QuoteDtlRevisionNumAfterChange_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlRevisionNumAfterChange_output{
parameters : {
      /**  output parameters  */  
   errorMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param rateCode
      @param newFixedAmount
      @param ds
   */  
export interface QuoteDtlTaxBaseFixedAmountChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  Rate Code  */  
   rateCode:string,
      /**  New base fixed amount  */  
   newFixedAmount:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxBaseFixedAmountChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param newReportableAmt
      @param ds
   */  
export interface QuoteDtlTaxBaseReportableAmtChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  New base reportable amount  */  
   newReportableAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxBaseReportableAmtChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param newTaxAmt
      @param ds
   */  
export interface QuoteDtlTaxBaseTaxAmtChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  New base tax amount  */  
   newTaxAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxBaseTaxAmtChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param rateCode
      @param newTaxableAmt
      @param ds
   */  
export interface QuoteDtlTaxBaseTaxableAmtChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  Rate Code  */  
   rateCode:string,
      /**  New base taxable amount  */  
   newTaxableAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxBaseTaxableAmtChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param rateCode
      @param newFixedAmount
      @param ds
   */  
export interface QuoteDtlTaxDocFixedAmountChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  Rate Code  */  
   rateCode:string,
      /**  New base fixed amount  */  
   newFixedAmount:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxDocFixedAmountChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param newReportableAmt
      @param ds
   */  
export interface QuoteDtlTaxDocReportableAmtChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  New base reportable amount  */  
   newReportableAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxDocReportableAmtChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param newTaxAmt
      @param ds
   */  
export interface QuoteDtlTaxDocTaxAmtChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  New base tax amount  */  
   newTaxAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxDocTaxAmtChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param taxCode
      @param rateCode
      @param newTaxableAmt
      @param ds
   */  
export interface QuoteDtlTaxDocTaxableAmtChange_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Tax Code  */  
   taxCode:string,
      /**  Rate Code  */  
   rateCode:string,
      /**  New base taxable amount  */  
   newTaxableAmt:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlTaxDocTaxableAmtChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param partIsInactiveOrOnHold
      @param partHasSubstitutes
      @param uomCode
      @param ds
   */  
export interface QuoteDtlXPartNumAfterChange_input{
      /**  Is the part inactive or on hold  */  
   partIsInactiveOrOnHold:boolean,
      /**  Does the part have substitutes  */  
   partHasSubstitutes:boolean,
      /**  Unit of measure code  */  
   uomCode:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteDtlXPartNumAfterChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface QuoteHedCustomerCustIDAfterChange_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteHedCustomerCustIDAfterChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param salesRepCode
      @param ds
   */  
export interface QuoteHedSalesRepCodeChanging_input{
      /**  Proposed sales rep code  */  
   salesRepCode:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteHedSalesRepCodeChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param partNum
   */  
export interface QuotePartNumHasSubstitutes_input{
      /**  Part Number to be evaluated  */  
   partNum:string,
}

export interface QuotePartNumHasSubstitutes_output{
   returnObj:boolean,
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param qtyNum
      @param markupType
      @param ds
   */  
export interface QuoteQtyMaterialMarkupChanged_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote line  */  
   quoteLine:number,
      /**  Quote quantity number  */  
   qtyNum:number,
      /**  (M)aterial, (P)rofit  */  
   markupType:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteQtyMaterialMarkupChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param qtyNum
      @param ds
   */  
export interface QuoteQtyPercentTypeChanged_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Quote Quantity number  */  
   qtyNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteQtyPercentTypeChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param qtyNum
      @param ds
   */  
export interface QuoteQtyValidateAndRecalcWorksheet_input{
      /**  Quote number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Quote Quantity number  */  
   qtyNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface QuoteQtyValidateAndRecalcWorksheet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param iQuoteNum
      @param iQuoteLine
   */  
export interface RecalcKitPriceAfterConfig_input{
      /**  Quote Number for configured part  */  
   iQuoteNum:number,
      /**  Quote Line for configured part  */  
   iQuoteLine:number,
}

export interface RecalcKitPriceAfterConfig_output{
}

   /** Required : 
      @param pCompany
      @param pQuoteNum
      @param parentLine
   */  
export interface RecalcKitPricing_input{
   pCompany:string,
   pQuoteNum:number,
   parentLine:number,
}

export interface RecalcKitPricing_output{
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param qtyNum
      @param ds
   */  
export interface RecalcWorksheet_input{
      /**  Quote Num  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Quote Qty Number  */  
   qtyNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface RecalcWorksheet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteHedDiscountPercent
      @param ds
   */  
export interface RecalculateLineDiscounts_input{
      /**  The quote header discount percent  */  
   quoteHedDiscountPercent:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface RecalculateLineDiscounts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param iPartNum
      @param quoteNum
      @param quoteLine
      @param ds
   */  
export interface RemoveKitComponents_input{
      /**  Parent Sales Kit number  */  
   iPartNum:string,
      /**  Quote number of the QuoteDtl record (0 if an Order is being processed)  */  
   quoteNum:number,
      /**  Quote Line of the QuoteDtl record (0 if an Order is being processed  */  
   quoteLine:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface RemoveKitComponents_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param partNum
      @param revision
   */  
export interface RequestEngineeringExternalMESValidation_input{
   quoteNum:number,
   quoteLine:number,
   partNum:string,
   revision:string,
}

export interface RequestEngineeringExternalMESValidation_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface SetDiscountAmountOverride_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface SetDiscountAmountOverride_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param kbConfigProdID
      @param assemblySeq
   */  
export interface SetKBMaxConfigProdID_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  CPQ Quote Product ID  */  
   kbConfigProdID:number,
      /**  Assembly sequence  */  
   assemblySeq:number,
}

export interface SetKBMaxConfigProdID_output{
}

   /** Required : 
      @param quoteNum
      @param setReqShipDt
      @param setOrdQty
      @param reqShipDate
   */  
export interface SetOrderDefaults_input{
      /**  The current QuoteHed.QuoteNum field  */  
   quoteNum:number,
      /**  Yes to set the QuoteDtl.ReqShipDate to the specified date  */  
   setReqShipDt:boolean,
      /**  Yes to set the Order Qty equal to the Expected Qty  */  
   setOrdQty:boolean,
      /**  Requested Ship Date  */  
   reqShipDate:string,
}

export interface SetOrderDefaults_output{
   returnObj:Erp_Tablesets_QuoteTableset[],
}

   /** Required : 
      @param ipQuoteNum
      @param UserIntiatedCall
      @param ds
   */  
export interface SetReadyToCalc_input{
      /**  The Quote Number  */  
   ipQuoteNum:number,
      /**  Indicates if the user initiated the tax calculation.  */  
   UserIntiatedCall:boolean,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface SetReadyToCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
      @param ds
   */  
export interface UpdateCosts_input{
      /**  The current QuoteQty.QuoteNum field  */  
   quoteNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface UpdateCosts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtQuoteTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtQuoteTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param assemblySeq
      @param configuredProductJson
   */  
export interface UpdateKBMaxConfigurator_input{
      /**  Quote Number  */  
   quoteNum:number,
      /**  Quote Line  */  
   quoteLine:number,
      /**  Assembly sequence  */  
   assemblySeq:number,
      /**  CPQ Configurator data passed from the embed API  */  
   configuredProductJson:string,
}

export interface UpdateKBMaxConfigurator_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipQuoteNum
      @param ipQuoteLine
   */  
export interface ValReqRefDes_input{
      /**  Quote Number to validate  */  
   ipQuoteNum:number,
      /**  Quote Line of the Quote Number to validate  */  
   ipQuoteLine:number,
}

export interface ValReqRefDes_output{
}

   /** Required : 
      @param customerID
      @param ds
   */  
export interface ValidateECCType_input{
      /**  Proposed customer ID  */  
   customerID:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ValidateECCType_output{
parameters : {
      /**  output parameters  */  
   message:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ds
      @param manualValidation
      @param hmrcFraudPrevHeader
   */  
export interface ValidateOTSTaxID_input{
   ds:Erp_Tablesets_QuoteTableset[],
   manualValidation:boolean,
   hmrcFraudPrevHeader:string,
}

export interface ValidateOTSTaxID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
   opMessage:string,
}
}

export interface ValidateOTS_output{
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param qtyNum
      @param ds
   */  
export interface ValidateProfits_input{
   quoteNum:number,
   quoteLine:number,
   qtyNum:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ValidateProfits_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param partNum
      @param sellingExpectedUM
      @param attributeValueSeq
      @param ds
   */  
export interface ValidateQuantityUOMQuoteDtlAttribute_input{
      /**  PartNum  */  
   partNum:string,
      /**  Selling Expected UOM  */  
   sellingExpectedUM:string,
      /**  Attribute Value Sequence  */  
   attributeValueSeq:number,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ValidateQuantityUOMQuoteDtlAttribute_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param quoteNum
   */  
export interface ValidateSOCreate_input{
      /**  The quote number  */  
   quoteNum:number,
}

export interface ValidateSOCreate_output{
parameters : {
      /**  output parameters  */  
   returnMessage:string,
}
}

   /** Required : 
      @param proposedDate
      @param dateColumnName
      @param dateColumnTable
      @param ds
   */  
export interface ValidateShippingDate_input{
      /**  New date to be validated  */  
   proposedDate:string,
      /**  The column the proposed date is from  */  
   dateColumnName:string,
      /**  The table that the validating date belongs to  */  
   dateColumnTable:string,
   ds:Erp_Tablesets_QuoteTableset[],
}

export interface ValidateShippingDate_output{
parameters : {
      /**  output parameters  */  
   invalidDateMessage:string,
   ds:Erp_Tablesets_QuoteTableset[],
}
}

   /** Required : 
      @param ipTaskSetId
      @param ipActiveTaskID
   */  
export interface ValidateTaskSet_input{
      /**  Task Set Id to validate  */  
   ipTaskSetId:string,
      /**  Active Task Id  */  
   ipActiveTaskID:string,
}

export interface ValidateTaskSet_output{
}

export interface WhatIfGetDate_output{
parameters : {
      /**  output parameters  */  
   schedDate:string,
}
}

   /** Required : 
      @param quoteNum
      @param quoteLine
      @param prodQty
      @param schedDate
      @param schedFinite
      @param considerLeadTime
   */  
export interface WhatIfScheduling_input{
   quoteNum:number,
   quoteLine:number,
   prodQty:number,
   schedDate:string,
   schedFinite:boolean,
   considerLeadTime:boolean,
}

export interface WhatIfScheduling_output{
parameters : {
      /**  output parameters  */  
   completionDate:string,
   isProdQtyAvailable:boolean,
}
}

export interface prjWBSPhaseDefinitionIsAllowed_output{
   returnObj:boolean,
}

