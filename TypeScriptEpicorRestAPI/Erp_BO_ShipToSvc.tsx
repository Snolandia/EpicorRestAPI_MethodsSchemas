import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ShipToSvc
// Description: Business Object for ShipTo.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/$metadata", {
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
   Description: Get ShipToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipToes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToRow
   */  
export function get_ShipToes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipToes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipToes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes", {
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
   Summary: Calls GetByID to retrieve the ShipTo item
   Description: Calls GetByID to retrieve the ShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToRow
   */  
export function get_ShipToes_Company_CustNum_ShipToNum(Company:string, CustNum:string, ShipToNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipTo for the service
   Description: Calls UpdateExt to update ShipTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipToes_Company_CustNum_ShipToNum(Company:string, CustNum:string, ShipToNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")", {
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
   Summary: Call UpdateExt to delete ShipTo item
   Description: Call UpdateExt to delete ShipTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipToes_Company_CustNum_ShipToNum(Company:string, CustNum:string, ShipToNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")", {
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
   Description: Get ShipToLabExpRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipToLabExpRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToLabExpRateRow
   */  
export function get_ShipToes_Company_CustNum_ShipToNum_ShipToLabExpRates(Company:string, CustNum:string, ShipToNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToLabExpRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipToLabExpRate item
   Description: Calls GetByID to retrieve the ShipToLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToLabExpRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   */  
export function get_ShipToes_Company_CustNum_ShipToNum_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company:string, CustNum:string, ShipToNum:string, ExpenseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipToLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipToLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipToAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipToAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToAttchRow
   */  
export function get_ShipToes_Company_CustNum_ShipToNum_ShipToAttches(Company:string, CustNum:string, ShipToNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipToAttch item
   Description: Calls GetByID to retrieve the ShipToAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   */  
export function get_ShipToes_Company_CustNum_ShipToNum_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipToAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipToAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ShipToLabExpRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipToLabExpRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToLabExpRateRow
   */  
export function get_ShipToLabExpRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipToLabExpRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipToLabExpRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates", {
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
   Summary: Calls GetByID to retrieve the ShipToLabExpRate item
   Description: Calls GetByID to retrieve the ShipToLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   */  
export function get_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company:string, CustNum:string, ShipToNum:string, ExpenseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipToLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipToLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipToLabExpRate for the service
   Description: Calls UpdateExt to update ShipToLabExpRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipToLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company:string, CustNum:string, ShipToNum:string, ExpenseCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")", {
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
   Summary: Call UpdateExt to delete ShipToLabExpRate item
   Description: Call UpdateExt to delete ShipToLabExpRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipToLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company:string, CustNum:string, ShipToNum:string, ExpenseCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")", {
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
   Description: Get ShipToAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipToAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToAttchRow
   */  
export function get_ShipToAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipToAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipToAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches", {
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
   Summary: Calls GetByID to retrieve the ShipToAttch item
   Description: Calls GetByID to retrieve the ShipToAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   */  
export function get_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipToAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipToAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipToAttch for the service
   Description: Calls UpdateExt to update ShipToAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipToAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ShipToAttch item
   Description: Call UpdateExt to delete ShipToAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipToAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseShipTo:string, whereClauseShipToAttch:string, whereClauseShipToLabExpRate:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseShipTo!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipTo=" + whereClauseShipTo
   }
   if(typeof whereClauseShipToAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipToAttch=" + whereClauseShipToAttch
   }
   if(typeof whereClauseShipToLabExpRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipToLabExpRate=" + whereClauseShipToLabExpRate
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(custNum:string, shipToNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
   }
   if(typeof shipToNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "shipToNum=" + shipToNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetByID" + params, {
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
   Summary: Invoke method GetListFilterCustomer
   Description: Filter ShipTo by Customer.  Call normal GetList method.
   OperationID: GetListFilterCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFilterCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFilterCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetListFilterCustomer", {
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
   Summary: Invoke method GetNewShipTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetNewShipTo", {
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
   Summary: Invoke method GetNewShipToAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipToAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipToAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipToAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipToAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetNewShipToAttch", {
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
   Summary: Invoke method GetNewShipToLabExpRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipToLabExpRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipToLabExpRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipToLabExpRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipToLabExpRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetNewShipToLabExpRate", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipToAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToLabExpRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipToLabExpRateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipToListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipToRow[],
}

export interface Erp_Tablesets_ShipToAttchRow{
   "Company":string,
   "CustNum":number,
   "ShipToNum":string,
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

export interface Erp_Tablesets_ShipToLabExpRateRow{
      /**  Company  */  
   "Company":string,
      /**  CustNum  */  
   "CustNum":number,
      /**  ShipToNum  */  
   "ShipToNum":string,
      /**  ExpenseCode  */  
   "ExpenseCode":string,
      /**  RateType  */  
   "RateType":number,
      /**  RateMultiplier  */  
   "RateMultiplier":number,
      /**  FixedRate  */  
   "FixedRate":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "ShipToShipToNum":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipToListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   "CustNum":number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   "ShipToNum":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   "Name":string,
      /**  The first line of the ShipTo address.  */  
   "Address1":string,
      /**  The second line of the ShipTo address.  */  
   "Address2":string,
      /**  The third line of the ShipTo address.  */  
   "Address3":string,
      /**  The city portion of the ShipTo address.  */  
   "City":string,
      /**  The state or province portion of the ShipTo address.  */  
   "State":string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   "ZIP":string,
      /**  The country portion of the ShipTo address.  */  
   "Country":string,
      /**  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  */  
   "ResaleID":string,
      /**  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  */  
   "SalesRepCode":string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   "TerritoryID":string,
      /**  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  */  
   "ShipViaCode":string,
      /**  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  */  
   "PrimSCon":number,
      /**  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "FaxNum":string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   "TaxExempt":string,
      /**  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  */  
   "EDIShipNum":string,
      /**  The Country.CountryNum value of the country selected in the ShipTo.Country field.  */  
   "CountryNum":number,
      /**  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional custom address format for the ShipTo location.  */  
   "FormatStr":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   "TaxRegionCode":string,
      /**  The email address of the ShipTo location.  */  
   "EMailAddress":string,
      /**   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  */  
   "TerritorySelect":string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   "PendingTerritoryID":string,
      /**  Determines whether or not the ShipTo record was created by an EDI transaction.  */  
   "CreatedByEDI":boolean,
      /**  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  */  
   "ExternalID":string,
      /**  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  */  
   "TaxAuthorityCode":string,
      /**  Disable this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   "DemandDeliveryDays":number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   "DemandDateType":string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   "DemandAddLeadTime":number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandAddAction":string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   "DemandChangeLeadTime":number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeAction":string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   "DemandCancelLeadTime":number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandCancelAction":string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   "DemandNewLineLeadTime":number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandNewLineAction":string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   "DemandQtyChangeLeadTime":number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandQtyChangeAction":string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   "DemandChangeDateLeadTime":number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeDateAction":string,
      /**  The trading partner name.  */  
   "TradingPartnerName":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   "PeriodicityCode":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  */  
   "OverrideCarrier":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  */  
   "OverrideService":boolean,
      /**  Indicates if the demand fields from the customer should be used.  */  
   "DemandUseCustomerValues":boolean,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "EarlyBuffer":number,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "LateBuffer":number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   "DemandUnitPriceDiff":boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   "DemandUnitPriceDiffAction":string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   "ExcFromVal":boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   "AddressVal":boolean,
      /**  Check for the part in the Part master.  */  
   "DemandCheckForPart":boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   "DemandCheckForPartAction":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Individual Pack IDs  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Third address line  */  
   "FFCountryNum":number,
      /**  Additional Handling flag  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Non Standard Packaging  */  
   "AddlHdlgFlag":boolean,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View From Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Freight Forwarder Country portion of the address  */  
   "FFAddress3":string,
      /**  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  */  
   "ETCAddrChg":boolean,
      /**  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  */  
   "IsAlternate":boolean,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterCustNum":number,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterShipToNum":string,
      /**  Check for Revision  */  
   "DemandCheckForRev":boolean,
      /**  Check for Revision Action  */  
   "DemandCheckForRevAction":string,
      /**  Flag for checking partial Shipment for Demand Entry.  */  
   "DemandCheckPartialShip":boolean,
      /**  Check Partial Shipments Action: B =Stop  and W = Warning  */  
   "DemandCheckShipAction":string,
      /**  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  */  
   "DemandCloseRejSkd":boolean,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   "DemandPricing":string,
      /**  Defines the tolerance for price difference validations  */  
   "PriceTolerance":number,
      /**  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  */  
   "CheckDateCapPromise":boolean,
      /**  Confirm or not the Capable to Promise jobs from Demand Entry  */  
   "CheckConfirmCapPromise":boolean,
      /**  If checked, Updates the date in Demand Entry  */  
   "CheckUpdateCapPromise":boolean,
      /**  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  */  
   "DemandCapPromiseDate":string,
      /**  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  */  
   "DemandCapPromiseAction":string,
      /**   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  */  
   "DemandCapPromiseUpdate":string,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   "OTSmartString":boolean,
      /**  Full Legal name  */  
   "LegalName":string,
      /**  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  */  
   "DemandCheckConfig":boolean,
      /**  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  */  
   "DemandCheckCfgAction":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Address in formatted delimited list  */  
   "AddrList":string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   "ContactName":string,
      /**  Display Format String  */  
   "DspFormatStr":string,
      /**  Use this field to display/update; replaces TerritorySelect  */  
   "TerrSelectFlag":string,
   "TerritorySelectDescription":string,
      /**  List of available Periodicity values  */  
   "PeriodicityList":string,
      /**  Indicates Integration with financial package (like EuroFin)  */  
   "IntegrationFlag":boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  */  
   "GlbLink":string,
      /**  Indicates if ShipTo is Global (Master or Linked)  */  
   "GlbFlag":boolean,
      /**  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  */  
   "PrimaryShipTo":boolean,
   "PeriodicityDesc":string,
   "CustID":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  Language Name Description  */  
   "LanguageDescription":string,
      /**  The full name of the customer.  */  
   "MasterCustIDName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "MasterCustIDBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "MasterCustIDCustID":string,
      /**  Name  */  
   "SalesRepName":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaWebDesc":string,
      /**  Long Description of the tax authority code.  */  
   "TATaxAuthorityDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionDescription":string,
      /**  Description of the territory.  */  
   "TerritoryTerritoryDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipToRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   "CustNum":number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   "ShipToNum":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   "Name":string,
      /**  The first line of the ShipTo address.  */  
   "Address1":string,
      /**  The second line of the ShipTo address.  */  
   "Address2":string,
      /**  The third line of the ShipTo address.  */  
   "Address3":string,
      /**  The city portion of the ShipTo address.  */  
   "City":string,
      /**  The state or province portion of the ShipTo address.  */  
   "State":string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   "ZIP":string,
      /**  The country portion of the ShipTo address.  */  
   "Country":string,
      /**  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  */  
   "ResaleID":string,
      /**  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  */  
   "SalesRepCode":string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   "TerritoryID":string,
      /**  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  */  
   "ShipViaCode":string,
      /**  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  */  
   "PrimSCon":number,
      /**  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "FaxNum":string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   "TaxExempt":string,
      /**  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  */  
   "EDIShipNum":string,
      /**  The Country.CountryNum value of the country selected in the ShipTo.Country field.  */  
   "CountryNum":number,
      /**  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional custom address format for the ShipTo location.  */  
   "FormatStr":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   "TaxRegionCode":string,
      /**  The email address of the ShipTo location.  */  
   "EMailAddress":string,
      /**   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  */  
   "TerritorySelect":string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   "PendingTerritoryID":string,
      /**  Determines whether or not the ShipTo record was created by an EDI transaction.  */  
   "CreatedByEDI":boolean,
      /**  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  */  
   "ExternalID":string,
      /**  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  */  
   "TaxAuthorityCode":string,
      /**  Disable this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   "DemandDeliveryDays":number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   "DemandDateType":string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   "DemandAddLeadTime":number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandAddAction":string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   "DemandChangeLeadTime":number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeAction":string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   "DemandCancelLeadTime":number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandCancelAction":string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   "DemandNewLineLeadTime":number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandNewLineAction":string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   "DemandQtyChangeLeadTime":number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandQtyChangeAction":string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   "DemandChangeDateLeadTime":number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeDateAction":string,
      /**  The trading partner name.  */  
   "TradingPartnerName":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   "PeriodicityCode":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  */  
   "OverrideCarrier":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  */  
   "OverrideService":boolean,
      /**  Indicates if the demand fields from the customer should be used.  */  
   "DemandUseCustomerValues":boolean,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "EarlyBuffer":number,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "LateBuffer":number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   "DemandUnitPriceDiff":boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   "DemandUnitPriceDiffAction":string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   "ExcFromVal":boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   "AddressVal":boolean,
      /**  Check for the part in the Part master.  */  
   "DemandCheckForPart":boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   "DemandCheckForPartAction":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Individual Pack IDs  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Third address line  */  
   "FFCountryNum":number,
      /**  Additional Handling flag  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Non Standard Packaging  */  
   "AddlHdlgFlag":boolean,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View From Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Freight Forwarder Country portion of the address  */  
   "FFAddress3":string,
      /**  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  */  
   "ETCAddrChg":boolean,
      /**  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  */  
   "IsAlternate":boolean,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterCustNum":number,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterShipToNum":string,
      /**  Check for Revision  */  
   "DemandCheckForRev":boolean,
      /**  Check for Revision Action  */  
   "DemandCheckForRevAction":string,
      /**  Flag for checking partial Shipment for Demand Entry.  */  
   "DemandCheckPartialShip":boolean,
      /**  Check Partial Shipments Action: B =Stop  and W = Warning  */  
   "DemandCheckShipAction":string,
      /**  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  */  
   "DemandCloseRejSkd":boolean,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   "DemandPricing":string,
      /**  Defines the tolerance for price difference validations  */  
   "PriceTolerance":number,
      /**  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  */  
   "CheckDateCapPromise":boolean,
      /**  Confirm or not the Capable to Promise jobs from Demand Entry  */  
   "CheckConfirmCapPromise":boolean,
      /**  If checked, Updates the date in Demand Entry  */  
   "CheckUpdateCapPromise":boolean,
      /**  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  */  
   "DemandCapPromiseDate":string,
      /**  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  */  
   "DemandCapPromiseAction":string,
      /**   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  */  
   "DemandCapPromiseUpdate":string,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   "OTSmartString":boolean,
      /**  Full Legal name  */  
   "LegalName":string,
      /**  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  */  
   "DemandCheckConfig":boolean,
      /**  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  */  
   "DemandCheckCfgAction":string,
      /**  WIWebShipTo  */  
   "WIWebShipTo":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGApartment  */  
   "AGApartment":string,
      /**  AGExtraStreetNumber  */  
   "AGExtraStreetNumber":string,
      /**  AGFloor  */  
   "AGFloor":string,
      /**  AGGrossIncomeTaxID  */  
   "AGGrossIncomeTaxID":string,
      /**  AGLocationCode  */  
   "AGLocationCode":string,
      /**  AGNeighborhood  */  
   "AGNeighborhood":string,
      /**  AGProvinceCode  */  
   "AGProvinceCode":string,
      /**  AGStreet  */  
   "AGStreet":string,
      /**  AGStreetNumber  */  
   "AGStreetNumber":string,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  Check if the part is a run out part.  */  
   "DemandCheckForRunOutPart":boolean,
      /**  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  */  
   "DemandCheckForRunOutPartAction":string,
      /**  INExciseRegNumber  */  
   "INExciseRegNumber":string,
      /**  INVATNumber  */  
   "INVATNumber":string,
      /**  INSTRegistration  */  
   "INSTRegistration":string,
      /**  MXCURP  */  
   "MXCURP":string,
      /**  MXMunicipio  */  
   "MXMunicipio":string,
      /**  MXFederalID  */  
   "MXFederalID":string,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  Geographical Location Code  */  
   "PEUBIGEOCode":string,
      /**  EORI Number  */  
   "EORINumber":string,
      /**  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  */  
   "TaxValidationStatus":number,
      /**  Tax Validation Date  */  
   "TaxValidationDate":string,
      /**  HMRCTaxValidationLog  */  
   "HMRCTaxValidationLog":string,
      /**  Indicates if the record is inactive.  */  
   "Inactive":boolean,
      /**  FSMRegionCode  */  
   "FSMRegionCode":string,
      /**  FSMArea  */  
   "FSMArea":string,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   "ContactName":string,
      /**  Display Format String  */  
   "DspFormatStr":string,
      /**  Indicates if ShipTo is Global (Master or Linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  */  
   "GlbLink":string,
      /**  Indicates Integration with financial package (like EuroFin)  */  
   "IntegrationFlag":boolean,
      /**  Flag used for integrations whether to run the on change country logic.  */  
   "IntRunChangeCountry":boolean,
   "PeriodicityDesc":string,
      /**  List of available Periodicity values  */  
   "PeriodicityList":string,
      /**  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  */  
   "PrimaryShipTo":boolean,
      /**  Sales Tax ID  */  
   "SalesTaxID":string,
      /**  Service Tax ID  */  
   "ServiceTaxID":string,
   "TerritorySelectDescription":string,
      /**  Use this field to display/update; replaces TerritorySelect  */  
   "TerrSelectFlag":string,
      /**  Address in formatted delimited list  */  
   "AddrList":string,
   "LanguageDescription":string,
   "BitFlag":number,
   "AGLocationDescription":string,
   "AGProvinceDescription":string,
   "CountryISOCode":string,
   "CountryEUMember":boolean,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "DeliveryTypeDescription":string,
   "MasterCustIDBTName":string,
   "MasterCustIDCustID":string,
   "MasterCustIDName":string,
   "SalesRepName":string,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
   "TATaxAuthorityDescription":string,
   "TaxRegionDescription":string,
   "TerritoryTerritoryDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param custNum
      @param shipToNum
   */  
export interface DeleteByID_input{
   custNum:number,
   shipToNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ShipToAttchRow{
   Company:string,
   CustNum:number,
   ShipToNum:string,
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

export interface Erp_Tablesets_ShipToLabExpRateRow{
      /**  Company  */  
   Company:string,
      /**  CustNum  */  
   CustNum:number,
      /**  ShipToNum  */  
   ShipToNum:string,
      /**  ExpenseCode  */  
   ExpenseCode:string,
      /**  RateType  */  
   RateType:number,
      /**  RateMultiplier  */  
   RateMultiplier:number,
      /**  FixedRate  */  
   FixedRate:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   ShipToShipToNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipToListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   ShipToNum:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   Name:string,
      /**  The first line of the ShipTo address.  */  
   Address1:string,
      /**  The second line of the ShipTo address.  */  
   Address2:string,
      /**  The third line of the ShipTo address.  */  
   Address3:string,
      /**  The city portion of the ShipTo address.  */  
   City:string,
      /**  The state or province portion of the ShipTo address.  */  
   State:string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   ZIP:string,
      /**  The country portion of the ShipTo address.  */  
   Country:string,
      /**  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  */  
   ResaleID:string,
      /**  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  */  
   SalesRepCode:string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   TerritoryID:string,
      /**  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  */  
   ShipViaCode:string,
      /**  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  */  
   PrimSCon:number,
      /**  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   FaxNum:string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   TaxExempt:string,
      /**  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  */  
   EDIShipNum:string,
      /**  The Country.CountryNum value of the country selected in the ShipTo.Country field.  */  
   CountryNum:number,
      /**  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional custom address format for the ShipTo location.  */  
   FormatStr:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   TaxRegionCode:string,
      /**  The email address of the ShipTo location.  */  
   EMailAddress:string,
      /**   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  */  
   TerritorySelect:string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   PendingTerritoryID:string,
      /**  Determines whether or not the ShipTo record was created by an EDI transaction.  */  
   CreatedByEDI:boolean,
      /**  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  */  
   ExternalID:string,
      /**  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  */  
   TaxAuthorityCode:string,
      /**  Disable this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   DemandDeliveryDays:number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   DemandDateType:string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   DemandAddLeadTime:number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandAddAction:string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   DemandChangeLeadTime:number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeAction:string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   DemandCancelLeadTime:number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandCancelAction:string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   DemandNewLineLeadTime:number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandNewLineAction:string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   DemandQtyChangeLeadTime:number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandQtyChangeAction:string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   DemandChangeDateLeadTime:number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeDateAction:string,
      /**  The trading partner name.  */  
   TradingPartnerName:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   PeriodicityCode:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  */  
   OverrideCarrier:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  */  
   OverrideService:boolean,
      /**  Indicates if the demand fields from the customer should be used.  */  
   DemandUseCustomerValues:boolean,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   DemandUnitPriceDiff:boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   DemandUnitPriceDiffAction:string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   ExcFromVal:boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   AddressVal:boolean,
      /**  Check for the part in the Part master.  */  
   DemandCheckForPart:boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   DemandCheckForPartAction:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Individual Pack IDs  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Third address line  */  
   FFCountryNum:number,
      /**  Additional Handling flag  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Non Standard Packaging  */  
   AddlHdlgFlag:boolean,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View From Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Freight Forwarder Country portion of the address  */  
   FFAddress3:string,
      /**  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  */  
   ETCAddrChg:boolean,
      /**  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  */  
   IsAlternate:boolean,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterCustNum:number,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterShipToNum:string,
      /**  Check for Revision  */  
   DemandCheckForRev:boolean,
      /**  Check for Revision Action  */  
   DemandCheckForRevAction:string,
      /**  Flag for checking partial Shipment for Demand Entry.  */  
   DemandCheckPartialShip:boolean,
      /**  Check Partial Shipments Action: B =Stop  and W = Warning  */  
   DemandCheckShipAction:string,
      /**  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  */  
   DemandCloseRejSkd:boolean,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   DemandPricing:string,
      /**  Defines the tolerance for price difference validations  */  
   PriceTolerance:number,
      /**  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  */  
   CheckDateCapPromise:boolean,
      /**  Confirm or not the Capable to Promise jobs from Demand Entry  */  
   CheckConfirmCapPromise:boolean,
      /**  If checked, Updates the date in Demand Entry  */  
   CheckUpdateCapPromise:boolean,
      /**  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  */  
   DemandCapPromiseDate:string,
      /**  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  */  
   DemandCapPromiseAction:string,
      /**   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  */  
   DemandCapPromiseUpdate:string,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   OTSmartString:boolean,
      /**  Full Legal name  */  
   LegalName:string,
      /**  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  */  
   DemandCheckConfig:boolean,
      /**  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  */  
   DemandCheckCfgAction:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Address in formatted delimited list  */  
   AddrList:string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   ContactName:string,
      /**  Display Format String  */  
   DspFormatStr:string,
      /**  Use this field to display/update; replaces TerritorySelect  */  
   TerrSelectFlag:string,
   TerritorySelectDescription:string,
      /**  List of available Periodicity values  */  
   PeriodicityList:string,
      /**  Indicates Integration with financial package (like EuroFin)  */  
   IntegrationFlag:boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  */  
   GlbLink:string,
      /**  Indicates if ShipTo is Global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  */  
   PrimaryShipTo:boolean,
   PeriodicityDesc:string,
   CustID:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  Language Name Description  */  
   LanguageDescription:string,
      /**  The full name of the customer.  */  
   MasterCustIDName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   MasterCustIDBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   MasterCustIDCustID:string,
      /**  Name  */  
   SalesRepName:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaWebDesc:string,
      /**  Long Description of the tax authority code.  */  
   TATaxAuthorityDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionDescription:string,
      /**  Description of the territory.  */  
   TerritoryTerritoryDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipToListTableset{
   ShipToList:Erp_Tablesets_ShipToListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ShipToRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   ShipToNum:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   Name:string,
      /**  The first line of the ShipTo address.  */  
   Address1:string,
      /**  The second line of the ShipTo address.  */  
   Address2:string,
      /**  The third line of the ShipTo address.  */  
   Address3:string,
      /**  The city portion of the ShipTo address.  */  
   City:string,
      /**  The state or province portion of the ShipTo address.  */  
   State:string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   ZIP:string,
      /**  The country portion of the ShipTo address.  */  
   Country:string,
      /**  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  */  
   ResaleID:string,
      /**  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  */  
   SalesRepCode:string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   TerritoryID:string,
      /**  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  */  
   ShipViaCode:string,
      /**  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  */  
   PrimSCon:number,
      /**  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   FaxNum:string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   TaxExempt:string,
      /**  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  */  
   EDIShipNum:string,
      /**  The Country.CountryNum value of the country selected in the ShipTo.Country field.  */  
   CountryNum:number,
      /**  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional custom address format for the ShipTo location.  */  
   FormatStr:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   TaxRegionCode:string,
      /**  The email address of the ShipTo location.  */  
   EMailAddress:string,
      /**   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  */  
   TerritorySelect:string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   PendingTerritoryID:string,
      /**  Determines whether or not the ShipTo record was created by an EDI transaction.  */  
   CreatedByEDI:boolean,
      /**  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  */  
   ExternalID:string,
      /**  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  */  
   TaxAuthorityCode:string,
      /**  Disable this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   DemandDeliveryDays:number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   DemandDateType:string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   DemandAddLeadTime:number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandAddAction:string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   DemandChangeLeadTime:number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeAction:string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   DemandCancelLeadTime:number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandCancelAction:string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   DemandNewLineLeadTime:number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandNewLineAction:string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   DemandQtyChangeLeadTime:number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandQtyChangeAction:string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   DemandChangeDateLeadTime:number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeDateAction:string,
      /**  The trading partner name.  */  
   TradingPartnerName:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   PeriodicityCode:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  */  
   OverrideCarrier:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  */  
   OverrideService:boolean,
      /**  Indicates if the demand fields from the customer should be used.  */  
   DemandUseCustomerValues:boolean,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   DemandUnitPriceDiff:boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   DemandUnitPriceDiffAction:string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   ExcFromVal:boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   AddressVal:boolean,
      /**  Check for the part in the Part master.  */  
   DemandCheckForPart:boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   DemandCheckForPartAction:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Individual Pack IDs  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Third address line  */  
   FFCountryNum:number,
      /**  Additional Handling flag  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Non Standard Packaging  */  
   AddlHdlgFlag:boolean,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View From Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Freight Forwarder Country portion of the address  */  
   FFAddress3:string,
      /**  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  */  
   ETCAddrChg:boolean,
      /**  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  */  
   IsAlternate:boolean,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterCustNum:number,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterShipToNum:string,
      /**  Check for Revision  */  
   DemandCheckForRev:boolean,
      /**  Check for Revision Action  */  
   DemandCheckForRevAction:string,
      /**  Flag for checking partial Shipment for Demand Entry.  */  
   DemandCheckPartialShip:boolean,
      /**  Check Partial Shipments Action: B =Stop  and W = Warning  */  
   DemandCheckShipAction:string,
      /**  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  */  
   DemandCloseRejSkd:boolean,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   DemandPricing:string,
      /**  Defines the tolerance for price difference validations  */  
   PriceTolerance:number,
      /**  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  */  
   CheckDateCapPromise:boolean,
      /**  Confirm or not the Capable to Promise jobs from Demand Entry  */  
   CheckConfirmCapPromise:boolean,
      /**  If checked, Updates the date in Demand Entry  */  
   CheckUpdateCapPromise:boolean,
      /**  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  */  
   DemandCapPromiseDate:string,
      /**  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  */  
   DemandCapPromiseAction:string,
      /**   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  */  
   DemandCapPromiseUpdate:string,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   OTSmartString:boolean,
      /**  Full Legal name  */  
   LegalName:string,
      /**  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  */  
   DemandCheckConfig:boolean,
      /**  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  */  
   DemandCheckCfgAction:string,
      /**  WIWebShipTo  */  
   WIWebShipTo:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGApartment  */  
   AGApartment:string,
      /**  AGExtraStreetNumber  */  
   AGExtraStreetNumber:string,
      /**  AGFloor  */  
   AGFloor:string,
      /**  AGGrossIncomeTaxID  */  
   AGGrossIncomeTaxID:string,
      /**  AGLocationCode  */  
   AGLocationCode:string,
      /**  AGNeighborhood  */  
   AGNeighborhood:string,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGStreet  */  
   AGStreet:string,
      /**  AGStreetNumber  */  
   AGStreetNumber:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  Check if the part is a run out part.  */  
   DemandCheckForRunOutPart:boolean,
      /**  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  */  
   DemandCheckForRunOutPartAction:string,
      /**  INExciseRegNumber  */  
   INExciseRegNumber:string,
      /**  INVATNumber  */  
   INVATNumber:string,
      /**  INSTRegistration  */  
   INSTRegistration:string,
      /**  MXCURP  */  
   MXCURP:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  MXFederalID  */  
   MXFederalID:string,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Geographical Location Code  */  
   PEUBIGEOCode:string,
      /**  EORI Number  */  
   EORINumber:string,
      /**  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  */  
   TaxValidationStatus:number,
      /**  Tax Validation Date  */  
   TaxValidationDate:string,
      /**  HMRCTaxValidationLog  */  
   HMRCTaxValidationLog:string,
      /**  Indicates if the record is inactive.  */  
   Inactive:boolean,
      /**  FSMRegionCode  */  
   FSMRegionCode:string,
      /**  FSMArea  */  
   FSMArea:string,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   ContactName:string,
      /**  Display Format String  */  
   DspFormatStr:string,
      /**  Indicates if ShipTo is Global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  */  
   GlbLink:string,
      /**  Indicates Integration with financial package (like EuroFin)  */  
   IntegrationFlag:boolean,
      /**  Flag used for integrations whether to run the on change country logic.  */  
   IntRunChangeCountry:boolean,
   PeriodicityDesc:string,
      /**  List of available Periodicity values  */  
   PeriodicityList:string,
      /**  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  */  
   PrimaryShipTo:boolean,
      /**  Sales Tax ID  */  
   SalesTaxID:string,
      /**  Service Tax ID  */  
   ServiceTaxID:string,
   TerritorySelectDescription:string,
      /**  Use this field to display/update; replaces TerritorySelect  */  
   TerrSelectFlag:string,
      /**  Address in formatted delimited list  */  
   AddrList:string,
   LanguageDescription:string,
   BitFlag:number,
   AGLocationDescription:string,
   AGProvinceDescription:string,
   CountryISOCode:string,
   CountryEUMember:boolean,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   DeliveryTypeDescription:string,
   MasterCustIDBTName:string,
   MasterCustIDCustID:string,
   MasterCustIDName:string,
   SalesRepName:string,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
   TATaxAuthorityDescription:string,
   TaxRegionDescription:string,
   TerritoryTerritoryDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipToTableset{
   ShipTo:Erp_Tablesets_ShipToRow[],
   ShipToAttch:Erp_Tablesets_ShipToAttchRow[],
   ShipToLabExpRate:Erp_Tablesets_ShipToLabExpRateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtShipToTableset{
   ShipTo:Erp_Tablesets_ShipToRow[],
   ShipToAttch:Erp_Tablesets_ShipToAttchRow[],
   ShipToLabExpRate:Erp_Tablesets_ShipToLabExpRateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param custNum
      @param shipToNum
   */  
export interface GetByID_input{
   custNum:number,
   shipToNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ShipToTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ShipToTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ShipToTableset[],
}

   /** Required : 
      @param WhereClause
      @param PageSize
      @param AbsolutePage
   */  
export interface GetListFilterCustomer_input{
      /**  Whereclause.  */  
   WhereClause:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
}

export interface GetListFilterCustomer_output{
   returnObj:Erp_Tablesets_ShipToListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
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
   returnObj:Erp_Tablesets_ShipToListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param custNum
      @param shipToNum
   */  
export interface GetNewShipToAttch_input{
   ds:Erp_Tablesets_ShipToTableset[],
   custNum:number,
   shipToNum:string,
}

export interface GetNewShipToAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShipToTableset[],
}
}

   /** Required : 
      @param ds
      @param custNum
      @param shipToNum
   */  
export interface GetNewShipToLabExpRate_input{
   ds:Erp_Tablesets_ShipToTableset[],
   custNum:number,
   shipToNum:string,
}

export interface GetNewShipToLabExpRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShipToTableset[],
}
}

   /** Required : 
      @param ds
      @param custNum
   */  
export interface GetNewShipTo_input{
   ds:Erp_Tablesets_ShipToTableset[],
   custNum:number,
}

export interface GetNewShipTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShipToTableset[],
}
}

   /** Required : 
      @param whereClauseShipTo
      @param whereClauseShipToAttch
      @param whereClauseShipToLabExpRate
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseShipTo:string,
   whereClauseShipToAttch:string,
   whereClauseShipToLabExpRate:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ShipToTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtShipToTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtShipToTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ShipToTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShipToTableset[],
}
}

