import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ApplyCreditMemoSvc
// Description: Apply Credit Memo entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/$metadata", {
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
   Description: Get ApplyCreditMemoes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ApplyCreditMemoes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadRow
   */  
export function get_ApplyCreditMemoes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ApplyCreditMemoes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ApplyCreditMemoes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyCreditMemoes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ApplyCreditMemoes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ApplyCreditMemo item
   Description: Calls GetByID to retrieve the ApplyCreditMemo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ApplyCreditMemo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   */  
export function get_ApplyCreditMemoes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ApplyCreditMemoes(" + Company + "," + GroupID + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ApplyCreditMemo for the service
   Description: Calls UpdateExt to update ApplyCreditMemo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ApplyCreditMemo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ApplyCreditMemoes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ApplyCreditMemoes(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete ApplyCreditMemo item
   Description: Call UpdateExt to delete ApplyCreditMemo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ApplyCreditMemo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ApplyCreditMemoes_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ApplyCreditMemoes(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Description: Get CashDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   */  
export function get_ApplyCreditMemoes_Company_GroupID_HeadNum_CashDtls(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ApplyCreditMemoes(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   */  
export function get_ApplyCreditMemoes_Company_GroupID_HeadNum_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ApplyCreditMemoes(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CashDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   */  
export function get_CashDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CashDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CashDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   */  
export function get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashDtl for the service
   Description: Calls UpdateExt to update CashDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Summary: Call UpdateExt to delete CashDtl item
   Description: Call UpdateExt to delete CashDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow)
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
export function get_GetRows(whereClauseCashHead:string, whereClauseCashDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCashHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashHead=" + whereClauseCashHead
   }
   if(typeof whereClauseCashDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashDtl=" + whereClauseCashDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetList" + params, {
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
   Summary: Invoke method _ApplyCreditMemoCC
   Description: This method needs to be run as the last method as the user leaves the CashHead record.
It validates that the entire memo has been applied and creates the required GL records
If the entire memo has not been applied, then an exception will be raised and the user
cannot leave the record until it all has been applied.
   OperationID: _ApplyCreditMemoCC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/_ApplyCreditMemoCC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_ApplyCreditMemoCC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyCreditMemoCC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/_ApplyCreditMemoCC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BeforeApplyCreditMemoCC
   Description: Method performs actions needed before sending the CashHead to the posting engine
Checks Withholding Taxes
Calculates Gains/Loss
Creates balancing CashDtl records
Performs Tax Calculation and Allocation
It should be done as the final step before posting engine
   OperationID: BeforeApplyCreditMemoCC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BeforeApplyCreditMemoCC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeApplyCreditMemoCC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BeforeApplyCreditMemoCC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/BeforeApplyCreditMemoCC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvcLegalNumber
   Description: metod to get InvcLegalNumber
   OperationID: GetInvcLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcLegalNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetInvcLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCMAmount
   Description: This method updates the DocTranAmt, UnuppliedAmt fields after
the CMAmount field is updated.
   OperationID: ChangeCMAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCMAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCMAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCMAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ChangeCMAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxWhld
   Description: This method updates the Applied/Unnaplied amounts after TaxWhld field is updated.
   OperationID: ChangeTaxWhld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxWhld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxWhld_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxWhld(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ChangeTaxWhld", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDetailWithholdTax
   Description: This method updates the Header Applied/Unnaplied amounts after DispDocWithholdAmt field is updated.
   OperationID: ChangeDetailWithholdTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailWithholdTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailWithholdTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailWithholdTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ChangeDetailWithholdTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePNRefCC
   Description: Procedure to be called when changing the PNRef field in the
            CashDtl table. This field will only be used for Credit Payment records
   OperationID: ChangePNRefCC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePNRefCC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePNRefCC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePNRefCC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ChangePNRefCC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranDate
   Description: Updates the ttCashHead.tranAmt when the date is changed to avoid wrong currency conversions.
   OperationID: ChangeTranDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/ChangeTranDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCreditCardRecords
   Description: This procedure will look for Credit Card records within CreditTran
            using the information in the CashHead table
   OperationID: CheckCreditCardRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCreditCardRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCreditCardRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCreditCardRecords(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CheckCreditCardRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentIsLocked(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckExchangeRate
   Description: This method is called when the CashDtl InvoiceNum field is modified
   OperationID: CheckExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckExchangeRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CheckExchangeRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOnScreenLoad
   Description: This method is called first thing when opening the screen.  It checks to see if
the G/L is interfaced and if the Fiscal Period is valid.  If the G/L is not interfaced,
a question asking if the user wants to continue will be returned.  If the user answers no,
then they are returned to the main menu.  If the Fiscal Period is invalid, an exception
will be raised and the user should be returned to the main menu.
   OperationID: CheckOnScreenLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOnScreenLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOnScreenLoad(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CheckOnScreenLoad", {
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
   Summary: Invoke method CreateWhereCustNumBO
   Description: // Apply Credit Memos to their own invoices and for customers defined in the �Payer-Sold To� Relationship (National Account)
   OperationID: CreateWhereCustNumBO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateWhereCustNumBO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateWhereCustNumBO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateWhereCustNumBO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/CreateWhereCustNumBO", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteCashDetails
   Description: This method needs to be run as the last method if the user chooses not to
Apply Credit Memo but wants to leave the CashHead record to create a new one
or closes/exits the ApplyCreditMemo UI screen.
This will delete the appropriate CashHead and CashDtl records and update the
related InvcHead to reflect the appropriate invoice balance.
   OperationID: DeleteCashDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCashDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCashDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCashDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/DeleteCashDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocumentHasTaxes
   Description: This method is used to determine whenever the document has taxes
   OperationID: DocumentHasTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocumentHasTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocumentHasTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocumentHasTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/DocumentHasTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyInfo
   Description: This method is used when the Currency Code changed
   OperationID: GetCurrencyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetCurrencyInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlInvoiceInfo
   Description: This method is called when the CashDtl InvoiceNum field is modified
   OperationID: GetDtlInvoiceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlInvoiceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlInvoiceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlInvoiceInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetDtlInvoiceInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlTranAmtInfo
   Description: This method is run when the DocTranAmt field is modified
   OperationID: GetDtlTranAmtInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlTranAmtInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlTranAmtInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlTranAmtInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetDtlTranAmtInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFiscalInfo
   Description: This method is run when the Transaction date is changed to update the fiscal period fields
   OperationID: GetFiscalInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetFiscalInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHdrDocumentInfo
   Description: This method will validate the document number provided and if valid, will default CashHead fields
to the values in the Document (Credit Memo, Deposit Invoice or Deposit Payment)
   OperationID: GetHdrDocumentInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHdrDocumentInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHdrDocumentInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHdrDocumentInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetHdrDocumentInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHdrTranAmtInfo
   Description: This method is used to validate/update the dataset when the DocTranAmt is udpated
   OperationID: GetHdrTranAmtInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHdrTranAmtInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHdrTranAmtInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHdrTranAmtInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetHdrTranAmtInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvoiceNumPreloadFilter
   Description: PreLoadSearchFilter - to get filter for own invoices and for customers defined in the "Payer-Sold To" Relationship (National Account)
   OperationID: GetInvoiceNumPreloadFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoiceNumPreloadFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoiceNumPreloadFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvoiceNumPreloadFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetInvoiceNumPreloadFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCreditPayment
   Description: This method is to be used when creating new Credit Payments. In this case
the invoice should be the same used in the header
   OperationID: GetNewCreditPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCreditPayment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetNewCreditPayment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnDocumentTypeChanging
   Description: This method validates changings of the 'DocumentType' field
   OperationID: OnDocumentTypeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnDocumentTypeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnDocumentTypeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnDocumentTypeChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/OnDocumentTypeChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetNewCashHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetNewCashDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ApplyCreditMemoSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadRow[],
}

export interface Erp_Tablesets_CashDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  */  
   "GroupID":string,
      /**  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  */  
   "HeadNum":number,
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   "InvoiceNum":number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   "InvoiceRef":number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   "TranType":string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger Module.  */  
   "GLPosted":boolean,
      /**  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  */  
   "TranDate":string,
      /**   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   "CheckRef":string,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  */  
   "TranAmt":number,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  */  
   "DocTranAmt":number,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   "Discount":number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   "DocDiscount":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  */  
   "Comment":string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   "Reference":string,
      /**   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  */  
   "DebitNote":boolean,
      /**  Debit Note Detail Comments.  */  
   "DNComments":string,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DNAmount":number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   "DocDnAmount":number,
      /**  The Debit Note Number assigned by the customer.  */  
   "DNCustNbr":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DnAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal Year Suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt No. (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date  (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate No. (Thailand Localization)  */  
   "WHTCertificateNo":string,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  Invoice Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  SEPADDMsgID  */  
   "SEPADDMsgID":string,
      /**  SEPADDPmtID  */  
   "SEPADDPmtID":string,
      /**  PmtDueDate  */  
   "PmtDueDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  MX Payment Number for AR Invoice  */  
   "MXPaymentNum":number,
      /**  Reference to HeadNum of main CashHead record.  */  
   "WriteOffHeadNumRef":number,
      /**  EpicorFSA  */  
   "EpicorFSA":boolean,
      /**  Taxable Adjustment  */  
   "TaxableAdjustment":boolean,
   "ApplyDate":string,
      /**  Adjustment amount in Base Currency  */  
   "BaseAdjAmt":number,
   "BaseCurrDesc":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  */  
   "BillConNum":number,
      /**  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  */  
   "CopyRate":boolean,
      /**  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  */  
   "CorrectionInv":boolean,
   "CreditMemo":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyDescription":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol  */  
   "CurrSymbol":string,
      /**  This field displays all Debit Note customer defined numbers applied.  */  
   "DebitNotesApplied":string,
   "DispDocSelfAssessAmt":number,
   "DispDocWithholdAmt":number,
      /**  Display gl account  */  
   "DispGLAcct":string,
   "DispSelfAssessAmt":number,
   "DispTranAmt":number,
   "DispWithholdAmt":number,
   "DocDispTranAmt":number,
      /**  Doc Invoice Amount  */  
   "DocInvoiceAmt":number,
      /**  Doc Invoice Balance  */  
   "DocInvoiceBal":number,
   "DocNetCash":number,
      /**  Doc New Invoice Balance  */  
   "DocNewBalance":number,
      /**  Write Off Amount  */  
   "DocWriteOffAmount":number,
      /**  If this flag is true then CopyRate checkbox is Read Only  */  
   "DsblCopyRate":boolean,
      /**  Legal Number Field  */  
   "EnableAssignLegNum":boolean,
   "EnableTranDocType":boolean,
      /**  Legal Number Field  */  
   "EnableVoidLegNum":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   "FullyPaid":boolean,
   "GainLossAmt":number,
      /**  G/L Reference Code Description  */  
   "GLRefCodeDesc":string,
      /**  Legal Number Field  */  
   "HasLegNumCnfg":boolean,
   "InvDiscountDate":string,
   "InvDueDate":string,
      /**  Invoice Exchange Rate  */  
   "InvExchRate":number,
   "InvLegalNumber":string,
   "InvLockRate":boolean,
      /**  Invoice Amount  */  
   "InvoiceAmt":number,
      /**  Invoice Balance  */  
   "InvoiceBal":number,
   "InvTermsCode":string,
   "InvXRateLabel":string,
      /**  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  */  
   "IsCreditPayment":boolean,
   "IsDiscountforCreditM":boolean,
   "LegalNumMessage":string,
   "LegalNumStyle":string,
   "NetCash":number,
      /**  New Invoice Balance  */  
   "NewBalance":number,
   "OldGainLoss":number,
      /**  The related order number (InvcHead.OrderNum)  */  
   "OrderNum":number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   "PNRef":string,
      /**  Indicates if posting GL transactions  */  
   "PostToGL":boolean,
      /**  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  */  
   "RecalcTranAmt":boolean,
   "RedStornoOpt":string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   "RefCodeStatus":string,
      /**  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  */  
   "RemoveForAdjustment":boolean,
   "Rpt1DispTranAmt":number,
   "Rpt1GainLossAmt":number,
   "Rpt1InvoiceAmt":number,
   "Rpt1InvoiceBal":number,
   "Rpt1NetCash":number,
   "Rpt1NewBalance":number,
   "Rpt1OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt1WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt1WriteOffGainLossAmt":number,
   "Rpt2DispTranAmt":number,
   "Rpt2GainLossAmt":number,
   "Rpt2InvoiceAmt":number,
   "Rpt2InvoiceBal":number,
   "Rpt2NetCash":number,
   "Rpt2NewBalance":number,
   "Rpt2OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt2WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt2WriteOffGainLossAmt":number,
   "Rpt3DispTranAmt":number,
   "Rpt3GainLossAmt":number,
   "Rpt3InvoiceAmt":number,
   "Rpt3InvoiceBal":number,
   "Rpt3NetCash":number,
   "Rpt3NewBalance":number,
   "Rpt3OldGainLoss":number,
      /**  Write Off Amount  */  
   "Rpt3WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "Rpt3WriteOffGainLossAmt":number,
      /**  CustID associated with CashDtl.SoldToCustNum  */  
   "SoldToCustID":string,
      /**  Populated from InvcHead.SoldToCustNum.  */  
   "SoldToCustNum":number,
      /**  CustName associated with CashDtl.SoldToCustNum  */  
   "SoldToCustomerName":string,
      /**  Legal Number Field  */  
   "SystemTranType":string,
      /**  Description of the Tran Type  */  
   "TranTypeDesc":string,
      /**  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  */  
   "Type":string,
      /**  Write Off  */  
   "WriteOff":boolean,
      /**  Write Off Account  */  
   "WriteOffAccount":string,
      /**  Write Off Account Description  */  
   "WriteOffAccountDesc":string,
      /**  Write Off Amount  */  
   "WriteOffAmount":number,
      /**  Write Off Gain Loss Amount  */  
   "WriteOffGainLossAmt":number,
   "XRateLabel":string,
      /**  Legal Number Field  */  
   "AllowChgAfterPrint":boolean,
      /**  Write Off Amount  */  
   "OldWriteOffAmount":number,
   "WriteOffAccountDisp":string,
   "TaxableWriteOff":boolean,
      /**  Total Gain Loss Amount  */  
   "TotalGainLossAmt":number,
      /**  Write Off Amount  */  
   "OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt1OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt2OldWriteOffGainLossAmt":number,
      /**  Write Off Amount  */  
   "Rpt3OldWriteOffGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt1TotalGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt2TotalGainLossAmt":number,
      /**  Total Gain Loss Amount  */  
   "Rpt3TotalGainLossAmt":number,
      /**  Write Off Amount  */  
   "DocOldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt1OldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt2OldWriteOffAmount":number,
      /**  Write Off Amount  */  
   "Rpt3OldWriteOffAmount":number,
      /**  Allows uset to enter comment for Write Off.  */  
   "WriteOffComment":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
   "ReferenceTranDate":string,
   "ReferenceTranNum":number,
   "ReferenceTranTime":number,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   "EnableManualWHTax":boolean,
      /**  Indicates if the withholding amount tax was manually modified.  */  
   "WHTaxManualChange":boolean,
   "BitFlag":number,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "InvoiceNumInvoiceType":string,
   "InvoiceNumCardMemberName":string,
   "InvoiceNumTermsCode":string,
   "RateGrpDescription":string,
   "TaxRgnDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   "GroupID":string,
      /**  Displays the receipt header number used for internal reference.  */  
   "HeadNum":number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Displays the transaction type.  */  
   "TranType":string,
      /**  Displays the number of the check.  */  
   "CheckRef":string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   "OrderNum":number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   "InvoiceNum":number,
      /**  Displays the transaction amount.  */  
   "TranAmt":number,
      /**  Displays the transaction amount in customer currency.  */  
   "DocTranAmt":number,
      /**  Displays the customer ID.  */  
   "CustID":string,
      /**  Displays the date of the transaction.  */  
   "TranDate":string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**  Displays the unapplied amount.  */  
   "UnAppliedAmt":number,
      /**  Displays the unapplied amount in base currency.  */  
   "DocUnAppliedAmt":number,
      /**  Displays the amount applied to invoices.  */  
   "AppliedAmt":number,
      /**  Displays the amount in document currency applied to invoices.  */  
   "DocAppliedAmt":number,
      /**  Displays the fiscal year that the check is posted to.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period that the check is posted to.  */  
   "FiscalPeriod":number,
      /**  Displays any reference.  */  
   "Reference":string,
      /**  Indicates if this transaction has been posted.  */  
   "GLPosted":boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   "CreditMemoNum":number,
      /**  Displays the customer currency.  */  
   "CurrencyCode":string,
      /**  Displays the exchange rate that is used for this check.  */  
   "ExchangeRate":number,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Displays the tax amount.  */  
   "DocTaxAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Displays the legal number of the check.  */  
   "LegalNumber":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   "DebNoteOnly":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnAppliedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  The unique code of Receipt Currency.  */  
   "ReceiptCurrencyCode":string,
      /**  Amount of Receipt in Receipt Currency.  */  
   "ReceiptAmt":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   "BankRcptExchangeRate":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   "SettlementExchangeRate":number,
      /**  The unique Currency code for Credit Memo.  */  
   "CMCurrencyCode":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "CMAmount":number,
      /**  Reference to cash receipt which had been reversed.  */  
   "ReverseRef":number,
      /**  Date when cash receipt had been reversed  */  
   "ReverseDate":string,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Withhold Tax  */  
   "TaxWhld":number,
      /**  Dsicount Date  */  
   "DiscountDate":string,
      /**  Calculate Withhold Tax  */  
   "TaxWhldCalc":number,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   "UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   "DocUnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   "Rpt1UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   "Rpt2UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   "Rpt3UnallocatedAmt":number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   "ApplyHeadNum":number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   "AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   "DocAllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   "Rpt1AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   "Rpt2AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   "Rpt3AllocatedAmt":number,
      /**  Comments related to the cash receipt.  */  
   "Comment":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  MandateReference  */  
   "MandateReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SEPADDExportDate  */  
   "SEPADDExportDate":string,
      /**  BOE Invoice Number  */  
   "BOEInvoiceNum":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  DocumentType  */  
   "DocumentType":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  BankRcptExchangeRate10D  */  
   "BankRcptExchangeRate10D":number,
      /**  SettlementExchangeRate10D  */  
   "SettlementExchangeRate10D":number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   "AllowUpdSettlementCurr":boolean,
   "ApplyDate":string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSAddr":string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSZip":string,
   "BankAcctDesc":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Bank Currency Value  */  
   "BankAmount":number,
   "BankBaseXRateLabel":string,
   "BankCurrencyCode":string,
      /**  Bank Currency Symbol  */  
   "BankCurrSymbol":string,
   "BankExchangeRate":number,
   "BankRcptXRateLabel":string,
   "BaseCurrencyCode":string,
   "BaseCurrSymbol":string,
      /**  Bill To Name  */  
   "BillToName":string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   "calcRate":boolean,
      /**  Stored Credit Card Number  */  
   "CardStore":string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   "CardTypeDescription":string,
      /**  Description  */  
   "CashbookLineDescription":string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   "CCAllowSales":boolean,
   "CCApprovalNum":string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   "CCCSCID":string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   "CCEnableAddress":boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   "CCEnableCSC":boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   "CCResponse":string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   "CCTranID":string,
      /**  Credit Card Transaction Type  */  
   "CCTranType":string,
      /**  Description of the currency  */  
   "CMCurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CMCurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CMCurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CMCurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CMCurrencyCodeDocumentDesc":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "CSCResult":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
   "CurrencySwitch":boolean,
   "CustFullAddr":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
   "CustomerName":string,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocDiscount":number,
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   "DocumentNum":number,
      /**  Amount of Credit Memo in CM Currency.  */  
   "DspCMAmount":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  */  
   "DspDocTranAmt":number,
   "DspSalesOrderValue":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspTranAmt":number,
   "EnableTransactionDate":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
      /**  The InvcHead legal number  */  
   "InvcLegalNumber":string,
      /**  The member's name on the credit card.  */  
   "InvoiceNumCardMemberName":string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "InvoiceNumTermsCode":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberDsp":string,
   "LegalNumMessage":string,
      /**  Copied from OrderHed.LockRate  */  
   "LockRate":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
   "PaymentMethod":string,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  Description of the currency  */  
   "RcptCurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "RcptCurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "RcptCurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "RcptCurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "RcptCurrencyCodeDocumentDesc":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt1TranTaxAmt":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt2TranTaxAmt":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt3TranTaxAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SalesOrderValue":number,
   "SettlementXRateLabel":string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   "SoldToCustomerName":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Transaction Amount less Tax Amount  */  
   "TranTaxAmt":number,
      /**  Description of TranType  */  
   "TranTypeDesc":string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   "UnappliedAmountApplied":boolean,
   "XRateLabel":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   "GroupID":string,
      /**  Displays the receipt header number used for internal reference.  */  
   "HeadNum":number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Displays the transaction type.  */  
   "TranType":string,
      /**  Displays the number of the check.  */  
   "CheckRef":string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   "OrderNum":number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   "InvoiceNum":number,
      /**  Displays the transaction amount.  */  
   "TranAmt":number,
      /**  Displays the transaction amount in customer currency.  */  
   "DocTranAmt":number,
      /**  Displays the customer ID.  */  
   "CustID":string,
      /**  Displays the date of the transaction.  */  
   "TranDate":string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**  Displays the unapplied amount.  */  
   "UnAppliedAmt":number,
      /**  Displays the unapplied amount in base currency.  */  
   "DocUnAppliedAmt":number,
      /**  Displays the amount applied to invoices.  */  
   "AppliedAmt":number,
      /**  Displays the amount in document currency applied to invoices.  */  
   "DocAppliedAmt":number,
      /**  Displays the fiscal year that the check is posted to.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period that the check is posted to.  */  
   "FiscalPeriod":number,
      /**  Displays any reference.  */  
   "Reference":string,
      /**  Indicates if this transaction has been posted.  */  
   "GLPosted":boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   "CreditMemoNum":number,
      /**  Displays the customer currency.  */  
   "CurrencyCode":string,
      /**  Displays the exchange rate that is used for this check.  */  
   "ExchangeRate":number,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Displays the tax amount.  */  
   "DocTaxAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Displays the legal number of the check.  */  
   "LegalNumber":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   "DebNoteOnly":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnAppliedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  The unique code of Receipt Currency.  */  
   "ReceiptCurrencyCode":string,
      /**  Amount of Receipt in Receipt Currency.  */  
   "ReceiptAmt":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   "BankRcptExchangeRate":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   "SettlementExchangeRate":number,
      /**  The unique Currency code for Credit Memo.  */  
   "CMCurrencyCode":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "CMAmount":number,
      /**  Reference to cash receipt which had been reversed.  */  
   "ReverseRef":number,
      /**  Date when cash receipt had been reversed  */  
   "ReverseDate":string,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Withhold Tax  */  
   "TaxWhld":number,
      /**  Dsicount Date  */  
   "DiscountDate":string,
      /**  Calculate Withhold Tax  */  
   "TaxWhldCalc":number,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   "UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   "DocUnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   "Rpt1UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   "Rpt2UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   "Rpt3UnallocatedAmt":number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   "ApplyHeadNum":number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   "AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   "DocAllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   "Rpt1AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   "Rpt2AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   "Rpt3AllocatedAmt":number,
      /**  Comments related to the cash receipt.  */  
   "Comment":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  MandateReference  */  
   "MandateReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SEPADDExportDate  */  
   "SEPADDExportDate":string,
      /**  BOE Invoice Number  */  
   "BOEInvoiceNum":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  DocumentType  */  
   "DocumentType":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  BankRcptExchangeRate10D  */  
   "BankRcptExchangeRate10D":number,
      /**  SettlementExchangeRate10D  */  
   "SettlementExchangeRate10D":number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  The amount of the cash receipt applied to invoices in receipt currency  */  
   "RcptCurAppliedAmt":number,
      /**  The amount of the cash receipt that is unapplied in receipt currency  */  
   "RcptCurUnAppliedAmt":number,
      /**  MXAccountNumber  */  
   "MXAccountNumber":string,
      /**  MX Method of Payment: single, multiple, etc.  */  
   "MXPaidAs":string,
      /**  If TRUE then MX Electronic Payment XML is required  */  
   "MXPaySupplementFlag":boolean,
      /**  LockboxID  */  
   "LockboxID":string,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  MX UUID of the original Receipt being corrected  */  
   "MXOriginalCheckRef":string,
      /**  MX Confirmation Code for special Cash Receipts  */  
   "MXConfirmationCode":string,
      /**  MX Customer’s Bank ID  */  
   "MXBankID":string,
      /**  Text entered by the user to indicate the reason Cash receipt was Reversed.  */  
   "ReversedReason":string,
      /**  Credit Card Holder City.  */  
   "CCCity":string,
      /**  Credit Card Holder State.  */  
   "CCState":string,
      /**  ccToken  */  
   "ccToken":string,
      /**  DepositBalance  */  
   "DepositBalance":number,
      /**  DocDepositBalance  */  
   "DocDepositBalance":number,
      /**  Rpt1DepositBalance  */  
   "Rpt1DepositBalance":number,
      /**  Rpt2DepositBalance  */  
   "Rpt2DepositBalance":number,
      /**  Rpt3DepositBalance  */  
   "Rpt3DepositBalance":number,
      /**  Indicates this record is an adjustment CashHead.  */  
   "Adjustment":boolean,
      /**  Reference to cash receipt which had been adjusted.  */  
   "AdjustmentRef":number,
      /**  The reason for the adjustment entered by the user  */  
   "AdjustmentReason":string,
      /**  Total Check Write Off Amount  */  
   "WriteOffAmount":number,
      /**  DocWriteOffAmount  */  
   "DocWriteOffAmount":number,
      /**  Rpt1WriteOffAmount  */  
   "Rpt1WriteOffAmount":number,
      /**  Rpt2WriteOffAmount  */  
   "Rpt2WriteOffAmount":number,
      /**  Rpt3WriteOffAmount  */  
   "Rpt3WriteOffAmount":number,
      /**  Mexico Certified Timestamp  */  
   "MXCertifiedTimestamp":string,
      /**  Mexico SAT Seal  */  
   "MXSATSeal":string,
      /**  Mexico Digital Seal  */  
   "MXDigitalSeal":string,
      /**  Mexico SAT Certificate Serial Number  */  
   "MXSATCertificateSN":string,
      /**  Mexico Original String Timbre Fiscal Digital  */  
   "MXOriginalStringTFD":string,
      /**  Mexico Certificate  */  
   "MXCertificate":string,
      /**  Mexico Certificate Serial Number  */  
   "MXCertificateSN":string,
      /**  SourceGroupID  */  
   "SourceGroupID":string,
      /**  SourceHeadNum  */  
   "SourceHeadNum":number,
      /**  Standard Entry Class Code  */  
   "SEC":string,
      /**  ACH Transaction Code  */  
   "ACHTranCode":number,
      /**  ID of the Customer's bank.  */  
   "CustomerBankID":string,
      /**  The Bank account number for the Customer.  */  
   "CustomerBankAcctNumber":string,
      /**  CustomerBankSwiftNum  */  
   "CustomerBankSwiftNum":string,
      /**  The Bank account IBAN Code  */  
   "CustomerBankIBANCode":string,
      /**  Name on the Bank Account.  */  
   "CustomerBankNameOnAccount":string,
      /**  First address line of customer bank.  */  
   "CustomerBankAddress1":string,
      /**  Second address line of customer bank.  */  
   "CustomerBankAddress2":string,
      /**  Third address line of customer bank.  */  
   "CustomerBankAddress3":string,
      /**  Bank City  */  
   "CustomerBankCity":string,
      /**  Bank State/Prov  */  
   "CustomerBankState":string,
      /**  Postal Code or zip code  */  
   "CustomerBankPostalCode":string,
      /**  Bank account Country Number.  */  
   "CustomerBankCountryNum":number,
      /**  ARRemittanceSlipPrinted  */  
   "ARRemittanceSlipPrinted":boolean,
      /**  Customer Bank Name  */  
   "CustomerBankName":string,
      /**  MXPostedTimeStamp  */  
   "MXPostedTimeStamp":string,
      /**  MXSerie  */  
   "MXSerie":string,
      /**  MXFolio  */  
   "MXFolio":string,
      /**  MXEPaymentType  */  
   "MXEPaymentType":string,
      /**  MXEPaymentCertificateNumber  */  
   "MXEPaymentCertificateNumber":string,
      /**  MXEPaymentOriginalString  */  
   "MXEPaymentOriginalString":string,
      /**  MXEPaymentDigitalSeal  */  
   "MXEPaymentDigitalSeal":string,
      /**  Source  */  
   "Source":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  GL Description for the Reverse process  */  
   "RevDescription":string,
      /**  GL Description for AR - Apply Credit Memo  */  
   "CMDescription":string,
      /**  Receipt Amount in Bank Currency  */  
   "BankReceiptAmt":number,
      /**  MXCancelReasonCode  */  
   "MXCancelReasonCode":string,
      /**  MXSubstHeadNum  */  
   "MXSubstHeadNum":number,
      /**  MXCancellationMode  */  
   "MXCancellationMode":string,
      /**  E-invoice error description.  */  
   "ELIEInvException":string,
      /**  EInvoice ID  */  
   "ELIEInvID":string,
      /**  E-invoice  */  
   "ELIEInvoice":boolean,
      /**  E-invoice Service Provider Status  */  
   "ELIEInvServiceProviderStatus":number,
      /**  E-invoice Status  */  
   "ELIEInvStatus":number,
      /**  User Id of the person generated E-invoice.  */  
   "ELIEInvUpdatedBy":string,
      /**  E-invoice Updated On  */  
   "ELIEInvUpdatedOn":string,
      /**  Adjustment Customer Name  */  
   "AdjustmentCustName":string,
      /**  Customer to which the new invoices will be applied.  */  
   "AdjustmentCustNum":number,
      /**  Date the adjustment was made.  */  
   "AdjustmentDate":string,
      /**  Displays the amount available to apply to the invoices.  */  
   "AdjustmentDocUnAppliedAmt":number,
      /**  On Account  */  
   "AdjustmentOnAccount":boolean,
      /**  Temp TranDocTypeID used when adjusting a Cash Rececipt  */  
   "AdjustmentTranDocTypeID":string,
   "AllocDepBal":number,
   "AllowChgAfterPrint":boolean,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   "AllowUpdSettlementCurr":boolean,
      /**  Amount to Allocate  */  
   "AmtToAlloc":number,
   "ApplyDate":string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSAddr":string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSZip":string,
      /**  Bank Currency Value  */  
   "BankAmount":number,
   "BankBaseXRateLabel":string,
   "BankCurrencyCode":string,
      /**  Bank Currency Symbol  */  
   "BankCurrSymbol":string,
   "BankExchangeRate":number,
   "BankRcptXRateLabel":string,
   "BaseCurrencyCode":string,
      /**  Base Currency Symbol  */  
   "BaseCurrSymbol":string,
      /**  Bill To Name  */  
   "BillToName":string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   "calcRate":boolean,
      /**  Stored Credit Card Number  */  
   "CardStore":string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   "CCAllowSales":boolean,
   "CCApprovalNum":string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   "CCCSCID":string,
      /**  Tokenized value of CSCID  */  
   "CCCSCIDToken":string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   "CCEnableAddress":boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   "CCEnableCSC":boolean,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   "CCIsTraining":boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   "CCResponse":string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   "CCTranID":string,
      /**  Credit Card Transaction Type  */  
   "CCTranType":string,
      /**  Check Box on the UI to filter records by Central Collection flag  */  
   "CentralCollectionCheck":boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  */  
   "CorrectionInv":boolean,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  */  
   "CreditMemo":boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   "CREProcessor":boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "CSCResult":string,
      /**  Current Amount Selected on Invoice Select Tab  */  
   "CurrAmtSelected":number,
   "CurrencySwitch":boolean,
      /**  Displays the address of the customer that paid the receipt.  */  
   "CustFullAddr":string,
   "CustomerName":string,
   "DisableFieldsForPCashDoc":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocAllocDepBal":number,
      /**  Doc Amount to Allocate  */  
   "DocAmtToAlloc":number,
      /**  Displays the discount applied to the receipt.  */  
   "DocDiscount":number,
      /**  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  */  
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   "DocumentNum":number,
   "DocWhldTax":number,
   "DspBankBatchID":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "DspCMAmount":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspDocTranAmt":number,
   "DspSalesOrderValue":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspTranAmt":number,
   "EnableAssignLegNum":boolean,
      /**  Indicates if the option to get the default account is enable.  */  
   "EnableGetDefaultAcct":boolean,
   "EnableTranDocType":boolean,
   "EnableTransactionDate":boolean,
   "EnableVoidLegNum":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
   "GLRefCodeDescription":string,
   "HasLegNumCnfg":boolean,
      /**  The InvcHead legal number  */  
   "InvcLegalNumber":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberDsp":string,
   "LegalNumMessage":string,
      /**  Copied from OrderHed.LockRate  */  
   "LockRate":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "ManualTaxAdj":boolean,
      /**  MXCancellationID  */  
   "MXCancellationID":string,
   "MXCancellationStatus":string,
      /**  MXECEPXml  */  
   "MXECEPXml":string,
      /**  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  */  
   "MXOriginalRefNum":string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   "PayGateHostAddress":string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   "PayGateNameSpace":string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   "PayGatePublicKey":string,
      /**  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  */  
   "ReceiptDate":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
   "Rpt1AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt1TranTaxAmt":number,
   "Rpt1WhldTax":number,
   "Rpt2AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt2TranTaxAmt":number,
   "Rpt2WhldTax":number,
   "Rpt3AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt3TranTaxAmt":number,
   "Rpt3WhldTax":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SalesOrderValue":number,
   "SettlementXRateLabel":string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   "SoldToCustomerName":string,
   "SystemTranType":string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Transaction Amount less Tax Amount  */  
   "TranTaxAmt":number,
      /**  Description of TranType  */  
   "TranTypeDesc":string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   "UnappliedAmountApplied":boolean,
   "WhldTax":number,
   "XRateLabel":string,
      /**  Displays the customer ID.  */  
   "AdjustmentCustID":string,
   "ReferenceTranDate":string,
   "ReferenceTranNum":number,
   "ReferenceTranTime":number,
      /**  Displays the address of the customer that paid the receipt with newline delimiter.  */  
   "CustFullAddrFormatted":string,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   "EnableManualWHTax":boolean,
      /**  Indicates if the withholding tax was manually modified.  */  
   "WHTaxManualChange":boolean,
      /**  Payment type description, displayed in the Details page header.  */  
   "TranTypeDescCaption":string,
   "AdjustmentCustAddress":string,
      /**  Substitution Cash Receipt Group ID  */  
   "MXSubstGroupId":string,
      /**  Substitution Cash Receipt CheckRef  */  
   "MXSubstCheckRef":string,
      /**  Substitution Cash Receipt UUID  */  
   "MXSubstFiscalFolio":string,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "CardTypeDescription":string,
   "CashBHedPosted":boolean,
   "CashBHedCashBookNum":number,
   "CashbookLineDescription":string,
   "CMCurrencyCodeDocumentDesc":string,
   "CMCurrencyCodeCurrName":string,
   "CMCurrencyCodeCurrSymbol":string,
   "CMCurrencyCodeCurrDesc":string,
   "CMCurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CustNumInactive":boolean,
   "CustNumName":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PCashDocDirection":string,
   "PMUIDName":string,
   "PMUIDMXSATCode":string,
   "PMUIDSummarizePerCustomer":boolean,
   "PMUIDType":number,
   "RateGrpDescription":string,
   "RcptCurrencyCodeCurrencyID":string,
   "RcptCurrencyCodeDocumentDesc":string,
   "RcptCurrencyCodeCurrDesc":string,
   "RcptCurrencyCodeCurrSymbol":string,
   "RcptCurrencyCodeCurrName":string,
   "ReverseMXCancelReasonCode":string,
   "ReverseMXCancellationMode":string,
   "SourceTranDateTranDate":string,
   "TaxRegionCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param inHeadNum
      @param inPNRef
      @param tranDate
      @param tranTime
      @param tranNum
   */  
export interface BeforeApplyCreditMemoCC_input{
      /**  CashReceipt HeadNum  */  
   inHeadNum:number,
      /**  PNRef Number, blank if the line is a normal invoice credit  */  
   inPNRef:string,
   tranDate:string,
   tranTime:number,
   tranNum:number,
}

export interface BeforeApplyCreditMemoCC_output{
}

   /** Required : 
      @param cmAmount
      @param ds
   */  
export interface ChangeCMAmount_input{
      /**  Proposed value change to the DocTranAmt field  */  
   cmAmount:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface ChangeCMAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param newTaxWhld
      @param ds
   */  
export interface ChangeDetailWithholdTax_input{
      /**  Proposed value for the document withhold tax  */  
   newTaxWhld:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface ChangeDetailWithholdTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param proposedPNRef
      @param tranDate
      @param tranTime
      @param tranNum
      @param ds
   */  
export interface ChangePNRefCC_input{
      /**  The PNRef to validate against CreditTran  */  
   proposedPNRef:string,
   tranDate:string,
   tranTime:number,
   tranNum:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface ChangePNRefCC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param newTaxWhld
      @param ds
   */  
export interface ChangeTaxWhld_input{
      /**  Proposed value change to the TaxWhld field  */  
   newTaxWhld:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface ChangeTaxWhld_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param tranDate
      @param ds
   */  
export interface ChangeTranDate_input{
      /**  new TransactionDate  */  
   tranDate:string,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface ChangeTranDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param iHeadNum
   */  
export interface CheckCreditCardRecords_input{
      /**  Cash Head Number  */  
   iHeadNum:number,
}

export interface CheckCreditCardRecords_output{
parameters : {
      /**  output parameters  */  
   oHasCreditCardRecords:boolean,
}
}

   /** Required : 
      @param keyValue
   */  
export interface CheckDocumentIsLocked_input{
      /**  InvoiceNum  */  
   keyValue:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param groupID
      @param headNum
      @param invoiceNum
      @param currSymbol
   */  
export interface CheckExchangeRate_input{
      /**  group idr  */  
   groupID:string,
      /**  CashHead HeadNum  */  
   headNum:number,
      /**  Proposed Invoice Number  */  
   invoiceNum:number,
      /**  Currency Symbol  */  
   currSymbol:string,
}

export interface CheckExchangeRate_output{
parameters : {
      /**  output parameters  */  
   pcQuestion:string,
}
}

export interface CheckOnScreenLoad_output{
parameters : {
      /**  output parameters  */  
   vQuestion:string,
}
}

   /** Required : 
      @param CustNum
   */  
export interface CreateWhereCustNumBO_input{
      /**  Customer Number  */  
   CustNum:number,
}

export interface CreateWhereCustNumBO_output{
   returnObj:string,
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface DeleteByID_input{
   groupID:string,
   headNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipHeadNum
   */  
export interface DeleteCashDetails_input{
      /**  CashHead HeadNum  */  
   ipHeadNum:number,
}

export interface DeleteCashDetails_output{
}

   /** Required : 
      @param documentNum
      @param documentType
   */  
export interface DocumentHasTaxes_input{
      /**  Document Number  */  
   documentNum:number,
      /**  Document Type  */  
   documentType:string,
}

export interface DocumentHasTaxes_output{
parameters : {
      /**  output parameters  */  
   hasTaxes:boolean,
}
}

export interface Erp_Tablesets_ApplyCreditMemoTableset{
   CashHead:Erp_Tablesets_CashHeadRow[],
   CashDtl:Erp_Tablesets_CashDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  */  
   GroupID:string,
      /**  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  */  
   HeadNum:number,
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   InvoiceNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   TranType:string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger Module.  */  
   GLPosted:boolean,
      /**  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  */  
   TranDate:string,
      /**   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  */  
   TranAmt:number,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  */  
   DocTranAmt:number,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   Discount:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   DocDiscount:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  */  
   Comment:string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   Reference:string,
      /**   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  */  
   DebitNote:boolean,
      /**  Debit Note Detail Comments.  */  
   DNComments:string,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DNAmount:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DocDnAmount:number,
      /**  The Debit Note Number assigned by the customer.  */  
   DNCustNbr:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal Year Suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt No. (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date  (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate No. (Thailand Localization)  */  
   WHTCertificateNo:string,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  SEPADDMsgID  */  
   SEPADDMsgID:string,
      /**  SEPADDPmtID  */  
   SEPADDPmtID:string,
      /**  PmtDueDate  */  
   PmtDueDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  MX Payment Number for AR Invoice  */  
   MXPaymentNum:number,
      /**  Reference to HeadNum of main CashHead record.  */  
   WriteOffHeadNumRef:number,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  Taxable Adjustment  */  
   TaxableAdjustment:boolean,
   ApplyDate:string,
      /**  Adjustment amount in Base Currency  */  
   BaseAdjAmt:number,
   BaseCurrDesc:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  */  
   BillConNum:number,
      /**  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  */  
   CopyRate:boolean,
      /**  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  */  
   CorrectionInv:boolean,
   CreditMemo:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyDescription:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol  */  
   CurrSymbol:string,
      /**  This field displays all Debit Note customer defined numbers applied.  */  
   DebitNotesApplied:string,
   DispDocSelfAssessAmt:number,
   DispDocWithholdAmt:number,
      /**  Display gl account  */  
   DispGLAcct:string,
   DispSelfAssessAmt:number,
   DispTranAmt:number,
   DispWithholdAmt:number,
   DocDispTranAmt:number,
      /**  Doc Invoice Amount  */  
   DocInvoiceAmt:number,
      /**  Doc Invoice Balance  */  
   DocInvoiceBal:number,
   DocNetCash:number,
      /**  Doc New Invoice Balance  */  
   DocNewBalance:number,
      /**  Write Off Amount  */  
   DocWriteOffAmount:number,
      /**  If this flag is true then CopyRate checkbox is Read Only  */  
   DsblCopyRate:boolean,
      /**  Legal Number Field  */  
   EnableAssignLegNum:boolean,
   EnableTranDocType:boolean,
      /**  Legal Number Field  */  
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
   GainLossAmt:number,
      /**  G/L Reference Code Description  */  
   GLRefCodeDesc:string,
      /**  Legal Number Field  */  
   HasLegNumCnfg:boolean,
   InvDiscountDate:string,
   InvDueDate:string,
      /**  Invoice Exchange Rate  */  
   InvExchRate:number,
   InvLegalNumber:string,
   InvLockRate:boolean,
      /**  Invoice Amount  */  
   InvoiceAmt:number,
      /**  Invoice Balance  */  
   InvoiceBal:number,
   InvTermsCode:string,
   InvXRateLabel:string,
      /**  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  */  
   IsCreditPayment:boolean,
   IsDiscountforCreditM:boolean,
   LegalNumMessage:string,
   LegalNumStyle:string,
   NetCash:number,
      /**  New Invoice Balance  */  
   NewBalance:number,
   OldGainLoss:number,
      /**  The related order number (InvcHead.OrderNum)  */  
   OrderNum:number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   PNRef:string,
      /**  Indicates if posting GL transactions  */  
   PostToGL:boolean,
      /**  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  */  
   RecalcTranAmt:boolean,
   RedStornoOpt:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
      /**  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  */  
   RemoveForAdjustment:boolean,
   Rpt1DispTranAmt:number,
   Rpt1GainLossAmt:number,
   Rpt1InvoiceAmt:number,
   Rpt1InvoiceBal:number,
   Rpt1NetCash:number,
   Rpt1NewBalance:number,
   Rpt1OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt1WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt1WriteOffGainLossAmt:number,
   Rpt2DispTranAmt:number,
   Rpt2GainLossAmt:number,
   Rpt2InvoiceAmt:number,
   Rpt2InvoiceBal:number,
   Rpt2NetCash:number,
   Rpt2NewBalance:number,
   Rpt2OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt2WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt2WriteOffGainLossAmt:number,
   Rpt3DispTranAmt:number,
   Rpt3GainLossAmt:number,
   Rpt3InvoiceAmt:number,
   Rpt3InvoiceBal:number,
   Rpt3NetCash:number,
   Rpt3NewBalance:number,
   Rpt3OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt3WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt3WriteOffGainLossAmt:number,
      /**  CustID associated with CashDtl.SoldToCustNum  */  
   SoldToCustID:string,
      /**  Populated from InvcHead.SoldToCustNum.  */  
   SoldToCustNum:number,
      /**  CustName associated with CashDtl.SoldToCustNum  */  
   SoldToCustomerName:string,
      /**  Legal Number Field  */  
   SystemTranType:string,
      /**  Description of the Tran Type  */  
   TranTypeDesc:string,
      /**  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  */  
   Type:string,
      /**  Write Off  */  
   WriteOff:boolean,
      /**  Write Off Account  */  
   WriteOffAccount:string,
      /**  Write Off Account Description  */  
   WriteOffAccountDesc:string,
      /**  Write Off Amount  */  
   WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   WriteOffGainLossAmt:number,
   XRateLabel:string,
      /**  Legal Number Field  */  
   AllowChgAfterPrint:boolean,
      /**  Write Off Amount  */  
   OldWriteOffAmount:number,
   WriteOffAccountDisp:string,
   TaxableWriteOff:boolean,
      /**  Total Gain Loss Amount  */  
   TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt1TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt2TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt3TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   DocOldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffAmount:number,
      /**  Allows uset to enter comment for Write Off.  */  
   WriteOffComment:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding amount tax was manually modified.  */  
   WHTaxManualChange:boolean,
   BitFlag:number,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   InvoiceNumInvoiceType:string,
   InvoiceNumCardMemberName:string,
   InvoiceNumTermsCode:string,
   RateGrpDescription:string,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   AllowUpdSettlementCurr:boolean,
   ApplyDate:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
   BankAcctDesc:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Bank Currency Value  */  
   BankAmount:number,
   BankBaseXRateLabel:string,
   BankCurrencyCode:string,
      /**  Bank Currency Symbol  */  
   BankCurrSymbol:string,
   BankExchangeRate:number,
   BankRcptXRateLabel:string,
   BaseCurrencyCode:string,
   BaseCurrSymbol:string,
      /**  Bill To Name  */  
   BillToName:string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   calcRate:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   CardTypeDescription:string,
      /**  Description  */  
   CashbookLineDescription:string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   CCAllowSales:boolean,
   CCApprovalNum:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   CCEnableAddress:boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   CCEnableCSC:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  Description of the currency  */  
   CMCurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CMCurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CMCurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CMCurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CMCurrencyCodeDocumentDesc:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
   CurrencySwitch:boolean,
   CustFullAddr:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
   CustomerName:string,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocDiscount:number,
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   DocumentNum:number,
      /**  Amount of Credit Memo in CM Currency.  */  
   DspCMAmount:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  */  
   DspDocTranAmt:number,
   DspSalesOrderValue:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspTranAmt:number,
   EnableTransactionDate:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
      /**  The InvcHead legal number  */  
   InvcLegalNumber:string,
      /**  The member's name on the credit card.  */  
   InvoiceNumCardMemberName:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   InvoiceNumTermsCode:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberDsp:string,
   LegalNumMessage:string,
      /**  Copied from OrderHed.LockRate  */  
   LockRate:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
   PaymentMethod:string,
      /**  Description  */  
   RateGrpDescription:string,
      /**  Description of the currency  */  
   RcptCurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   RcptCurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   RcptCurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   RcptCurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   RcptCurrencyCodeDocumentDesc:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
      /**  Transaction Amount less Tax Amount  */  
   Rpt1TranTaxAmt:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt2TranTaxAmt:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt3TranTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SalesOrderValue:number,
   SettlementXRateLabel:string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   SoldToCustomerName:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Transaction Amount less Tax Amount  */  
   TranTaxAmt:number,
      /**  Description of TranType  */  
   TranTypeDesc:string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   UnappliedAmountApplied:boolean,
   XRateLabel:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadListTableset{
   CashHeadList:Erp_Tablesets_CashHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  The amount of the cash receipt applied to invoices in receipt currency  */  
   RcptCurAppliedAmt:number,
      /**  The amount of the cash receipt that is unapplied in receipt currency  */  
   RcptCurUnAppliedAmt:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MX Method of Payment: single, multiple, etc.  */  
   MXPaidAs:string,
      /**  If TRUE then MX Electronic Payment XML is required  */  
   MXPaySupplementFlag:boolean,
      /**  LockboxID  */  
   LockboxID:string,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  MX UUID of the original Receipt being corrected  */  
   MXOriginalCheckRef:string,
      /**  MX Confirmation Code for special Cash Receipts  */  
   MXConfirmationCode:string,
      /**  MX Customer’s Bank ID  */  
   MXBankID:string,
      /**  Text entered by the user to indicate the reason Cash receipt was Reversed.  */  
   ReversedReason:string,
      /**  Credit Card Holder City.  */  
   CCCity:string,
      /**  Credit Card Holder State.  */  
   CCState:string,
      /**  ccToken  */  
   ccToken:string,
      /**  DepositBalance  */  
   DepositBalance:number,
      /**  DocDepositBalance  */  
   DocDepositBalance:number,
      /**  Rpt1DepositBalance  */  
   Rpt1DepositBalance:number,
      /**  Rpt2DepositBalance  */  
   Rpt2DepositBalance:number,
      /**  Rpt3DepositBalance  */  
   Rpt3DepositBalance:number,
      /**  Indicates this record is an adjustment CashHead.  */  
   Adjustment:boolean,
      /**  Reference to cash receipt which had been adjusted.  */  
   AdjustmentRef:number,
      /**  The reason for the adjustment entered by the user  */  
   AdjustmentReason:string,
      /**  Total Check Write Off Amount  */  
   WriteOffAmount:number,
      /**  DocWriteOffAmount  */  
   DocWriteOffAmount:number,
      /**  Rpt1WriteOffAmount  */  
   Rpt1WriteOffAmount:number,
      /**  Rpt2WriteOffAmount  */  
   Rpt2WriteOffAmount:number,
      /**  Rpt3WriteOffAmount  */  
   Rpt3WriteOffAmount:number,
      /**  Mexico Certified Timestamp  */  
   MXCertifiedTimestamp:string,
      /**  Mexico SAT Seal  */  
   MXSATSeal:string,
      /**  Mexico Digital Seal  */  
   MXDigitalSeal:string,
      /**  Mexico SAT Certificate Serial Number  */  
   MXSATCertificateSN:string,
      /**  Mexico Original String Timbre Fiscal Digital  */  
   MXOriginalStringTFD:string,
      /**  Mexico Certificate  */  
   MXCertificate:string,
      /**  Mexico Certificate Serial Number  */  
   MXCertificateSN:string,
      /**  SourceGroupID  */  
   SourceGroupID:string,
      /**  SourceHeadNum  */  
   SourceHeadNum:number,
      /**  Standard Entry Class Code  */  
   SEC:string,
      /**  ACH Transaction Code  */  
   ACHTranCode:number,
      /**  ID of the Customer's bank.  */  
   CustomerBankID:string,
      /**  The Bank account number for the Customer.  */  
   CustomerBankAcctNumber:string,
      /**  CustomerBankSwiftNum  */  
   CustomerBankSwiftNum:string,
      /**  The Bank account IBAN Code  */  
   CustomerBankIBANCode:string,
      /**  Name on the Bank Account.  */  
   CustomerBankNameOnAccount:string,
      /**  First address line of customer bank.  */  
   CustomerBankAddress1:string,
      /**  Second address line of customer bank.  */  
   CustomerBankAddress2:string,
      /**  Third address line of customer bank.  */  
   CustomerBankAddress3:string,
      /**  Bank City  */  
   CustomerBankCity:string,
      /**  Bank State/Prov  */  
   CustomerBankState:string,
      /**  Postal Code or zip code  */  
   CustomerBankPostalCode:string,
      /**  Bank account Country Number.  */  
   CustomerBankCountryNum:number,
      /**  ARRemittanceSlipPrinted  */  
   ARRemittanceSlipPrinted:boolean,
      /**  Customer Bank Name  */  
   CustomerBankName:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXEPaymentType  */  
   MXEPaymentType:string,
      /**  MXEPaymentCertificateNumber  */  
   MXEPaymentCertificateNumber:string,
      /**  MXEPaymentOriginalString  */  
   MXEPaymentOriginalString:string,
      /**  MXEPaymentDigitalSeal  */  
   MXEPaymentDigitalSeal:string,
      /**  Source  */  
   Source:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  GL Description for the Reverse process  */  
   RevDescription:string,
      /**  GL Description for AR - Apply Credit Memo  */  
   CMDescription:string,
      /**  Receipt Amount in Bank Currency  */  
   BankReceiptAmt:number,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstHeadNum  */  
   MXSubstHeadNum:number,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  E-invoice Service Provider Status  */  
   ELIEInvServiceProviderStatus:number,
      /**  E-invoice Status  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice Updated On  */  
   ELIEInvUpdatedOn:string,
      /**  Adjustment Customer Name  */  
   AdjustmentCustName:string,
      /**  Customer to which the new invoices will be applied.  */  
   AdjustmentCustNum:number,
      /**  Date the adjustment was made.  */  
   AdjustmentDate:string,
      /**  Displays the amount available to apply to the invoices.  */  
   AdjustmentDocUnAppliedAmt:number,
      /**  On Account  */  
   AdjustmentOnAccount:boolean,
      /**  Temp TranDocTypeID used when adjusting a Cash Rececipt  */  
   AdjustmentTranDocTypeID:string,
   AllocDepBal:number,
   AllowChgAfterPrint:boolean,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   AllowUpdSettlementCurr:boolean,
      /**  Amount to Allocate  */  
   AmtToAlloc:number,
   ApplyDate:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
      /**  Bank Currency Value  */  
   BankAmount:number,
   BankBaseXRateLabel:string,
   BankCurrencyCode:string,
      /**  Bank Currency Symbol  */  
   BankCurrSymbol:string,
   BankExchangeRate:number,
   BankRcptXRateLabel:string,
   BaseCurrencyCode:string,
      /**  Base Currency Symbol  */  
   BaseCurrSymbol:string,
      /**  Bill To Name  */  
   BillToName:string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   calcRate:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   CCAllowSales:boolean,
   CCApprovalNum:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Tokenized value of CSCID  */  
   CCCSCIDToken:string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   CCEnableAddress:boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   CCEnableCSC:boolean,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   CCIsTraining:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  Check Box on the UI to filter records by Central Collection flag  */  
   CentralCollectionCheck:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  */  
   CorrectionInv:boolean,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  */  
   CreditMemo:boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   CREProcessor:boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
      /**  Current Amount Selected on Invoice Select Tab  */  
   CurrAmtSelected:number,
   CurrencySwitch:boolean,
      /**  Displays the address of the customer that paid the receipt.  */  
   CustFullAddr:string,
   CustomerName:string,
   DisableFieldsForPCashDoc:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocAllocDepBal:number,
      /**  Doc Amount to Allocate  */  
   DocAmtToAlloc:number,
      /**  Displays the discount applied to the receipt.  */  
   DocDiscount:number,
      /**  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  */  
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   DocumentNum:number,
   DocWhldTax:number,
   DspBankBatchID:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   DspCMAmount:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspDocTranAmt:number,
   DspSalesOrderValue:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspTranAmt:number,
   EnableAssignLegNum:boolean,
      /**  Indicates if the option to get the default account is enable.  */  
   EnableGetDefaultAcct:boolean,
   EnableTranDocType:boolean,
   EnableTransactionDate:boolean,
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
   GLRefCodeDescription:string,
   HasLegNumCnfg:boolean,
      /**  The InvcHead legal number  */  
   InvcLegalNumber:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberDsp:string,
   LegalNumMessage:string,
      /**  Copied from OrderHed.LockRate  */  
   LockRate:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   ManualTaxAdj:boolean,
      /**  MXCancellationID  */  
   MXCancellationID:string,
   MXCancellationStatus:string,
      /**  MXECEPXml  */  
   MXECEPXml:string,
      /**  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  */  
   MXOriginalRefNum:string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   PayGateHostAddress:string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   PayGateNameSpace:string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   PayGatePublicKey:string,
      /**  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  */  
   ReceiptDate:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
   Rpt1AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt1TranTaxAmt:number,
   Rpt1WhldTax:number,
   Rpt2AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt2TranTaxAmt:number,
   Rpt2WhldTax:number,
   Rpt3AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt3TranTaxAmt:number,
   Rpt3WhldTax:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SalesOrderValue:number,
   SettlementXRateLabel:string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   SoldToCustomerName:string,
   SystemTranType:string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Transaction Amount less Tax Amount  */  
   TranTaxAmt:number,
      /**  Description of TranType  */  
   TranTypeDesc:string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   UnappliedAmountApplied:boolean,
   WhldTax:number,
   XRateLabel:string,
      /**  Displays the customer ID.  */  
   AdjustmentCustID:string,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Displays the address of the customer that paid the receipt with newline delimiter.  */  
   CustFullAddrFormatted:string,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding tax was manually modified.  */  
   WHTaxManualChange:boolean,
      /**  Payment type description, displayed in the Details page header.  */  
   TranTypeDescCaption:string,
   AdjustmentCustAddress:string,
      /**  Substitution Cash Receipt Group ID  */  
   MXSubstGroupId:string,
      /**  Substitution Cash Receipt CheckRef  */  
   MXSubstCheckRef:string,
      /**  Substitution Cash Receipt UUID  */  
   MXSubstFiscalFolio:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CardTypeDescription:string,
   CashBHedPosted:boolean,
   CashBHedCashBookNum:number,
   CashbookLineDescription:string,
   CMCurrencyCodeDocumentDesc:string,
   CMCurrencyCodeCurrName:string,
   CMCurrencyCodeCurrSymbol:string,
   CMCurrencyCodeCurrDesc:string,
   CMCurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CustNumInactive:boolean,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PCashDocDirection:string,
   PMUIDName:string,
   PMUIDMXSATCode:string,
   PMUIDSummarizePerCustomer:boolean,
   PMUIDType:number,
   RateGrpDescription:string,
   RcptCurrencyCodeCurrencyID:string,
   RcptCurrencyCodeDocumentDesc:string,
   RcptCurrencyCodeCurrDesc:string,
   RcptCurrencyCodeCurrSymbol:string,
   RcptCurrencyCodeCurrName:string,
   ReverseMXCancelReasonCode:string,
   ReverseMXCancellationMode:string,
   SourceTranDateTranDate:string,
   TaxRegionCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtApplyCreditMemoTableset{
   CashHead:Erp_Tablesets_CashHeadRow[],
   CashDtl:Erp_Tablesets_CashDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetByID_input{
   groupID:string,
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ApplyCreditMemoTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ApplyCreditMemoTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ApplyCreditMemoTableset[],
}

   /** Required : 
      @param currencyCode
      @param ds
   */  
export interface GetCurrencyInfo_input{
      /**  Proposed Currency Code  */  
   currencyCode:string,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface GetCurrencyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface GetDtlInvoiceInfo_input{
      /**  Proposed Invoice Number  */  
   invoiceNum:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface GetDtlInvoiceInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param docTranAmt
      @param ds
   */  
export interface GetDtlTranAmtInfo_input{
      /**  Proposed transaction amount  */  
   docTranAmt:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface GetDtlTranAmtInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param tranDate
      @param ds
   */  
export interface GetFiscalInfo_input{
      /**  Proposed Transaction Date  */  
   tranDate:string,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface GetFiscalInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param documentNum
      @param ds
   */  
export interface GetHdrDocumentInfo_input{
      /**  proposed Document Number  */  
   documentNum:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface GetHdrDocumentInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param docTranAmt
      @param ds
   */  
export interface GetHdrTranAmtInfo_input{
      /**  Proposed value change to the DocTranAmt field  */  
   docTranAmt:number,
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface GetHdrTranAmtInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param DocumentNum
      @param DocumentType
   */  
export interface GetInvcLegalNumber_input{
   DocumentNum:number,
   DocumentType:string,
}

export interface GetInvcLegalNumber_output{
   returnObj:string,
}

   /** Required : 
      @param CustNum
      @param CurrencyCode
   */  
export interface GetInvoiceNumPreloadFilter_input{
      /**  CashHead.CustNum  */  
   CustNum:number,
      /**  CashHead.CurrencyCode  */  
   CurrencyCode:string,
}

export interface GetInvoiceNumPreloadFilter_output{
parameters : {
      /**  output parameters  */  
   preLoadSearchFilter:string,
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
   returnObj:Erp_Tablesets_CashHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
      @param invoiceNum
   */  
export interface GetNewCashDtl_input{
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
   groupID:string,
   headNum:number,
   invoiceNum:number,
}

export interface GetNewCashDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewCashHead_input{
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
   groupID:string,
}

export interface GetNewCashHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param ds
      @param inGroupID
      @param inHeadNum
   */  
export interface GetNewCreditPayment_input{
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
      /**  Credit memo Group ID field  */  
   inGroupID:string,
      /**  CashHead.HeadNum field  */  
   inHeadNum:number,
}

export interface GetNewCreditPayment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param whereClauseCashHead
      @param whereClauseCashDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCashHead:string,
   whereClauseCashDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ApplyCreditMemoTableset[],
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
      @param documentType
   */  
export interface OnDocumentTypeChanging_input{
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
      /**  Document Type  */  
   documentType:string,
}

export interface OnDocumentTypeChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtApplyCreditMemoTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtApplyCreditMemoTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ApplyCreditMemoTableset[],
}
}

   /** Required : 
      @param inHeadNum
      @param inPNRef
      @param tranDate
      @param tranTime
      @param tranNum
   */  
export interface _ApplyCreditMemoCC_input{
      /**  CashReceipt ID  */  
   inHeadNum:number,
      /**  PNRef Number, blank if the line is a normal invoice credit  */  
   inPNRef:string,
   tranDate:string,
   tranTime:number,
   tranNum:number,
}

export interface _ApplyCreditMemoCC_output{
parameters : {
      /**  output parameters  */  
   peMessage:string,
}
}

