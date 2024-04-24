import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CNCustomsDeclarationBillSvc
// Description: CustomsDeclarationBill
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/$metadata", {
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
   Description: Get CNCustomsDeclarationBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNCustomsDeclarationBills
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   */  
export function get_CNCustomsDeclarationBills(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNCustomsDeclarationBills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CNCustomsDeclarationBills(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CNCustomsDeclarationBill item
   Description: Calls GetByID to retrieve the CNCustomsDeclarationBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNCustomsDeclarationBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationBill Desc: DeclarationBill   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   */  
export function get_CNCustomsDeclarationBills_Company_DeclarationBill(Company:string, DeclarationBill:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CNCustomsDeclarationBillHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills(" + Company + "," + DeclarationBill + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CNCustomsDeclarationBillHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CNCustomsDeclarationBill for the service
   Description: Calls UpdateExt to update CNCustomsDeclarationBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNCustomsDeclarationBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationBill Desc: DeclarationBill   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CNCustomsDeclarationBills_Company_DeclarationBill(Company:string, DeclarationBill:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills(" + Company + "," + DeclarationBill + ")", {
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
   Summary: Call UpdateExt to delete CNCustomsDeclarationBill item
   Description: Call UpdateExt to delete CNCustomsDeclarationBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNCustomsDeclarationBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationBill Desc: DeclarationBill   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CNCustomsDeclarationBills_Company_DeclarationBill(Company:string, DeclarationBill:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBills(" + Company + "," + DeclarationBill + ")", {
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
   Description: Get CNCustomsDeclarationBillDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNCustomsDeclarationBillDetails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   */  
export function get_CNCustomsDeclarationBillDetails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNCustomsDeclarationBillDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CNCustomsDeclarationBillDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CNCustomsDeclarationBillDetail item
   Description: Calls GetByID to retrieve the CNCustomsDeclarationBillDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNCustomsDeclarationBillDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationBill Desc: DeclarationBill   Required: True   Allow empty value : True
      @param DeclarationBillLine Desc: DeclarationBillLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   */  
export function get_CNCustomsDeclarationBillDetails_Company_DeclarationBill_DeclarationBillLine(Company:string, DeclarationBill:string, DeclarationBillLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CNCustomsDeclarationBillDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CNCustomsDeclarationBillDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CNCustomsDeclarationBillDetail for the service
   Description: Calls UpdateExt to update CNCustomsDeclarationBillDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNCustomsDeclarationBillDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationBill Desc: DeclarationBill   Required: True   Allow empty value : True
      @param DeclarationBillLine Desc: DeclarationBillLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclarationBillDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CNCustomsDeclarationBillDetails_Company_DeclarationBill_DeclarationBillLine(Company:string, DeclarationBill:string, DeclarationBillLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")", {
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
   Summary: Call UpdateExt to delete CNCustomsDeclarationBillDetail item
   Description: Call UpdateExt to delete CNCustomsDeclarationBillDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNCustomsDeclarationBillDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclarationBill Desc: DeclarationBill   Required: True   Allow empty value : True
      @param DeclarationBillLine Desc: DeclarationBillLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CNCustomsDeclarationBillDetails_Company_DeclarationBill_DeclarationBillLine(Company:string, DeclarationBill:string, DeclarationBillLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/CNCustomsDeclarationBillDetails(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclarationBillHdrLstRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCNCustomsDeclarationBillHeader:string, whereClauseCNCustomsDeclarationBillDetail:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCNCustomsDeclarationBillHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCNCustomsDeclarationBillHeader=" + whereClauseCNCustomsDeclarationBillHeader
   }
   if(typeof whereClauseCNCustomsDeclarationBillDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCNCustomsDeclarationBillDetail=" + whereClauseCNCustomsDeclarationBillDetail
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(declarationBill:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof declarationBill!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "declarationBill=" + declarationBill
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetList" + params, {
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
   Summary: Invoke method PreUpdate
   Description: Performs validations
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/PreUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCNWeightUOMClass
   Description: Returns XbSyst.CNWeightUOMClass. This method is only used by Smart Client.
   OperationID: GetCNWeightUOMClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCNWeightUOMClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCNWeightUOMClass(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetCNWeightUOMClass", {
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
   Summary: Invoke method ChangeSourceDocumentType
   Description: Performs validations and sets defaults values after the Source Document Type has been changed
   OperationID: ChangeSourceDocumentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSourceDocumentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSourceDocumentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSourceDocumentType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/ChangeSourceDocumentType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCustVendorNum
   Description: Performs validations and sets defaults values after the Customer/Supplier has been changed
   OperationID: ChangeCustVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustVendorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/ChangeCustVendorNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoice
   Description: Sets the default values after changing the invoice
   OperationID: ChangeInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/ChangeInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Performs validations and sets defaults values after the Part has been changed
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/ChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCurrencyCode
   Description: Performs validations and sets defaults values after the Currency has been changed
   OperationID: ChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/ChangeCurrencyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteDeclarationBillHeader
   Description: Deletes DeclarationBillHeader.
   OperationID: DeleteDeclarationBillHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteDeclarationBillHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDeclarationBillHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteDeclarationBillHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/DeleteDeclarationBillHeader", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCNCustomsDeclarationBillHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNCustomsDeclarationBillHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNCustomsDeclarationBillHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNCustomsDeclarationBillHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCNCustomsDeclarationBillHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetNewCNCustomsDeclarationBillHeader", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCNCustomsDeclarationBillDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNCustomsDeclarationBillDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNCustomsDeclarationBillDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNCustomsDeclarationBillDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCNCustomsDeclarationBillDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetNewCNCustomsDeclarationBillDetail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclarationBillSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CNCustomsDeclarationBillDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclarationBillHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CNCustomsDeclarationBillHeaderRow[],
}

export interface Erp_Tablesets_CNCustomsDeclarationBillDetailRow{
      /**  Company  */  
   "Company":string,
      /**  Declaration Bill  */  
   "DeclarationBill":string,
      /**  Line Number  */  
   "DeclarationBillLine":number,
      /**  Part  */  
   "PartNum":string,
      /**  Specification  */  
   "Specification":string,
      /**  Quantity  */  
   "Quantity":number,
      /**  UOM  */  
   "UOM":string,
      /**  Weight  */  
   "Weight":number,
      /**  Unit of Weight  */  
   "WeightUOM":string,
      /**  Unit Price  */  
   "UnitPrice":number,
      /**  Total Price  */  
   "TotalPrice":number,
      /**  Country  */  
   "CountryNum":number,
      /**  Domestic Destination  */  
   "DomesticDestination":string,
      /**  Tax Exemption Type  */  
   "TaxExemptType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CNWeightUOMClass":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow{
      /**  Company  */  
   "Company":string,
      /**  Declaration Bill  */  
   "DeclarationBill":string,
      /**  Direction  */  
   "Direction":string,
      /**  Handbook Code  */  
   "HandbookCode":string,
      /**  Trade Mode  */  
   "TradeMode":string,
      /**  Declaration Date  */  
   "DeclarationDate":string,
      /**  Contract Number  */  
   "ContractNumber":string,
      /**  Trade Port  */  
   "TradePort":string,
      /**  Agent  */  
   "Agent":string,
      /**  Net Weight  */  
   "NetWeight":number,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**  Unit of Weight  */  
   "WeightUOM":string,
      /**  Source Document Type  */  
   "SourceDocumentType":string,
      /**  Customer/Supplier Number  */  
   "CustVendorNum":number,
      /**  AR Invoice Number  */  
   "InvoiceNum":number,
      /**  AP Invoice Num  */  
   "APInvNum":string,
      /**  Invoice Amount  */  
   "InvoiceAmt":number,
      /**  Declaration Amount  */  
   "DeclarationAmt":number,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  SysRowID  */  
   "SysRowID":string,
   "CustID":string,
   "DspCurrencyID":string,
   "DspDirection":string,
   "DspInvoiceCurrencyID":string,
   "DspInvoiceNum":string,
   "DspSourceDocumentType":string,
   "DspTradeMode":string,
   "VendorID":string,
   "InvoiceDeleted":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CNCustomsDeclarationBillHeaderRow{
      /**  Company  */  
   "Company":string,
      /**  Declaration Bill  */  
   "DeclarationBill":string,
      /**  Direction  */  
   "Direction":string,
      /**  Handbook Code  */  
   "HandbookCode":string,
      /**  Trade Mode  */  
   "TradeMode":string,
      /**  Declaration Date  */  
   "DeclarationDate":string,
      /**  Contract Number  */  
   "ContractNumber":string,
      /**  Trade Port  */  
   "TradePort":string,
      /**  Agent  */  
   "Agent":string,
      /**  Net Weight  */  
   "NetWeight":number,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**  Unit of Weight  */  
   "WeightUOM":string,
      /**  Source Document Type  */  
   "SourceDocumentType":string,
      /**  Customer/Supplier Number  */  
   "CustVendorNum":number,
      /**  AR Invoice Number  */  
   "InvoiceNum":number,
      /**  AP Invoice Num  */  
   "APInvNum":string,
      /**  Invoice Amount  */  
   "InvoiceAmt":number,
      /**  Declaration Amount  */  
   "DeclarationAmt":number,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "CustID":string,
   "VendorID":string,
   "InvoiceCurrencyCode":string,
   "InvoiceDeleted":boolean,
   "GrossWeightUOM":string,
   "DspCurrencyID":string,
   "DspDirection":string,
   "DspInvoiceCurrencyID":string,
   "DspInvoiceNum":string,
   "DspSourceDocumentType":string,
   "DspTradeMode":string,
   "CNWeightUOMClass":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param currencyCode
      @param ds
   */  
export interface ChangeCurrencyCode_input{
   currencyCode:string,
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface ChangeCurrencyCode_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

   /** Required : 
      @param custVendorNum
      @param ds
   */  
export interface ChangeCustVendorNum_input{
      /**  new value  */  
   custVendorNum:number,
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface ChangeCustVendorNum_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param apInvNum
      @param ds
   */  
export interface ChangeInvoice_input{
   invoiceNum:number,
   apInvNum:string,
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface ChangeInvoice_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

   /** Required : 
      @param partNum
      @param ds
   */  
export interface ChangePartNum_input{
      /**  new value  */  
   partNum:string,
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface ChangePartNum_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

   /** Required : 
      @param documentType
      @param ds
   */  
export interface ChangeSourceDocumentType_input{
      /**  new value  */  
   documentType:string,
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface ChangeSourceDocumentType_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

   /** Required : 
      @param declarationBill
   */  
export interface DeleteByID_input{
   declarationBill:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
      @param updateReferencedDoc
   */  
export interface DeleteDeclarationBillHeader_input{
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
      /**  if true then DeclarationBill field of ShipHead, RcvHead, RMAHead, DMRHead will be cleared and DeclarationBillHeader will be deleted, else warning message will be returned  */  
   updateReferencedDoc:boolean,
}

export interface DeleteDeclarationBillHeader_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
   message:string,
}
}

export interface Erp_Tablesets_CNCustomsDeclarationBillDetailRow{
      /**  Company  */  
   Company:string,
      /**  Declaration Bill  */  
   DeclarationBill:string,
      /**  Line Number  */  
   DeclarationBillLine:number,
      /**  Part  */  
   PartNum:string,
      /**  Specification  */  
   Specification:string,
      /**  Quantity  */  
   Quantity:number,
      /**  UOM  */  
   UOM:string,
      /**  Weight  */  
   Weight:number,
      /**  Unit of Weight  */  
   WeightUOM:string,
      /**  Unit Price  */  
   UnitPrice:number,
      /**  Total Price  */  
   TotalPrice:number,
      /**  Country  */  
   CountryNum:number,
      /**  Domestic Destination  */  
   DomesticDestination:string,
      /**  Tax Exemption Type  */  
   TaxExemptType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   CurrencyCode:string,
   CNWeightUOMClass:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow{
      /**  Company  */  
   Company:string,
      /**  Declaration Bill  */  
   DeclarationBill:string,
      /**  Direction  */  
   Direction:string,
      /**  Handbook Code  */  
   HandbookCode:string,
      /**  Trade Mode  */  
   TradeMode:string,
      /**  Declaration Date  */  
   DeclarationDate:string,
      /**  Contract Number  */  
   ContractNumber:string,
      /**  Trade Port  */  
   TradePort:string,
      /**  Agent  */  
   Agent:string,
      /**  Net Weight  */  
   NetWeight:number,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**  Unit of Weight  */  
   WeightUOM:string,
      /**  Source Document Type  */  
   SourceDocumentType:string,
      /**  Customer/Supplier Number  */  
   CustVendorNum:number,
      /**  AR Invoice Number  */  
   InvoiceNum:number,
      /**  AP Invoice Num  */  
   APInvNum:string,
      /**  Invoice Amount  */  
   InvoiceAmt:number,
      /**  Declaration Amount  */  
   DeclarationAmt:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  SysRowID  */  
   SysRowID:string,
   CustID:string,
   DspCurrencyID:string,
   DspDirection:string,
   DspInvoiceCurrencyID:string,
   DspInvoiceNum:string,
   DspSourceDocumentType:string,
   DspTradeMode:string,
   VendorID:string,
   InvoiceDeleted:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CNCustomsDeclarationBillHeaderRow{
      /**  Company  */  
   Company:string,
      /**  Declaration Bill  */  
   DeclarationBill:string,
      /**  Direction  */  
   Direction:string,
      /**  Handbook Code  */  
   HandbookCode:string,
      /**  Trade Mode  */  
   TradeMode:string,
      /**  Declaration Date  */  
   DeclarationDate:string,
      /**  Contract Number  */  
   ContractNumber:string,
      /**  Trade Port  */  
   TradePort:string,
      /**  Agent  */  
   Agent:string,
      /**  Net Weight  */  
   NetWeight:number,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**  Unit of Weight  */  
   WeightUOM:string,
      /**  Source Document Type  */  
   SourceDocumentType:string,
      /**  Customer/Supplier Number  */  
   CustVendorNum:number,
      /**  AR Invoice Number  */  
   InvoiceNum:number,
      /**  AP Invoice Num  */  
   APInvNum:string,
      /**  Invoice Amount  */  
   InvoiceAmt:number,
      /**  Declaration Amount  */  
   DeclarationAmt:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   CustID:string,
   VendorID:string,
   InvoiceCurrencyCode:string,
   InvoiceDeleted:boolean,
   GrossWeightUOM:string,
   DspCurrencyID:string,
   DspDirection:string,
   DspInvoiceCurrencyID:string,
   DspInvoiceNum:string,
   DspSourceDocumentType:string,
   DspTradeMode:string,
   CNWeightUOMClass:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CNCustomsDeclarationBillListTableset{
   CNCustomsDeclarationBillHdrLst:Erp_Tablesets_CNCustomsDeclarationBillHdrLstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CNCustomsDeclarationBillTableset{
   CNCustomsDeclarationBillHeader:Erp_Tablesets_CNCustomsDeclarationBillHeaderRow[],
   CNCustomsDeclarationBillDetail:Erp_Tablesets_CNCustomsDeclarationBillDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCNCustomsDeclarationBillTableset{
   CNCustomsDeclarationBillHeader:Erp_Tablesets_CNCustomsDeclarationBillHeaderRow[],
   CNCustomsDeclarationBillDetail:Erp_Tablesets_CNCustomsDeclarationBillDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param declarationBill
   */  
export interface GetByID_input{
   declarationBill:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface GetCNWeightUOMClass_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param declarationBill
   */  
export interface GetNewCNCustomsDeclarationBillDetail_input{
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
   declarationBill:string,
}

export interface GetNewCNCustomsDeclarationBillDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCNCustomsDeclarationBillHeader_input{
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface GetNewCNCustomsDeclarationBillHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

   /** Required : 
      @param whereClauseCNCustomsDeclarationBillHeader
      @param whereClauseCNCustomsDeclarationBillDetail
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCNCustomsDeclarationBillHeader:string,
   whereClauseCNCustomsDeclarationBillDetail:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
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
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
   warnings:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCNCustomsDeclarationBillTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCNCustomsDeclarationBillTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CNCustomsDeclarationBillTableset[],
}
}

