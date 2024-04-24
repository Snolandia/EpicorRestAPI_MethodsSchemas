import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.RFQEntrySvc
// Description: Request for Quote - Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/$metadata", {
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
   Description: Get RFQEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadRow
   */  
export function get_RFQEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQEntries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries", {
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
   Summary: Calls GetByID to retrieve the RFQEntry item
   Description: Calls GetByID to retrieve the RFQEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
   */  
export function get_RFQEntries_Company_RFQNum(Company:string, RFQNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQEntry for the service
   Description: Calls UpdateExt to update RFQEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQEntries_Company_RFQNum(Company:string, RFQNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")", {
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
   Summary: Call UpdateExt to delete RFQEntry item
   Description: Call UpdateExt to delete RFQEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQEntries_Company_RFQNum(Company:string, RFQNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")", {
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
   Description: Get RFQItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQItems1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemRow
   */  
export function get_RFQEntries_Company_RFQNum_RFQItems(Company:string, RFQNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQItem item
   Description: Calls GetByID to retrieve the RFQItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItem1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   */  
export function get_RFQEntries_Company_RFQNum_RFQItems_Company_RFQNum_RFQLine(Company:string, RFQNum:string, RFQLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RFQHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadAttchRow
   */  
export function get_RFQEntries_Company_RFQNum_RFQHeadAttches(Company:string, RFQNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQHeadAttch item
   Description: Calls GetByID to retrieve the RFQHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   */  
export function get_RFQEntries_Company_RFQNum_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company:string, RFQNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RFQItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQItems
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemRow
   */  
export function get_RFQItems(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQItems(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems", {
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
   Summary: Calls GetByID to retrieve the RFQItem item
   Description: Calls GetByID to retrieve the RFQItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItem
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine(Company:string, RFQNum:string, RFQLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQItem for the service
   Description: Calls UpdateExt to update RFQItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQItem
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQItems_Company_RFQNum_RFQLine(Company:string, RFQNum:string, RFQLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")", {
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
   Summary: Call UpdateExt to delete RFQItem item
   Description: Call UpdateExt to delete RFQItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQItem
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQItems_Company_RFQNum_RFQLine(Company:string, RFQNum:string, RFQLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")", {
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
   Description: Get RFQParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQParts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQPartRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQParts(Company:string, RFQNum:string, RFQLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQPart item
   Description: Calls GetByID to retrieve the RFQPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQPart1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company:string, RFQNum:string, RFQLine:string, MfgNum:string, MfgPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RFQQties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQQties1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQQtyRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQQties(Company:string, RFQNum:string, RFQLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQQties", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQQty item
   Description: Calls GetByID to retrieve the RFQQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQQty1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company:string, RFQNum:string, RFQLine:string, QtyNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RFQSourcings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQSourcings1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSourcingRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQSourcings(Company:string, RFQNum:string, RFQLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSourcingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQSourcings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSourcingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQSourcing item
   Description: Calls GetByID to retrieve the RFQSourcing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQSourcing1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param SourcingSeq Desc: SourcingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company:string, RFQNum:string, RFQLine:string, SourcingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQSourcingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQSourcingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RFQVends items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQVends1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQVends(Company:string, RFQNum:string, RFQLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQVends", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQVend item
   Description: Calls GetByID to retrieve the RFQVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQVend1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RFQItemAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQItemAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemAttchRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQItemAttches(Company:string, RFQNum:string, RFQLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQItemAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQItemAttch item
   Description: Calls GetByID to retrieve the RFQItemAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItemAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   */  
export function get_RFQItems_Company_RFQNum_RFQLine_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company:string, RFQNum:string, RFQLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQItemAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQItemAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RFQParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQParts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQPartRow
   */  
export function get_RFQParts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts", {
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
   Summary: Calls GetByID to retrieve the RFQPart item
   Description: Calls GetByID to retrieve the RFQPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   */  
export function get_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company:string, RFQNum:string, RFQLine:string, MfgNum:string, MfgPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQPart for the service
   Description: Calls UpdateExt to update RFQPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company:string, RFQNum:string, RFQLine:string, MfgNum:string, MfgPartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")", {
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
   Summary: Call UpdateExt to delete RFQPart item
   Description: Call UpdateExt to delete RFQPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company:string, RFQNum:string, RFQLine:string, MfgNum:string, MfgPartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")", {
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
   Description: Get RFQQties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQQties
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQQtyRow
   */  
export function get_RFQQties(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQQties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQQties(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties", {
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
   Summary: Calls GetByID to retrieve the RFQQty item
   Description: Calls GetByID to retrieve the RFQQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQQty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   */  
export function get_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company:string, RFQNum:string, RFQLine:string, QtyNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQQtyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQQtyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQQty for the service
   Description: Calls UpdateExt to update RFQQty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQQty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company:string, RFQNum:string, RFQLine:string, QtyNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")", {
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
   Summary: Call UpdateExt to delete RFQQty item
   Description: Call UpdateExt to delete RFQQty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQQty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param QtyNum Desc: QtyNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company:string, RFQNum:string, RFQLine:string, QtyNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")", {
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
   Description: Get RFQSourcings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQSourcings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSourcingRow
   */  
export function get_RFQSourcings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSourcingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSourcingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQSourcings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQSourcings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings", {
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
   Summary: Calls GetByID to retrieve the RFQSourcing item
   Description: Calls GetByID to retrieve the RFQSourcing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQSourcing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param SourcingSeq Desc: SourcingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   */  
export function get_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company:string, RFQNum:string, RFQLine:string, SourcingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQSourcingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQSourcingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQSourcing for the service
   Description: Calls UpdateExt to update RFQSourcing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQSourcing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param SourcingSeq Desc: SourcingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company:string, RFQNum:string, RFQLine:string, SourcingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")", {
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
   Summary: Call UpdateExt to delete RFQSourcing item
   Description: Call UpdateExt to delete RFQSourcing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQSourcing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param SourcingSeq Desc: SourcingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company:string, RFQNum:string, RFQLine:string, SourcingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")", {
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
   Description: Get RFQVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQVends
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendRow
   */  
export function get_RFQVends(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQVends(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends", {
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
   Summary: Calls GetByID to retrieve the RFQVend item
   Description: Calls GetByID to retrieve the RFQVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   */  
export function get_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQVend for the service
   Description: Calls UpdateExt to update RFQVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
   Summary: Call UpdateExt to delete RFQVend item
   Description: Call UpdateExt to delete RFQVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
   Description: Get RFQItemAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQItemAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemAttchRow
   */  
export function get_RFQItemAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQItemAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQItemAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches", {
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
   Summary: Calls GetByID to retrieve the RFQItemAttch item
   Description: Calls GetByID to retrieve the RFQItemAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItemAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   */  
export function get_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company:string, RFQNum:string, RFQLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQItemAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQItemAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQItemAttch for the service
   Description: Calls UpdateExt to update RFQItemAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQItemAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company:string, RFQNum:string, RFQLine:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete RFQItemAttch item
   Description: Call UpdateExt to delete RFQItemAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQItemAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company:string, RFQNum:string, RFQLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")", {
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
   Description: Get RFQHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadAttchRow
   */  
export function get_RFQHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQHeadAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches", {
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
   Summary: Calls GetByID to retrieve the RFQHeadAttch item
   Description: Calls GetByID to retrieve the RFQHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   */  
export function get_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company:string, RFQNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQHeadAttch for the service
   Description: Calls UpdateExt to update RFQHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company:string, RFQNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete RFQHeadAttch item
   Description: Call UpdateExt to delete RFQHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company:string, RFQNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseRFQHead:string, whereClauseRFQHeadAttch:string, whereClauseRFQItem:string, whereClauseRFQItemAttch:string, whereClauseRFQPart:string, whereClauseRFQQty:string, whereClauseRFQSourcing:string, whereClauseRFQVend:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRFQHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQHead=" + whereClauseRFQHead
   }
   if(typeof whereClauseRFQHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQHeadAttch=" + whereClauseRFQHeadAttch
   }
   if(typeof whereClauseRFQItem!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQItem=" + whereClauseRFQItem
   }
   if(typeof whereClauseRFQItemAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQItemAttch=" + whereClauseRFQItemAttch
   }
   if(typeof whereClauseRFQPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQPart=" + whereClauseRFQPart
   }
   if(typeof whereClauseRFQQty!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQQty=" + whereClauseRFQQty
   }
   if(typeof whereClauseRFQSourcing!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQSourcing=" + whereClauseRFQSourcing
   }
   if(typeof whereClauseRFQVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQVend=" + whereClauseRFQVend
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetRows" + params, {
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
export function get_GetByID(rfQNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rfQNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rfQNum=" + rfQNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetList" + params, {
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
   Summary: Invoke method AddRFQItemFromJob
   Description: This method adds RFQItem from Job
   OperationID: AddRFQItemFromJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRFQItemFromJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddRFQItemFromJob", {
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
   Summary: Invoke method AddRFQItemFromMiscReq
   Description: This method adds RFQItem from RFQSugg created from non-job requisitions
   OperationID: AddRFQItemFromMiscReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemFromMiscReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemFromMiscReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRFQItemFromMiscReq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddRFQItemFromMiscReq", {
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
   Summary: Invoke method AddRFQItemFromQuote
   Description: This method adds RFQItem from Qoute
   OperationID: AddRFQItemFromQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemFromQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemFromQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRFQItemFromQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddRFQItemFromQuote", {
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
   Summary: Invoke method AddRFQItemJob
   Description: This method adds RFQItem with SugNumList
   OperationID: AddRFQItemJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRFQItemJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddRFQItemJob", {
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
   Summary: Invoke method AddRFQItemMiscReq
   Description: This method adds RFQItem with SugNumList from non-job related requisitions
   OperationID: AddRFQItemMiscReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemMiscReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemMiscReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRFQItemMiscReq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddRFQItemMiscReq", {
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
   Summary: Invoke method AddRFQItemQuote
   Description: This method adds RFQItem with SugNumList from Qoute
   OperationID: AddRFQItemQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRFQItemQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddRFQItemQuote", {
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
   Summary: Invoke method AddSupplierFromSearch
   Description: Call this method when UI uses Add (search).
   OperationID: AddSupplierFromSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddSupplierFromSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSupplierFromSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddSupplierFromSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddSupplierFromSearch", {
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
   Summary: Invoke method CheckComplianceFail
   Description: Check for every vendor of the RFQ if it requires to be compliant.
   OperationID: CheckComplianceFail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckComplianceFail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckComplianceFail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckComplianceFail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/CheckComplianceFail", {
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
   Summary: Invoke method CreateNewRFQQty
   Description: Create RFQQty record. Please use this method instead of GetNewRFQQty.
   OperationID: CreateNewRFQQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewRFQQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewRFQQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewRFQQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/CreateNewRFQQty", {
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
   Summary: Invoke method DuplicateRFQ
   Description: Duplicates RFQ.
   OperationID: DuplicateRFQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateRFQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateRFQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateRFQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/DuplicateRFQ", {
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
   Summary: Invoke method AddVendorsFromSearch
   Description: Duplicates RFQ.
   OperationID: AddVendorsFromSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddVendorsFromSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddVendorsFromSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddVendorsFromSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/AddVendorsFromSearch", {
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
   Summary: Invoke method GetSourcingStatus
   OperationID: GetSourcingStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourcingStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSourcingStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetSourcingStatus", {
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
   Summary: Invoke method OnChangeofBuyerID
   Description: Call this method when the value of BuyerID changes.
   OperationID: OnChangeofBuyerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofBuyerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofBuyerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofBuyerID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/OnChangeofBuyerID", {
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
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the value of PartNum changes.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/OnChangePartNum", {
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
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/OnChangingRevisionNum", {
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
   Summary: Invoke method OnChangePurPoint
   Description: Call this method when the value of PurPoint changes.
   OperationID: OnChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePurPoint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/OnChangePurPoint", {
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
   Summary: Invoke method OnChangeRFQItemPUM
   Description: Call this method when the value of RFQItem.PUM changes.
   OperationID: OnChangeRFQItemPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRFQItemPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRFQItemPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRFQItemPUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/OnChangeRFQItemPUM", {
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
   Summary: Invoke method OnChangeVendorID
   Description: Call this method when the value of VendorID changes.
   OperationID: OnChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/OnChangeVendorID", {
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
   Summary: Invoke method OpenRFQ
   Description: Close/Open the RFQ.
   OperationID: OpenRFQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenRFQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenRFQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenRFQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/OpenRFQ", {
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
   Summary: Invoke method ReOpenRFQLine
   Description: Reopens the RFQ line.
   OperationID: ReOpenRFQLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReOpenRFQLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReOpenRFQLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReOpenRFQLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/ReOpenRFQLine", {
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
   Summary: Invoke method VendorWizard
   Description: This procedures generates a list of potential Vendors for
the RFQItem.PartNum.
   OperationID: VendorWizard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VendorWizard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VendorWizard_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendorWizard(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/VendorWizard", {
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
   Summary: Invoke method ValidateSelectedVendAttributes
   Description: This procedures called from Kinetic to validate Selected Vendor Attributes
   OperationID: ValidateSelectedVendAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectedVendAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectedVendAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSelectedVendAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/ValidateSelectedVendAttributes", {
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
   Summary: Invoke method ECCUpdateFinal
   Description: Method specific to ECC.
This is used as a final process using the XML that was sent from the Web.
   OperationID: ECCUpdateFinal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECCUpdateFinal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECCUpdateFinal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECCUpdateFinal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/ECCUpdateFinal", {
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
   Summary: Invoke method GetNewRFQHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQHead", {
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
   Summary: Invoke method GetNewRFQHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQHeadAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQHeadAttch", {
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
   Summary: Invoke method GetNewRFQItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQItem(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQItem", {
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
   Summary: Invoke method GetNewRFQItemAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQItemAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQItemAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQItemAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQItemAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQItemAttch", {
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
   Summary: Invoke method GetNewRFQPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQPart", {
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
   Summary: Invoke method GetNewRFQQty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQQty", {
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
   Summary: Invoke method GetNewRFQSourcing
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQSourcing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQSourcing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQSourcing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQSourcing(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQSourcing", {
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
   Summary: Invoke method GetNewRFQVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQVend(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetNewRFQVend", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQHeadAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQItemAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQItemRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQPartRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQQtyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQQtyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSourcingRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQSourcingRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQVendRow[],
}

export interface Erp_Tablesets_RFQHeadAttchRow{
   "Company":string,
   "RFQNum":number,
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

export interface Erp_Tablesets_RFQHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  */  
   "OpenRFQ":boolean,
      /**  Number that uniquely identifies the RFQ document.  */  
   "RFQNum":number,
      /**  Date that this RFQ was entered.  */  
   "RFQDate":string,
      /**  The date the vendor responses are due.  */  
   "RFQDueDate":string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  Contains comments about the RFQ. These will be printed on the RFQ document.  */  
   "CommentText":string,
      /**  Indicates if the RFQ is to selected for printing during the Mass Print process.  */  
   "ReadyToPrint":boolean,
      /**  Date the supplier is to respond by  */  
   "RespondDate":string,
      /**  Date the PO is planned to be awarded  */  
   "DecisionDate":string,
      /**  Indicates the Supplier will respond via Suppliers workbench  */  
   "PostToWeb":boolean,
      /**  Date Buyer posted the RFQ  */  
   "PostDate":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global RFQ identifier.  Used in Consolidated Purchasing.  */  
   "GlbRFQNum":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  UOM Class ID  */  
   "UOMClassID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "WebVendorExists":boolean,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   "BuyerIDName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  */  
   "OpenRFQ":boolean,
      /**  Number that uniquely identifies the RFQ document.  */  
   "RFQNum":number,
      /**  Date that this RFQ was entered.  */  
   "RFQDate":string,
      /**  The date the vendor responses are due.  */  
   "RFQDueDate":string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  Contains comments about the RFQ. These will be printed on the RFQ document.  */  
   "CommentText":string,
      /**  Indicates if the RFQ is to selected for printing during the Mass Print process.  */  
   "ReadyToPrint":boolean,
      /**  Date the supplier is to respond by  */  
   "RespondDate":string,
      /**  Date the PO is planned to be awarded  */  
   "DecisionDate":string,
      /**  Indicates the Supplier will respond via Suppliers workbench  */  
   "PostToWeb":boolean,
      /**  Date Buyer posted the RFQ  */  
   "PostDate":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global RFQ identifier.  Used in Consolidated Purchasing.  */  
   "GlbRFQNum":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  UOM Class ID  */  
   "UOMClassID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "WebVendorExists":boolean,
   "BitFlag":number,
   "BuyerIDName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQItemAttchRow{
   "Company":string,
   "RFQNum":number,
   "RFQLine":number,
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

export interface Erp_Tablesets_RFQItemRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed.  Set to "Closed" as when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   "OpenItem":boolean,
      /**  RFQ number  that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   "LineDesc":string,
      /**  Issue (our) unit of measure.  */  
   "IUM":string,
      /**  OUR internal part number for this item.  */  
   "PartNum":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Contains comments about the item. These will be printed on the RFQ. Defaults from the Job’s Material Purchasing comments.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   "ClassID":string,
      /**  Related job number.  */  
   "JobNum":string,
      /**  Related Customer QuoteNum.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  Mtl = Material, Sub = Subcontract  */  
   "ItemType":string,
      /**   Operation Code - used to identify specific subcontracting operation that is needs to be quoted.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts service).  */  
   "OpCode":string,
      /**  Assembly sequence number that this rfq is associated with.  */  
   "AssemblySeq":number,
      /**  Job Seq of the requirement. Not maintainable.  */  
   "JobSeq":number,
      /**  The number of vendor quotes that are required for this rfq line.  */  
   "RFQVendQuotes":number,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global RFQ identifier.  Used in Consolidated Purchasing.  */  
   "GlbRFQNum":string,
      /**  Global RFQ Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbRFQLine":number,
      /**  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  */  
   "RequiredQty":number,
      /**  Indicates if inspection is required when items are received.  Used when create PODetail records  */  
   "RcvInspectionReq":boolean,
      /**  The warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  Number of quotes required as indicated by the source file  */  
   "SrcVendQuotes":number,
      /**  Indicates if the Source file (JobMtl,QuoteMtl,...) is a valid source record  */  
   "ValidSrc":boolean,
      /**  The Purchase Unit of Measure  */  
   "PUM":string,
      /**  Used to capture the purchasing factor.  */  
   "PurchasingFactor":number,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  UOM Class ID  */  
   "UOMClassID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Requisition number that the detail line is linked to.  */  
   "ReqNum":number,
      /**  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  */  
   "ReqLine":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   "NotCompliant":boolean,
   "Source":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "AttributeSetIDShortDescription":string,
   "AttributeSetIDDescription":string,
   "ClassDescription":string,
   "JobNumPartDescription":string,
   "OpCodeOpDesc":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQPartRow{
      /**  Company  */  
   "Company":string,
      /**  RFQNum  */  
   "RFQNum":number,
      /**  RFQLine  */  
   "RFQLine":number,
      /**  MfgNum  */  
   "MfgNum":number,
      /**  MfgPartNum  */  
   "MfgPartNum":string,
      /**  True if this mfg part should be included on the RFQ, false if it should not be. Defaults to true.  */  
   "RFQInclude":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "MfgNumName":string,
   "MfgNumID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQQtyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Number that uniquely identifies the RFQ document.  */  
   "RFQNum":number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  */  
   "QtyNum":number,
      /**  The quantity for which the RFQ is requesting a quote.  */  
   "Quantity":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Display only field based on RFQItem.PUM  */  
   "DspUOM":string,
   "BitFlag":number,
   "RFQLineLineDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQSourcingRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Number that uniquely identifies the RFQ document.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**  Sequence number used to complete the primary index and in case more than one records get created.  */  
   "SourcingSeq":number,
      /**  ID number that Sorcing retrieves in order to keep track of an auction.  */  
   "SourcingID":string,
      /**  Status of the Auction ( S = Send to Sourcing , P = Posted to Sourcing and Empty, Blank = Available to be sent)  */  
   "SourcingStatus":string,
      /**  Title of the auction  */  
   "AuctionTitle":string,
      /**  An option that restricts the information displayed about the winner of the event.  */  
   "BidAnonimity":string,
      /**  Category in which the items belong  */  
   "Category":string,
      /**  The number of hours that the auction will stay online and open for bids  */  
   "Duration":number,
      /**  Type of Event Auction  */  
   "EventType":string,
      /**  Description of the item that is being sold / bought  */  
   "ItemDescription":string,
      /**  Minimum Offer Decrement. The minimum amount of money that one user can bid over the current price.  */  
   "MinOfferDec":number,
      /**  Preview time is a given time for the users to preview the auction without being able to make bids yet.  */  
   "PreviewDate":string,
      /**  Displays the time at which the auction can be previewed.  */  
   "PreviewTime":number,
      /**  Start date is the date when the auction will be available for users to make bids.  */  
   "StartingDate":string,
      /**  Starting time for the users to be able to make bids.  */  
   "StartingTime":number,
      /**  Expected Total Price  */  
   "ExpectedTotalPrice":number,
      /**  Actual Total Price  */  
   "ActualTotalPrice":number,
      /**  Anonimity Level. Level of restriction for the information displayed about the winner of the event.  */  
   "AnonimityLevel":string,
      /**  Strictly speaking, negative bidding is simply placing a bid using a negative number.  */  
   "NegativeBids":boolean,
      /**  Unit of Measure (used only on Dynamic Descent Events)  */  
   "UOMCode":string,
      /**  When creating a dynamic ascending or dynamic descending event you must enter the number of units you wish to buy or sell.  */  
   "UnitQty":number,
      /**  A rule that can determine how the winner of an event is selected.  */  
   "DecisionMakingRule":string,
      /**  The beginning or opening price of an item or service in a Dutch or reverse Dutch event.  */  
   "StartingPrice":number,
      /**  The highest price a buyer will pay for an evented item.  */  
   "MaxPrice":number,
      /**  Price Increment at each Interval. Used in buyer-centric events, it is the amount by which an event price increases per each interval of time.  */  
   "PriceIncrement":number,
      /**  Time Interval for each Price Increase  */  
   "TimeInterval":number,
      /**  Universal Standard Products and Services Classification (UNSPSC)  */  
   "UNSPSC":string,
      /**  Forms Of Payment  */  
   "FormsOfPayment":string,
      /**  Designates who pays the carrier for the shipping of an item  */  
   "FreeOnBoard":string,
      /**  The payment terms of a posting.  */  
   "Terms":string,
      /**  The various methods of shipping that apply to a posting.  */  
   "ShippingOptions":string,
      /**  The geographic location of an item for sale, or, in the case of an item for purchase, the geographic location where the item should be delivered.  */  
   "Location":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  String representation of the StartingTime field  */  
   "StartingTimeString":string,
      /**  String representation of the Preview Time field  */  
   "PreviewTimeString":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQVendRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   "OpenItem":boolean,
      /**   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  */  
   "Response":string,
      /**  RFQ number  that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Vendor Purchase Point ID.  */  
   "PurPoint":string,
      /**  Supplier contact linked to this RFQ  */  
   "ConNum":number,
      /**  Can be "Web" or "Client"  */  
   "RespondVia":string,
      /**  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  */  
   "RespondDate":string,
      /**  Compliance Message  */  
   "ComplianceMsg":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "VendorID":string,
   "VendorName":string,
   "OpenRFQ":boolean,
   "LineDescription":string,
   "PartNum":string,
   "RevisionNum":string,
   "JobNum":string,
   "QuoteNum":number,
   "OpCode":string,
   "OpDescription":string,
   "ResponseDescription":string,
      /**  Vend Part Effective Date  */  
   "EffectiveDate":string,
      /**  Description of the Source field (either Job, Quote or blank)  */  
   "RFQSource":string,
   "RFQStatus":string,
      /**  Buyer Name  */  
   "BuyerID":string,
   "RFQDate":string,
   "RFQDueDate":string,
      /**  Our UOM  */  
   "OurUOM":string,
      /**  Supplier UOM  */  
   "SupplierUOM":string,
      /**  Base UOM Code from Part Master  */  
   "IUM":string,
      /**  The Purchasing Unit of measure for the Part.  */  
   "PUM":string,
   "CalcOurQty":number,
   "CalcVendQty":number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   "NotCompliant":boolean,
   "Selected":boolean,
      /**  Supplier Address  */  
   "AddressFormatted":string,
      /**  Valid Response options for combo.  */  
   "ResponseOptions":string,
   "AttributeDescription":string,
   "AttributeSetID":number,
   "AttributeShortDescription":string,
   "BitFlag":number,
   "RFQLineLineDesc":string,
   "VendorNumVendorID":string,
   "VendorNumAddress2":string,
   "VendorNumName":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param piRFQNum
      @param pcJobNum
      @param pcGlbCompany
      @param ds
   */  
export interface AddRFQItemFromJob_input{
      /**  RFQ Number  */  
   piRFQNum:number,
      /**  Job Number  */  
   pcJobNum:string,
      /**  GlbCompany Number  */  
   pcGlbCompany:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface AddRFQItemFromJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param piRFQNum
      @param pcGlbCompany
      @param ds
   */  
export interface AddRFQItemFromMiscReq_input{
      /**  RFQ Number  */  
   piRFQNum:number,
      /**  GlbCompany Number  */  
   pcGlbCompany:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface AddRFQItemFromMiscReq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param piRFQNum
      @param piQuoteNum
      @param pcGlbCompany
      @param ds
   */  
export interface AddRFQItemFromQuote_input{
      /**  RFQ Number  */  
   piRFQNum:number,
      /**  Quote Number  */  
   piQuoteNum:number,
      /**  GlbCompany Number  */  
   pcGlbCompany:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface AddRFQItemFromQuote_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param piRFQNum
      @param pcSugNumList
      @param ds
   */  
export interface AddRFQItemJob_input{
      /**  RFQ Number  */  
   piRFQNum:number,
      /**  SugNumList  */  
   pcSugNumList:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface AddRFQItemJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param piRFQNum
      @param pcSugNumList
      @param ds
   */  
export interface AddRFQItemMiscReq_input{
      /**  RFQ Number  */  
   piRFQNum:number,
      /**  SugNumList  */  
   pcSugNumList:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface AddRFQItemMiscReq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param pcSugNumList
      @param piRFQNum
      @param ds
   */  
export interface AddRFQItemQuote_input{
      /**  SugNumList  */  
   pcSugNumList:string,
      /**  RFQ Number  */  
   piRFQNum:number,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface AddRFQItemQuote_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param ds
      @param pcVendorID
      @param pcPurPoint
   */  
export interface AddSupplierFromSearch_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
      /**  VendorID  */  
   pcVendorID:string,
      /**  PurPoint  */  
   pcPurPoint:string,
}

export interface AddSupplierFromSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param vendNumList
      @param vendPPList
      @param rfqNum
      @param rfqLine
   */  
export interface AddVendorsFromSearch_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
      /**  List of Vendor Numbers  */  
   vendNumList:string,
      /**  List of Vendor Purchase Point  */  
   vendPPList:string,
      /**  RFQ Number  */  
   rfqNum:number,
      /**  RFQ Line Number  */  
   rfqLine:number,
}

export interface AddVendorsFromSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param rfqNum
      @param rfqLine
      @param vendorNum
      @param purPoint
   */  
export interface CheckComplianceFail_input{
      /**  Current RFQ.  */  
   rfqNum:number,
      /**  Current RFQ Line.  */  
   rfqLine:number,
      /**  Current Vendor.  */  
   vendorNum:number,
      /**  Current Purchase Point.  */  
   purPoint:string,
}

export interface CheckComplianceFail_output{
parameters : {
      /**  output parameters  */  
   compliant:boolean,
}
}

   /** Required : 
      @param ds
      @param rfqNum
      @param rfqLine
   */  
export interface CreateNewRFQQty_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
      /**  RFQ Number  */  
   rfqNum:number,
      /**  RFQ Line Number  */  
   rfqLine:number,
}

export interface CreateNewRFQQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param rfQNum
   */  
export interface DeleteByID_input{
   rfQNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param piSourceRFQNum
   */  
export interface DuplicateRFQ_input{
      /**  Source RFQ Number  */  
   piSourceRFQNum:number,
}

export interface DuplicateRFQ_output{
   returnObj:Erp_Tablesets_RFQEntryTableset[],
parameters : {
      /**  output parameters  */  
   poNewRFQNum:number,
}
}

   /** Required : 
      @param ds
      @param reqType
      @param xmlDoc
   */  
export interface ECCUpdateFinal_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   reqType:string,
   xmlDoc:string,
}

export interface ECCUpdateFinal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

export interface Erp_Tablesets_RFQEntryTableset{
   RFQHead:Erp_Tablesets_RFQHeadRow[],
   RFQHeadAttch:Erp_Tablesets_RFQHeadAttchRow[],
   RFQItem:Erp_Tablesets_RFQItemRow[],
   RFQItemAttch:Erp_Tablesets_RFQItemAttchRow[],
   RFQPart:Erp_Tablesets_RFQPartRow[],
   RFQQty:Erp_Tablesets_RFQQtyRow[],
   RFQSourcing:Erp_Tablesets_RFQSourcingRow[],
   RFQVend:Erp_Tablesets_RFQVendRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RFQHeadAttchRow{
   Company:string,
   RFQNum:number,
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

export interface Erp_Tablesets_RFQHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  */  
   OpenRFQ:boolean,
      /**  Number that uniquely identifies the RFQ document.  */  
   RFQNum:number,
      /**  Date that this RFQ was entered.  */  
   RFQDate:string,
      /**  The date the vendor responses are due.  */  
   RFQDueDate:string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  Contains comments about the RFQ. These will be printed on the RFQ document.  */  
   CommentText:string,
      /**  Indicates if the RFQ is to selected for printing during the Mass Print process.  */  
   ReadyToPrint:boolean,
      /**  Date the supplier is to respond by  */  
   RespondDate:string,
      /**  Date the PO is planned to be awarded  */  
   DecisionDate:string,
      /**  Indicates the Supplier will respond via Suppliers workbench  */  
   PostToWeb:boolean,
      /**  Date Buyer posted the RFQ  */  
   PostDate:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global RFQ identifier.  Used in Consolidated Purchasing.  */  
   GlbRFQNum:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  UOM Class ID  */  
   UOMClassID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   WebVendorExists:boolean,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   BuyerIDName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQHeadListTableset{
   RFQHeadList:Erp_Tablesets_RFQHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RFQHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  */  
   OpenRFQ:boolean,
      /**  Number that uniquely identifies the RFQ document.  */  
   RFQNum:number,
      /**  Date that this RFQ was entered.  */  
   RFQDate:string,
      /**  The date the vendor responses are due.  */  
   RFQDueDate:string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  Contains comments about the RFQ. These will be printed on the RFQ document.  */  
   CommentText:string,
      /**  Indicates if the RFQ is to selected for printing during the Mass Print process.  */  
   ReadyToPrint:boolean,
      /**  Date the supplier is to respond by  */  
   RespondDate:string,
      /**  Date the PO is planned to be awarded  */  
   DecisionDate:string,
      /**  Indicates the Supplier will respond via Suppliers workbench  */  
   PostToWeb:boolean,
      /**  Date Buyer posted the RFQ  */  
   PostDate:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global RFQ identifier.  Used in Consolidated Purchasing.  */  
   GlbRFQNum:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  UOM Class ID  */  
   UOMClassID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   WebVendorExists:boolean,
   BitFlag:number,
   BuyerIDName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQItemAttchRow{
   Company:string,
   RFQNum:number,
   RFQLine:number,
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

export interface Erp_Tablesets_RFQItemRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed.  Set to "Closed" as when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   OpenItem:boolean,
      /**  RFQ number  that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   LineDesc:string,
      /**  Issue (our) unit of measure.  */  
   IUM:string,
      /**  OUR internal part number for this item.  */  
   PartNum:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Contains comments about the item. These will be printed on the RFQ. Defaults from the Job’s Material Purchasing comments.  */  
   CommentText:string,
      /**  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   ClassID:string,
      /**  Related job number.  */  
   JobNum:string,
      /**  Related Customer QuoteNum.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  Mtl = Material, Sub = Subcontract  */  
   ItemType:string,
      /**   Operation Code - used to identify specific subcontracting operation that is needs to be quoted.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts service).  */  
   OpCode:string,
      /**  Assembly sequence number that this rfq is associated with.  */  
   AssemblySeq:number,
      /**  Job Seq of the requirement. Not maintainable.  */  
   JobSeq:number,
      /**  The number of vendor quotes that are required for this rfq line.  */  
   RFQVendQuotes:number,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global RFQ identifier.  Used in Consolidated Purchasing.  */  
   GlbRFQNum:string,
      /**  Global RFQ Line identifier.  Used in Consolidated Purchasing.  */  
   GlbRFQLine:number,
      /**  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  */  
   RequiredQty:number,
      /**  Indicates if inspection is required when items are received.  Used when create PODetail records  */  
   RcvInspectionReq:boolean,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Number of quotes required as indicated by the source file  */  
   SrcVendQuotes:number,
      /**  Indicates if the Source file (JobMtl,QuoteMtl,...) is a valid source record  */  
   ValidSrc:boolean,
      /**  The Purchase Unit of Measure  */  
   PUM:string,
      /**  Used to capture the purchasing factor.  */  
   PurchasingFactor:number,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  UOM Class ID  */  
   UOMClassID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Requisition number that the detail line is linked to.  */  
   ReqNum:number,
      /**  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  */  
   ReqLine:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   NotCompliant:boolean,
   Source:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   AttributeSetIDShortDescription:string,
   AttributeSetIDDescription:string,
   ClassDescription:string,
   JobNumPartDescription:string,
   OpCodeOpDesc:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackInventoryByRevision:boolean,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQPartRow{
      /**  Company  */  
   Company:string,
      /**  RFQNum  */  
   RFQNum:number,
      /**  RFQLine  */  
   RFQLine:number,
      /**  MfgNum  */  
   MfgNum:number,
      /**  MfgPartNum  */  
   MfgPartNum:string,
      /**  True if this mfg part should be included on the RFQ, false if it should not be. Defaults to true.  */  
   RFQInclude:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   MfgNumName:string,
   MfgNumID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQQtyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Number that uniquely identifies the RFQ document.  */  
   RFQNum:number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  */  
   QtyNum:number,
      /**  The quantity for which the RFQ is requesting a quote.  */  
   Quantity:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Display only field based on RFQItem.PUM  */  
   DspUOM:string,
   BitFlag:number,
   RFQLineLineDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQSourcingRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Number that uniquely identifies the RFQ document.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**  Sequence number used to complete the primary index and in case more than one records get created.  */  
   SourcingSeq:number,
      /**  ID number that Sorcing retrieves in order to keep track of an auction.  */  
   SourcingID:string,
      /**  Status of the Auction ( S = Send to Sourcing , P = Posted to Sourcing and Empty, Blank = Available to be sent)  */  
   SourcingStatus:string,
      /**  Title of the auction  */  
   AuctionTitle:string,
      /**  An option that restricts the information displayed about the winner of the event.  */  
   BidAnonimity:string,
      /**  Category in which the items belong  */  
   Category:string,
      /**  The number of hours that the auction will stay online and open for bids  */  
   Duration:number,
      /**  Type of Event Auction  */  
   EventType:string,
      /**  Description of the item that is being sold / bought  */  
   ItemDescription:string,
      /**  Minimum Offer Decrement. The minimum amount of money that one user can bid over the current price.  */  
   MinOfferDec:number,
      /**  Preview time is a given time for the users to preview the auction without being able to make bids yet.  */  
   PreviewDate:string,
      /**  Displays the time at which the auction can be previewed.  */  
   PreviewTime:number,
      /**  Start date is the date when the auction will be available for users to make bids.  */  
   StartingDate:string,
      /**  Starting time for the users to be able to make bids.  */  
   StartingTime:number,
      /**  Expected Total Price  */  
   ExpectedTotalPrice:number,
      /**  Actual Total Price  */  
   ActualTotalPrice:number,
      /**  Anonimity Level. Level of restriction for the information displayed about the winner of the event.  */  
   AnonimityLevel:string,
      /**  Strictly speaking, negative bidding is simply placing a bid using a negative number.  */  
   NegativeBids:boolean,
      /**  Unit of Measure (used only on Dynamic Descent Events)  */  
   UOMCode:string,
      /**  When creating a dynamic ascending or dynamic descending event you must enter the number of units you wish to buy or sell.  */  
   UnitQty:number,
      /**  A rule that can determine how the winner of an event is selected.  */  
   DecisionMakingRule:string,
      /**  The beginning or opening price of an item or service in a Dutch or reverse Dutch event.  */  
   StartingPrice:number,
      /**  The highest price a buyer will pay for an evented item.  */  
   MaxPrice:number,
      /**  Price Increment at each Interval. Used in buyer-centric events, it is the amount by which an event price increases per each interval of time.  */  
   PriceIncrement:number,
      /**  Time Interval for each Price Increase  */  
   TimeInterval:number,
      /**  Universal Standard Products and Services Classification (UNSPSC)  */  
   UNSPSC:string,
      /**  Forms Of Payment  */  
   FormsOfPayment:string,
      /**  Designates who pays the carrier for the shipping of an item  */  
   FreeOnBoard:string,
      /**  The payment terms of a posting.  */  
   Terms:string,
      /**  The various methods of shipping that apply to a posting.  */  
   ShippingOptions:string,
      /**  The geographic location of an item for sale, or, in the case of an item for purchase, the geographic location where the item should be delivered.  */  
   Location:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  String representation of the StartingTime field  */  
   StartingTimeString:string,
      /**  String representation of the Preview Time field  */  
   PreviewTimeString:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQVendRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   OpenItem:boolean,
      /**   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  */  
   Response:string,
      /**  RFQ number  that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Vendor Purchase Point ID.  */  
   PurPoint:string,
      /**  Supplier contact linked to this RFQ  */  
   ConNum:number,
      /**  Can be "Web" or "Client"  */  
   RespondVia:string,
      /**  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  */  
   RespondDate:string,
      /**  Compliance Message  */  
   ComplianceMsg:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   VendorID:string,
   VendorName:string,
   OpenRFQ:boolean,
   LineDescription:string,
   PartNum:string,
   RevisionNum:string,
   JobNum:string,
   QuoteNum:number,
   OpCode:string,
   OpDescription:string,
   ResponseDescription:string,
      /**  Vend Part Effective Date  */  
   EffectiveDate:string,
      /**  Description of the Source field (either Job, Quote or blank)  */  
   RFQSource:string,
   RFQStatus:string,
      /**  Buyer Name  */  
   BuyerID:string,
   RFQDate:string,
   RFQDueDate:string,
      /**  Our UOM  */  
   OurUOM:string,
      /**  Supplier UOM  */  
   SupplierUOM:string,
      /**  Base UOM Code from Part Master  */  
   IUM:string,
      /**  The Purchasing Unit of measure for the Part.  */  
   PUM:string,
   CalcOurQty:number,
   CalcVendQty:number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   NotCompliant:boolean,
   Selected:boolean,
      /**  Supplier Address  */  
   AddressFormatted:string,
      /**  Valid Response options for combo.  */  
   ResponseOptions:string,
   AttributeDescription:string,
   AttributeSetID:number,
   AttributeShortDescription:string,
   BitFlag:number,
   RFQLineLineDesc:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtRFQEntryTableset{
   RFQHead:Erp_Tablesets_RFQHeadRow[],
   RFQHeadAttch:Erp_Tablesets_RFQHeadAttchRow[],
   RFQItem:Erp_Tablesets_RFQItemRow[],
   RFQItemAttch:Erp_Tablesets_RFQItemAttchRow[],
   RFQPart:Erp_Tablesets_RFQPartRow[],
   RFQQty:Erp_Tablesets_RFQQtyRow[],
   RFQSourcing:Erp_Tablesets_RFQSourcingRow[],
   RFQVend:Erp_Tablesets_RFQVendRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param rfQNum
   */  
export interface GetByID_input{
   rfQNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RFQEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RFQEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RFQEntryTableset[],
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
   returnObj:Erp_Tablesets_RFQHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rfQNum
   */  
export interface GetNewRFQHeadAttch_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   rfQNum:number,
}

export interface GetNewRFQHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRFQHead_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface GetNewRFQHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param rfQNum
      @param rfQLine
   */  
export interface GetNewRFQItemAttch_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   rfQNum:number,
   rfQLine:number,
}

export interface GetNewRFQItemAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param rfQNum
   */  
export interface GetNewRFQItem_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   rfQNum:number,
}

export interface GetNewRFQItem_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param rfQNum
      @param rfQLine
      @param mfgNum
   */  
export interface GetNewRFQPart_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   rfQNum:number,
   rfQLine:number,
   mfgNum:number,
}

export interface GetNewRFQPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param rfQNum
      @param rfQLine
   */  
export interface GetNewRFQQty_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   rfQNum:number,
   rfQLine:number,
}

export interface GetNewRFQQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param rfQNum
      @param rfQLine
   */  
export interface GetNewRFQSourcing_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   rfQNum:number,
   rfQLine:number,
}

export interface GetNewRFQSourcing_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param rfQNum
      @param rfQLine
      @param vendorNum
   */  
export interface GetNewRFQVend_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
   rfQNum:number,
   rfQLine:number,
   vendorNum:number,
}

export interface GetNewRFQVend_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param whereClauseRFQHead
      @param whereClauseRFQHeadAttch
      @param whereClauseRFQItem
      @param whereClauseRFQItemAttch
      @param whereClauseRFQPart
      @param whereClauseRFQQty
      @param whereClauseRFQSourcing
      @param whereClauseRFQVend
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRFQHead:string,
   whereClauseRFQHeadAttch:string,
   whereClauseRFQItem:string,
   whereClauseRFQItemAttch:string,
   whereClauseRFQPart:string,
   whereClauseRFQQty:string,
   whereClauseRFQSourcing:string,
   whereClauseRFQVend:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RFQEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSourcingStatus_output{
parameters : {
      /**  output parameters  */  
   oStatus:boolean,
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
      @param newPart
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  Proposed Part Number  */  
   newPart:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param pcVendorID
      @param pcVendorPP
   */  
export interface OnChangePurPoint_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
      /**  VendorID  */  
   pcVendorID:string,
      /**  VendorPP  */  
   pcVendorPP:string,
}

export interface OnChangePurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPUM
   */  
export interface OnChangeRFQItemPUM_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
      /**  PUM  */  
   ipPUM:string,
}

export interface OnChangeRFQItemPUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param pcVendorID
   */  
export interface OnChangeVendorID_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
      /**  VendorID  */  
   pcVendorID:string,
}

export interface OnChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param piRFQNum
      @param newBuyerID
      @param ds
   */  
export interface OnChangeofBuyerID_input{
      /**  RFQ Number  */  
   piRFQNum:number,
      /**  Buyer ID  */  
   newBuyerID:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface OnChangeofBuyerID_output{
parameters : {
      /**  output parameters  */  
   rtnMessage:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param piRFQNum
      @param piOpenRFQ
   */  
export interface OpenRFQ_input{
      /**  The RFQ number  */  
   piRFQNum:number,
      /**  True/False open RFQ  */  
   piOpenRFQ:boolean,
}

export interface OpenRFQ_output{
   returnObj:Erp_Tablesets_RFQEntryTableset[],
}

   /** Required : 
      @param piRFQNum
      @param piRFQLine
      @param ds
   */  
export interface ReOpenRFQLine_input{
      /**  The RFQ number  */  
   piRFQNum:number,
      /**  The RFQ Line number  */  
   piRFQLine:number,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface ReOpenRFQLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtRFQEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRFQEntryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
}
}

   /** Required : 
      @param inclVendAttrList
      @param exclVendAttrList
   */  
export interface ValidateSelectedVendAttributes_input{
      /**  Included Attributes  */  
   inclVendAttrList:string,
      /**  Excluded Attributes  */  
   exclVendAttrList:string,
}

export interface ValidateSelectedVendAttributes_output{
   returnObj:boolean,
}

   /** Required : 
      @param piRFQNum
      @param piRFQLine
      @param plCheckPOs
      @param plCheckPriceBreaks
      @param plCheckRFQs
      @param pcIncludeVendAttrList
      @param pcExcludeVendAttrList
      @param pcComplianceList
      @param ds
   */  
export interface VendorWizard_input{
      /**  The RFQ number  */  
   piRFQNum:number,
      /**  The RFQ Line number  */  
   piRFQLine:number,
      /**  The CheckPOs  */  
   plCheckPOs:boolean,
      /**  The CheckPriceBreaks  */  
   plCheckPriceBreaks:boolean,
      /**  The CheckRFQs  */  
   plCheckRFQs:boolean,
      /**  The include vendor attributes list  */  
   pcIncludeVendAttrList:string,
      /**  The exclude vendor attributes list  */  
   pcExcludeVendAttrList:string,
      /**  The Compliances the vendor must accomplish  */  
   pcComplianceList:string,
   ds:Erp_Tablesets_RFQEntryTableset[],
}

export interface VendorWizard_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryTableset[],
   pcMessage:string,
}
}

