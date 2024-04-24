import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.BankFileImportSvc
// Description: BankFile class
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/$metadata", {
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
   Description: Get BankFileImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankFileImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpImportRow
   */  
export function get_BankFileImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankFileImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankFileImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankFileImport item
   Description: Calls GetByID to retrieve the BankFileImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankFileImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
   */  
export function get_BankFileImports_Company_GroupID(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashGrpImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashGrpImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankFileImport for the service
   Description: Calls UpdateExt to update BankFileImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankFileImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankFileImports_Company_GroupID(Company:string, GroupID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete BankFileImport item
   Description: Call UpdateExt to delete BankFileImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankFileImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankFileImports_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")", {
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
   Description: Get CashHeadImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashHeadImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadImportRow
   */  
export function get_BankFileImports_Company_GroupID_CashHeadImports(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")/CashHeadImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashHeadImport item
   Description: Calls GetByID to retrieve the CashHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   */  
export function get_BankFileImports_Company_GroupID_CashHeadImports_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CashHeadImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashHeadImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadImportRow
   */  
export function get_CashHeadImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashHeadImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashHeadImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashHeadImport item
   Description: Calls GetByID to retrieve the CashHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   */  
export function get_CashHeadImports_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashHeadImport for the service
   Description: Calls UpdateExt to update CashHeadImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashHeadImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashHeadImports_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete CashHeadImport item
   Description: Call UpdateExt to delete CashHeadImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashHeadImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashHeadImports_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Description: Get CashDtlImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtlImports1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlImportRow
   */  
export function get_CashHeadImports_Company_GroupID_HeadNum_CashDtlImports(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtlImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtlImport item
   Description: Calls GetByID to retrieve the CashDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlImport1
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   */  
export function get_CashHeadImports_Company_GroupID_HeadNum_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CashDtlImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtlImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlImportRow
   */  
export function get_CashDtlImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtlImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashDtlImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CashDtlImport item
   Description: Calls GetByID to retrieve the CashDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlImport
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   */  
export function get_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashDtlImport for the service
   Description: Calls UpdateExt to update CashDtlImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtlImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceRef Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
   Summary: Call UpdateExt to delete CashDtlImport item
   Description: Call UpdateExt to delete CashDtlImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtlImport
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
export function delete_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company:string, GroupID:string, HeadNum:string, InvoiceNum:string, InvoiceRef:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpImportListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportListRow)
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
export function get_GetRows(whereClauseCashGrpImport:string, whereClauseCashHeadImport:string, whereClauseCashDtlImport:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCashGrpImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashGrpImport=" + whereClauseCashGrpImport
   }
   if(typeof whereClauseCashHeadImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashHeadImport=" + whereClauseCashHeadImport
   }
   if(typeof whereClauseCashDtlImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashDtlImport=" + whereClauseCashDtlImport
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetRows" + params, {
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
export function get_GetByID(groupID:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetList" + params, {
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
   Summary: Invoke method ChangeARInvSelApplyAmt
   Description: Method to call when changing the apply amount on the invoice to match.
   OperationID: ChangeARInvSelApplyAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeARInvSelApplyAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeARInvSelApplyAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeARInvSelApplyAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeARInvSelApplyAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeARInvSelDocDiscAmt
   Description: Method to call when changing the discount amount for the invoice to match.
   OperationID: ChangeARInvSelDocDiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeARInvSelDocDiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeARInvSelDocDiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeARInvSelDocDiscAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeARInvSelDocDiscAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeARInvSelSelected
   Description: Method to call when selecting or deselecting an invoice to match.
   OperationID: ChangeARInvSelSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeARInvSelSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeARInvSelSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeARInvSelSelected(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeARInvSelSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCashDtlImportDocDiscount
   Description: Method to call when changing the discount on the payment detail.
   OperationID: ChangeCashDtlImportDocDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashDtlImportDocDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashDtlImportDocDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCashDtlImportDocDiscount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeCashDtlImportDocDiscount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCashDtlImportDocTranAmt
   Description: Method to call when changing the tran amount on the payment detail.
   OperationID: ChangeCashDtlImportDocTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashDtlImportDocTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashDtlImportDocTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCashDtlImportDocTranAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeCashDtlImportDocTranAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCashDtlImportInvoiceNum
   Description: Method to call when changing the invoice number.
   OperationID: ChangeCashDtlImportInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashDtlImportInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashDtlImportInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCashDtlImportInvoiceNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeCashDtlImportInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCashGrpImportBankAcctID
   Description: Method to call when changing the bank account.
   OperationID: ChangeCashGrpImportBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashGrpImportBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashGrpImportBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCashGrpImportBankAcctID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeCashGrpImportBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCashHeadImportCustID
   Description: Method to call when changing the customer.
   OperationID: ChangeCashHeadImportCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashHeadImportCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashHeadImportCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCashHeadImportCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeCashHeadImportCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCashHeadSettlementExRate
   Description: Method to call when changing the Settlement Exchange rate.
   OperationID: ChangeCashHeadSettlementExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashHeadSettlementExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashHeadSettlementExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCashHeadSettlementExRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ChangeCashHeadSettlementExRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreatePymtForInvoices
   Description: Create payments for selected invoices.
   OperationID: CreatePymtForInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePymtForInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePymtForInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePymtForInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CreatePymtForInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteCreditMemos
   Description: Delete Credit Memos
   OperationID: DeleteCreditMemos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCreditMemos_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCreditMemos(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/DeleteCreditMemos", {
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
   Summary: Invoke method DeletePaymantsWithErrors
   Description: Delete Paymants with errors
   OperationID: DeletePaymantsWithErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePaymantsWithErrors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePaymantsWithErrors_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePaymantsWithErrors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/DeletePaymantsWithErrors", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankFileImportParam
   Description: Returns record in BankFileImportParam dataset
   OperationID: GetBankFileImportParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankFileImportParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFileImportParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankFileImportParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetBankFileImportParam", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportBankFileExpress
   OperationID: ImportBankFileExpress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBankFileExpress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBankFileExpress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportBankFileExpress(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ImportBankFileExpress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetBankFileImportExpressGroup
   Description: Reset status of group in case payments are hanged in Generation of Posting status.
   OperationID: ResetBankFileImportExpressGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetBankFileImportExpressGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetBankFileImportExpressGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetBankFileImportExpressGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ResetBankFileImportExpressGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupInfo
   Description: Returns current status of Group
   OperationID: GetGroupInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetGroupInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTranTypeActiveRevision
   Description: Check AR Payment transaction Type: Active Revision, Send To RJ flag and PE Log
   OperationID: CheckTranTypeActiveRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTranTypeActiveRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTranTypeActiveRevision(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CheckTranTypeActiveRevision", {
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
   Summary: Invoke method ImportBankFile
   Description: Imports a bank file
   OperationID: ImportBankFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBankFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBankFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportBankFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ImportBankFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchCHCashHeadImport
   Description: Method to call to match CashHeadImport record with invalid ISR Reference Number to invoices (for Switzerland).
   OperationID: MatchCHCashHeadImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchCHCashHeadImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchCHCashHeadImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchCHCashHeadImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/MatchCHCashHeadImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchPayments
   Description: Method to call to automatically match the invoices, called after import
   OperationID: MatchPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchPayments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/MatchPayments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessReceipts
   Description: Method to call to automatically process receipts
   OperationID: ProcessReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessReceipts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/ProcessReceipts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectInvoices
   Description: Read InvcHead records and create ARInvSel records if they meet the selection criteria.
   OperationID: SelectInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/SelectInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockGroup
   Description: Should be call before GetByID to lock the Group.
   OperationID: LockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/LockGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockGroup
   Description: Unlock the group.  Only user who locked the group can unlock it.
   OperationID: UnlockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/UnlockGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashGrpImportNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewCashGrpImportNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpImportNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpImportNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrpImportNoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetNewCashGrpImportNoLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashGrpImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashGrpImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrpImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetNewCashGrpImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHeadImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHeadImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHeadImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHeadImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHeadImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetNewCashHeadImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashDtlImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtlImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashDtlImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtlImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashDtlImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetNewCashDtlImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashDtlImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashGrpImportListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashGrpImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadImportRow[],
}

export interface Erp_Tablesets_CashDtlImportRow{
      /**  Company  */  
   "Company":string,
      /**  GroupID  */  
   "GroupID":string,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  InvoiceNum  */  
   "InvoiceNum":number,
      /**  InvoiceRef  */  
   "InvoiceRef":number,
      /**  TranType  */  
   "TranType":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalPeriod  */  
   "FiscalPeriod":number,
      /**  GLPosted  */  
   "GLPosted":boolean,
      /**  TranDate  */  
   "TranDate":string,
      /**  CheckRef  */  
   "CheckRef":string,
      /**  TranAmt  */  
   "TranAmt":number,
      /**  DocTranAmt  */  
   "DocTranAmt":number,
      /**  CustNum  */  
   "CustNum":number,
      /**  Discount  */  
   "Discount":number,
      /**  DocDiscount  */  
   "DocDiscount":number,
      /**  Comment  */  
   "Comment":string,
      /**  Reference  */  
   "Reference":string,
      /**  ExchangeRate  */  
   "ExchangeRate":number,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  GLRefType  */  
   "GLRefType":string,
      /**  GLRefCode  */  
   "GLRefCode":string,
      /**  DebitNote  */  
   "DebitNote":boolean,
      /**  DNComments  */  
   "DNComments":string,
      /**  DNAmount  */  
   "DNAmount":number,
      /**  DocDnAmount  */  
   "DocDnAmount":number,
      /**  DNCustNbr  */  
   "DNCustNbr":string,
      /**  RoundDiff  */  
   "RoundDiff":number,
      /**  Rpt1Discount  */  
   "Rpt1Discount":number,
      /**  Rpt2Discount  */  
   "Rpt2Discount":number,
      /**  Rpt3Discount  */  
   "Rpt3Discount":number,
      /**  Rpt1DnAmount  */  
   "Rpt1DnAmount":number,
      /**  Rpt2DnAmount  */  
   "Rpt2DnAmount":number,
      /**  Rpt3DnAmount  */  
   "Rpt3DnAmount":number,
      /**  Rpt1TranAmt  */  
   "Rpt1TranAmt":number,
      /**  Rpt2TranAmt  */  
   "Rpt2TranAmt":number,
      /**  Rpt3TranAmt  */  
   "Rpt3TranAmt":number,
      /**  RateGrpCode  */  
   "RateGrpCode":string,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  TaxRegionCode  */  
   "TaxRegionCode":string,
      /**  GetDfltTaxIds  */  
   "GetDfltTaxIds":boolean,
      /**  WithholdAmt  */  
   "WithholdAmt":number,
      /**  DocWithholdAmt  */  
   "DocWithholdAmt":number,
      /**  Rpt1WithholdAmt  */  
   "Rpt1WithholdAmt":number,
      /**  Rpt2WithholdAmt  */  
   "Rpt2WithholdAmt":number,
      /**  Rpt3WithholdAmt  */  
   "Rpt3WithholdAmt":number,
      /**  SelfAssessAmt  */  
   "SelfAssessAmt":number,
      /**  DocSelfAssessAmt  */  
   "DocSelfAssessAmt":number,
      /**  Rpt1SelfAssessAmt  */  
   "Rpt1SelfAssessAmt":number,
      /**  Rpt2SelfAssessAmt  */  
   "Rpt2SelfAssessAmt":number,
      /**  Rpt3SelfAssessAmt  */  
   "Rpt3SelfAssessAmt":number,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  DocTaxAmt  */  
   "DocTaxAmt":number,
      /**  Rpt1TaxAmt  */  
   "Rpt1TaxAmt":number,
      /**  Rpt2TaxAmt  */  
   "Rpt2TaxAmt":number,
      /**  Rpt3TaxAmt  */  
   "Rpt3TaxAmt":number,
      /**  RedStorno  */  
   "RedStorno":boolean,
      /**  TaxReceiptDate  */  
   "TaxReceiptDate":string,
      /**  TaxReceiptNo  */  
   "TaxReceiptNo":string,
      /**  WHTCertificateDate  */  
   "WHTCertificateDate":string,
      /**  WHTCertificateNo  */  
   "WHTCertificateNo":string,
      /**  PCashDeskID  */  
   "PCashDeskID":string,
      /**  GainLossType  */  
   "GainLossType":string,
      /**  PCashRefNum  */  
   "PCashRefNum":number,
      /**  ReverseGL  */  
   "ReverseGL":boolean,
      /**  RevalueDate  */  
   "RevalueDate":string,
      /**  RevalueBal  */  
   "RevalueBal":number,
      /**  DocRevalueBal  */  
   "DocRevalueBal":number,
      /**  Rpt1RevalueBal  */  
   "Rpt1RevalueBal":number,
      /**  Rpt2RevalueBal  */  
   "Rpt2RevalueBal":number,
      /**  Rpt3RevalueBal  */  
   "Rpt3RevalueBal":number,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  MainSite  */  
   "MainSite":boolean,
      /**  SiteCode  */  
   "SiteCode":string,
      /**  BranchID  */  
   "BranchID":string,
      /**  InvoiceDate  */  
   "InvoiceDate":string,
      /**  TaxRemarks  */  
   "TaxRemarks":string,
      /**  NonDeductCode  */  
   "NonDeductCode":string,
      /**  NonDeductAmt  */  
   "NonDeductAmt":number,
      /**  NonDeductDocAmt  */  
   "NonDeductDocAmt":number,
      /**  NonDeductRpt1Amt  */  
   "NonDeductRpt1Amt":number,
      /**  NonDeductRpt2Amt  */  
   "NonDeductRpt2Amt":number,
      /**  NonDeductRpt3Amt  */  
   "NonDeductRpt3Amt":number,
      /**  AssetTypeCode  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  CreditCard  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  InvDueDate  */  
   "InvDueDate":string,
      /**  ManualMatch  */  
   "ManualMatch":boolean,
      /**  BillingNumber  */  
   "BillingNumber":string,
      /**  SEPADDMsgID  */  
   "SEPADDMsgID":string,
      /**  SEPADDPmtID  */  
   "SEPADDPmtID":string,
      /**  PmtDueDate  */  
   "PmtDueDate":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  MXPaymentNum  */  
   "MXPaymentNum":number,
      /**  WriteOffHeadNumRef  */  
   "WriteOffHeadNumRef":number,
      /**  EpicorFSA  */  
   "EpicorFSA":boolean,
      /**  TaxableAdjustment  */  
   "TaxableAdjustment":boolean,
   "BankNetPay":number,
   "DispCurrencyCode":string,
   "DocNetPay":number,
   "InvPayStatus":string,
   "DocRemainInvBal":number,
   "InvOpenBalance":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashGrpImportListRow{
      /**  Company  */  
   "Company":string,
      /**  GroupID  */  
   "GroupID":string,
      /**  TranDate  */  
   "TranDate":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalPeriod  */  
   "FiscalPeriod":number,
      /**  ActiveUserID  */  
   "ActiveUserID":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  Cashbook  */  
   "Cashbook":boolean,
      /**  DebNoteOnly  */  
   "DebNoteOnly":boolean,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  PromissoryNote  */  
   "PromissoryNote":boolean,
      /**  PMUID  */  
   "PMUID":number,
      /**  EIPaymSent  */  
   "EIPaymSent":boolean,
      /**  PIStatus  */  
   "PIStatus":string,
      /**  PIStatusGrp  */  
   "PIStatusGrp":boolean,
      /**  PIType  */  
   "PIType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Bank Branch Code  */  
   "BankAcctBankBranchCode":string,
      /**  Swift Number or ABA Routing Number  */  
   "BankAcctBankIdentifier":string,
      /**  The Bank's full name.  */  
   "BankAcctBankName":string,
      /**  The account number for the bank account. Used for reference only.  */  
   "BankAcctCheckingAccount":string,
      /**  Currency.CurrencyCode of the currency that the bank account is denominated in.  */  
   "BankAcctCurrencyCode":string,
      /**  Full description of the bank account.  */  
   "BankAcctDescription":string,
      /**  IBAN Code  */  
   "BankAcctIBANCode":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
      /**  Name of the payment method  */  
   "PayMethodName":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PayMethodSummarizePerCustomer":boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PayMethodType":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashGrpImportRow{
      /**  Company  */  
   "Company":string,
      /**  GroupID  */  
   "GroupID":string,
      /**  TranDate  */  
   "TranDate":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalPeriod  */  
   "FiscalPeriod":number,
      /**  ActiveUserID  */  
   "ActiveUserID":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  Cashbook  */  
   "Cashbook":boolean,
      /**  DebNoteOnly  */  
   "DebNoteOnly":boolean,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  PromissoryNote  */  
   "PromissoryNote":boolean,
      /**  PMUID  */  
   "PMUID":number,
      /**  EIPaymSent  */  
   "EIPaymSent":boolean,
      /**  PIStatus  */  
   "PIStatus":string,
      /**  PIStatusGrp  */  
   "PIStatusGrp":boolean,
      /**  PIType  */  
   "PIType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  BankBatchID  */  
   "BankBatchID":string,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  ProcessStatus  */  
   "ProcessStatus":string,
      /**  ImportFileName  */  
   "ImportFileName":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrDesc":string,
   "LockForChanges":boolean,
   "ProcessButtonEnabled":boolean,
   "ProcessStatusDisplay":string,
      /**  Enable matching Credit Memo with Invoice  */  
   "EnableMatchCMemoWithInv":boolean,
   "BitFlag":number,
   "BankAcctBankBranchCode":string,
   "BankAcctCurrencyCode":string,
   "BankAcctDescription":string,
   "BankAcctBankName":string,
   "BankAcctBankIdentifier":string,
   "BankAcctIBANCode":string,
   "BankAcctCheckingAccount":string,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "PayMethodType":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadImportRow{
      /**  Company  */  
   "Company":string,
      /**  GroupID  */  
   "GroupID":string,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  Posted  */  
   "Posted":boolean,
      /**  TranType  */  
   "TranType":string,
      /**  CheckRef  */  
   "CheckRef":string,
      /**  OrderNum  */  
   "OrderNum":number,
      /**  InvoiceNum  */  
   "InvoiceNum":number,
      /**  TranAmt  */  
   "TranAmt":number,
      /**  DocTranAmt  */  
   "DocTranAmt":number,
      /**  CustID  */  
   "CustID":string,
      /**  TranDate  */  
   "TranDate":string,
      /**  CustNum  */  
   "CustNum":number,
      /**  UnAppliedAmt  */  
   "UnAppliedAmt":number,
      /**  DocUnAppliedAmt  */  
   "DocUnAppliedAmt":number,
      /**  AppliedAmt  */  
   "AppliedAmt":number,
      /**  DocAppliedAmt  */  
   "DocAppliedAmt":number,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalPeriod  */  
   "FiscalPeriod":number,
      /**  Reference  */  
   "Reference":string,
      /**  GLPosted  */  
   "GLPosted":boolean,
      /**  CreditMemoNum  */  
   "CreditMemoNum":number,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  ExchangeRate  */  
   "ExchangeRate":number,
      /**  TaxRegionCode  */  
   "TaxRegionCode":string,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  DocTaxAmt  */  
   "DocTaxAmt":number,
      /**  CashBookNum  */  
   "CashBookNum":number,
      /**  CashbookLine  */  
   "CashbookLine":number,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  ExternalID  */  
   "ExternalID":string,
      /**  GLRefType  */  
   "GLRefType":string,
      /**  GLRefCode  */  
   "GLRefCode":string,
      /**  CardMemberName  */  
   "CardMemberName":string,
      /**  CardNumber  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  ExpirationMonth  */  
   "ExpirationMonth":number,
      /**  ExpirationYear  */  
   "ExpirationYear":number,
      /**  CardID  */  
   "CardID":string,
      /**  CardmemberReference  */  
   "CardmemberReference":string,
      /**  ProcessCard  */  
   "ProcessCard":string,
      /**  CCAmount  */  
   "CCAmount":number,
      /**  CCFreight  */  
   "CCFreight":number,
      /**  CCTax  */  
   "CCTax":number,
      /**  CCTotal  */  
   "CCTotal":number,
      /**  CCDocAmount  */  
   "CCDocAmount":number,
      /**  CCDocFreight  */  
   "CCDocFreight":number,
      /**  CCDocTax  */  
   "CCDocTax":number,
      /**  CCDocTotal  */  
   "CCDocTotal":number,
      /**  CCStreetAddr  */  
   "CCStreetAddr":string,
      /**  CCZip  */  
   "CCZip":string,
      /**  DebNoteOnly  */  
   "DebNoteOnly":boolean,
      /**  Rpt1AppliedAmt  */  
   "Rpt1AppliedAmt":number,
      /**  Rpt2AppliedAmt  */  
   "Rpt2AppliedAmt":number,
      /**  Rpt3AppliedAmt  */  
   "Rpt3AppliedAmt":number,
      /**  Rpt1TaxAmt  */  
   "Rpt1TaxAmt":number,
      /**  Rpt2TaxAmt  */  
   "Rpt2TaxAmt":number,
      /**  Rpt3TaxAmt  */  
   "Rpt3TaxAmt":number,
      /**  Rpt1TranAmt  */  
   "Rpt1TranAmt":number,
      /**  Rpt2TranAmt  */  
   "Rpt2TranAmt":number,
      /**  Rpt3TranAmt  */  
   "Rpt3TranAmt":number,
      /**  Rpt1UnAppliedAmt  */  
   "Rpt1UnAppliedAmt":number,
      /**  Rpt2UnAppliedAmt  */  
   "Rpt2UnAppliedAmt":number,
      /**  Rpt3UnAppliedAmt  */  
   "Rpt3UnAppliedAmt":number,
      /**  RateGrpCode  */  
   "RateGrpCode":string,
      /**  DocDepApplied  */  
   "DocDepApplied":number,
      /**  Rpt1CCAmount  */  
   "Rpt1CCAmount":number,
      /**  Rpt2CCAmount  */  
   "Rpt2CCAmount":number,
      /**  Rpt3CCAmount  */  
   "Rpt3CCAmount":number,
      /**  Rpt1CCFreight  */  
   "Rpt1CCFreight":number,
      /**  Rpt2CCFreight  */  
   "Rpt2CCFreight":number,
      /**  Rpt3CCFreight  */  
   "Rpt3CCFreight":number,
      /**  Rpt1CCTax  */  
   "Rpt1CCTax":number,
      /**  Rpt2CCTax  */  
   "Rpt2CCTax":number,
      /**  Rpt3CCTax  */  
   "Rpt3CCTax":number,
      /**  Rpt1CCTotal  */  
   "Rpt1CCTotal":number,
      /**  Rpt2CCTotal  */  
   "Rpt2CCTotal":number,
      /**  Rpt3CCTotal  */  
   "Rpt3CCTotal":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  ReadyToCalc  */  
   "ReadyToCalc":boolean,
      /**  RecalcBeforePost  */  
   "RecalcBeforePost":boolean,
      /**  GetDfltTaxIds  */  
   "GetDfltTaxIds":boolean,
      /**  WithholdAmt  */  
   "WithholdAmt":number,
      /**  DocWithholdAmt  */  
   "DocWithholdAmt":number,
      /**  Rpt1WithholdAmt  */  
   "Rpt1WithholdAmt":number,
      /**  Rpt2WithholdAmt  */  
   "Rpt2WithholdAmt":number,
      /**  Rpt3WithholdAmt  */  
   "Rpt3WithholdAmt":number,
      /**  SelfAssessAmt  */  
   "SelfAssessAmt":number,
      /**  DocSelfAssessAmt  */  
   "DocSelfAssessAmt":number,
      /**  Rpt1SelfAssessAmt  */  
   "Rpt1SelfAssessAmt":number,
      /**  Rpt2SelfAssessAmt  */  
   "Rpt2SelfAssessAmt":number,
      /**  Rpt3SelfAssessAmt  */  
   "Rpt3SelfAssessAmt":number,
      /**  ReceiptCurrencyCode  */  
   "ReceiptCurrencyCode":string,
      /**  ReceiptAmt  */  
   "ReceiptAmt":number,
      /**  BankRcptExchangeRate  */  
   "BankRcptExchangeRate":number,
      /**  SettlementExchangeRate  */  
   "SettlementExchangeRate":number,
      /**  CMCurrencyCode  */  
   "CMCurrencyCode":string,
      /**  CMAmount  */  
   "CMAmount":number,
      /**  ReverseRef  */  
   "ReverseRef":number,
      /**  ReverseDate  */  
   "ReverseDate":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  TaxWhld  */  
   "TaxWhld":number,
      /**  DiscountDate  */  
   "DiscountDate":string,
      /**  TaxWhldCalc  */  
   "TaxWhldCalc":number,
      /**  ContractDate  */  
   "ContractDate":string,
      /**  Plant  */  
   "Plant":string,
      /**  UnallocatedAmt  */  
   "UnallocatedAmt":number,
      /**  DocUnallocatedAmt  */  
   "DocUnallocatedAmt":number,
      /**  Rpt1UnallocatedAmt  */  
   "Rpt1UnallocatedAmt":number,
      /**  Rpt2UnallocatedAmt  */  
   "Rpt2UnallocatedAmt":number,
      /**  Rpt3UnallocatedAmt  */  
   "Rpt3UnallocatedAmt":number,
      /**  ApplyHeadNum  */  
   "ApplyHeadNum":number,
      /**  AllocatedAmt  */  
   "AllocatedAmt":number,
      /**  DocAllocatedAmt  */  
   "DocAllocatedAmt":number,
      /**  Rpt1AllocatedAmt  */  
   "Rpt1AllocatedAmt":number,
      /**  Rpt2AllocatedAmt  */  
   "Rpt2AllocatedAmt":number,
      /**  Rpt3AllocatedAmt  */  
   "Rpt3AllocatedAmt":number,
      /**  Comment  */  
   "Comment":string,
      /**  PMUID  */  
   "PMUID":number,
      /**  PCashDeskID  */  
   "PCashDeskID":string,
      /**  BankTranID  */  
   "BankTranID":string,
      /**  PCashRefNum  */  
   "PCashRefNum":number,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  MainSite  */  
   "MainSite":boolean,
      /**  SiteCode  */  
   "SiteCode":string,
      /**  BranchID  */  
   "BranchID":string,
      /**  InvoiceDate  */  
   "InvoiceDate":string,
      /**  TaxRemarks  */  
   "TaxRemarks":string,
      /**  NonDeductCode  */  
   "NonDeductCode":string,
      /**  NonDeductAmt  */  
   "NonDeductAmt":number,
      /**  NonDeductDocAmt  */  
   "NonDeductDocAmt":number,
      /**  NonDeductRpt1Amt  */  
   "NonDeductRpt1Amt":number,
      /**  NonDeductRpt2Amt  */  
   "NonDeductRpt2Amt":number,
      /**  NonDeductRpt3Amt  */  
   "NonDeductRpt3Amt":number,
      /**  AssetTypeCode  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  CreditCard  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  BankTransDate  */  
   "BankTransDate":string,
      /**  CustNameFromFile  */  
   "CustNameFromFile":string,
      /**  OCRNumber  */  
   "OCRNumber":string,
      /**  ImportLineStatus  */  
   "ImportLineStatus":string,
      /**  ImportLineError  */  
   "ImportLineError":string,
      /**  DescFromImport  */  
   "DescFromImport":string,
      /**  InvNumList  */  
   "InvNumList":string,
      /**  InvAmtList  */  
   "InvAmtList":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  ManualMatch  */  
   "ManualMatch":boolean,
      /**  CreditMemo  */  
   "CreditMemo":boolean,
      /**  CMNum  */  
   "CMNum":number,
      /**  CMDocAmount  */  
   "CMDocAmount":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  CHISRPartyID  */  
   "CHISRPartyID":string,
      /**  CHISRRefNumAvailableToChange  */  
   "CHISRRefNumAvailableToChange":boolean,
      /**  BankBatchID  */  
   "BankBatchID":string,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  RcptCurAppliedAmt  */  
   "RcptCurAppliedAmt":number,
      /**  RcptCurUnAppliedAmt  */  
   "RcptCurUnAppliedAmt":number,
      /**  MXAccountNumber  */  
   "MXAccountNumber":string,
      /**  MXPaidAs  */  
   "MXPaidAs":string,
      /**  MXPaySupplementFlag  */  
   "MXPaySupplementFlag":boolean,
      /**  LockboxID  */  
   "LockboxID":string,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  MXOriginalCheckRef  */  
   "MXOriginalCheckRef":string,
      /**  MXConfirmationCode  */  
   "MXConfirmationCode":string,
      /**  MXBankID  */  
   "MXBankID":string,
      /**  ReversedReason  */  
   "ReversedReason":string,
      /**  CCCity  */  
   "CCCity":string,
      /**  CCState  */  
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
      /**  Adjustment  */  
   "Adjustment":boolean,
      /**  AdjustmentRef  */  
   "AdjustmentRef":number,
      /**  AdjustmentReason  */  
   "AdjustmentReason":string,
      /**  WriteOffAmount  */  
   "WriteOffAmount":number,
      /**  DocWriteOffAmount  */  
   "DocWriteOffAmount":number,
      /**  Rpt1WriteOffAmount  */  
   "Rpt1WriteOffAmount":number,
      /**  Rpt2WriteOffAmount  */  
   "Rpt2WriteOffAmount":number,
      /**  Rpt3WriteOffAmount  */  
   "Rpt3WriteOffAmount":number,
      /**  MXCertifiedTimestamp  */  
   "MXCertifiedTimestamp":string,
      /**  MXSATSeal  */  
   "MXSATSeal":string,
      /**  MXDigitalSeal  */  
   "MXDigitalSeal":string,
      /**  MXSATCertificateSN  */  
   "MXSATCertificateSN":string,
      /**  MXOriginalStringTFD  */  
   "MXOriginalStringTFD":string,
      /**  MXCertificate  */  
   "MXCertificate":string,
      /**  MXCertificateSN  */  
   "MXCertificateSN":string,
      /**  SourceGroupID  */  
   "SourceGroupID":string,
      /**  SourceHeadNum  */  
   "SourceHeadNum":number,
      /**  SEC  */  
   "SEC":string,
      /**  ACHTranCode  */  
   "ACHTranCode":number,
      /**  CustomerBankID  */  
   "CustomerBankID":string,
      /**  CustomerBankAcctNumber  */  
   "CustomerBankAcctNumber":string,
      /**  CustomerBankSwiftNum  */  
   "CustomerBankSwiftNum":string,
      /**  CustomerBankIBANCode  */  
   "CustomerBankIBANCode":string,
      /**  CustomerBankNameOnAccount  */  
   "CustomerBankNameOnAccount":string,
      /**  CustomerBankAddress1  */  
   "CustomerBankAddress1":string,
      /**  CustomerBankAddress2  */  
   "CustomerBankAddress2":string,
      /**  CustomerBankAddress3  */  
   "CustomerBankAddress3":string,
      /**  CustomerBankCity  */  
   "CustomerBankCity":string,
      /**  CustomerBankState  */  
   "CustomerBankState":string,
      /**  CustomerBankPostalCode  */  
   "CustomerBankPostalCode":string,
      /**  CustomerBankCountryNum  */  
   "CustomerBankCountryNum":number,
      /**  ARRemittanceSlipPrinted  */  
   "ARRemittanceSlipPrinted":boolean,
      /**  CustomerBankName  */  
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
      /**  Cash Rec Group ID  */  
   "CashRecGroupID":string,
      /**  Cash Rec Head Num  */  
   "CashRecHeadNum":number,
      /**  RvJrnUID  */  
   "RvJrnUID":number,
      /**  ProcessStatus  */  
   "ProcessStatus":string,
      /**  NettingID  */  
   "NettingID":number,
      /**  GL Description for the Reverse process  */  
   "RevDescription":string,
      /**  GL Description for AR - Apply Credit Memo  */  
   "CMDescription":string,
      /**  BankReceiptAmt  */  
   "BankReceiptAmt":number,
      /**  MXCancelReasonCode  */  
   "MXCancelReasonCode":string,
      /**  MXSubstHeadNum  */  
   "MXSubstHeadNum":number,
      /**  MXCancellationMode  */  
   "MXCancellationMode":string,
   "BankRcptXRateLabel":string,
      /**  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  */  
   "CHImportStatus":boolean,
      /**  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  */  
   "EnableCust":boolean,
   "SettlementXRateLabel":string,
   "LockForChanges":boolean,
   "ProcessStatusDisplay":string,
   "BitFlag":number,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "RcptCurrencyCurrSymbol":string,
   "SettlementCurrencyCurrSymbol":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ProposedApplyAmt
      @param inInvoiceNum
      @param ds
   */  
export interface ChangeARInvSelApplyAmt_input{
      /**  The proposed apply amount  */  
   ProposedApplyAmt:number,
      /**  The invoice number  */  
   inInvoiceNum:number,
   ds:Erp_Tablesets_ARInvSelTableset[],
}

export interface ChangeARInvSelApplyAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSelTableset[],
}
}

   /** Required : 
      @param ProposedDocDiscAmt
      @param inInvoiceNum
      @param ds
   */  
export interface ChangeARInvSelDocDiscAmt_input{
      /**  The proposed doc discount amount  */  
   ProposedDocDiscAmt:number,
      /**  The invoice number  */  
   inInvoiceNum:number,
   ds:Erp_Tablesets_ARInvSelTableset[],
}

export interface ChangeARInvSelDocDiscAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSelTableset[],
}
}

   /** Required : 
      @param ProposedSelected
      @param inInvoiceNum
      @param inTranDate
      @param inCreditMemo
      @param ds
   */  
export interface ChangeARInvSelSelected_input{
      /**  The proposed selected value  */  
   ProposedSelected:boolean,
      /**  The invoice number  */  
   inInvoiceNum:number,
      /**  The tran date  */  
   inTranDate:string,
      /**  Credit Memo  */  
   inCreditMemo:boolean,
   ds:Erp_Tablesets_ARInvSelTableset[],
}

export interface ChangeARInvSelSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSelTableset[],
}
}

   /** Required : 
      @param ProposedDocDiscount
      @param ds
   */  
export interface ChangeCashDtlImportDocDiscount_input{
      /**  The proposed discount  */  
   ProposedDocDiscount:number,
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface ChangeCashDtlImportDocDiscount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param ProposedDocTranAmt
      @param ds
   */  
export interface ChangeCashDtlImportDocTranAmt_input{
      /**  The proposed tran amt  */  
   ProposedDocTranAmt:number,
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface ChangeCashDtlImportDocTranAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param ProposedInvoiceNum
      @param ds
   */  
export interface ChangeCashDtlImportInvoiceNum_input{
      /**  The proposed invoice number  */  
   ProposedInvoiceNum:number,
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface ChangeCashDtlImportInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param ProposedBankAcctID
      @param ds
   */  
export interface ChangeCashGrpImportBankAcctID_input{
      /**  The proposed bank account id  */  
   ProposedBankAcctID:string,
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface ChangeCashGrpImportBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param ProposedCustID
      @param ds
   */  
export interface ChangeCashHeadImportCustID_input{
      /**  The proposed bank account id  */  
   ProposedCustID:string,
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface ChangeCashHeadImportCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param proposedExRate
      @param ds
   */  
export interface ChangeCashHeadSettlementExRate_input{
      /**  The proposed settlement exchange rate  */  
   proposedExRate:number,
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface ChangeCashHeadSettlementExRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

export interface CheckTranTypeActiveRevision_output{
parameters : {
      /**  output parameters  */  
   NoActiveRevision:boolean,
   SendToReviewJournal:boolean,
   PELogEnabled:boolean,
}
}

   /** Required : 
      @param pcGroupID
      @param pcHeadNum
      @param ds
   */  
export interface CreatePymtForInvoices_input{
      /**  Cash Receipt Group ID  */  
   pcGroupID:string,
      /**  Imported payment to create the line for  */  
   pcHeadNum:number,
   ds:Erp_Tablesets_ARInvSelTableset[],
}

export interface CreatePymtForInvoices_output{
   returnObj:Erp_Tablesets_BankFileImportTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSelTableset[],
}
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

export interface DeleteCreditMemos_output{
}

   /** Required : 
      @param ipGroupID
   */  
export interface DeletePaymantsWithErrors_input{
      /**  Group ID  */  
   ipGroupID:string,
}

export interface DeletePaymantsWithErrors_output{
}

export interface Erp_Tablesets_ARInvSelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   ClosedDate:string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   UnappliedCash:boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   DeferredRevenue:boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   OrderNum:number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Defaults from sales order ORderHed.FOB  */  
   FOB:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   FiscalPeriod:number,
      /**  Once posted, maintenance is not allowed.  */  
   GLPosted:boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DepositCredit:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DocDepositCredit:number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   SalesRepList:string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   RefCancelled:number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   RefCancelledBy:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   PayDiscDate:string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   PayDiscAmt:number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   DocPayDiscAmt:number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   LineType:string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**  The Site that the invoice is relate to.  */  
   Plant:string,
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
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   DNComments:string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   DebitNote:boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   SoldToCustNum:number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   Consolidated:boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   BillToInvoiceAddress:boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   SoldToInvoiceAddress:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm1:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm2:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm3:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm4:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm5:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate1:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate2:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate3:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate4:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate5:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales1:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales2:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales3:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales4:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales5:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit1:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit2:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit3:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit4:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit5:number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   CMType:string,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding in Customer currency  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3DepGainLoss:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   LastChrgCalcDate:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Total Finance Charge amount.  */  
   TotFinChrg:number,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   BlockedFinChrg:boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   BlockedFinChrgReason:string,
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
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   BlockedRemLetters:boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   BlockedRemLettersReason:string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Currency Rate Date  */  
   CurrRateDate:string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   UseAltBillTo:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   SEBankRef:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Reversal Doucment Amount  */  
   ReversalDocAmount:number,
      /**  Original Due Date at posting time  */  
   OrigDueDate:string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   HeadNum:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  The free text field which can contain reference (such as Contract)  */  
   ContractRef:string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   OurBank:string,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   PBProjectID:string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   DepositAmt:number,
      /**   Taiwan Localization
Export Bill Number  */  
   GUIExportBillNumber:string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   DocDepositAmt:number,
      /**   Taiwan Localization
Date of Export  */  
   GUIDateOfExport:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   Rpt1DepositAmt:number,
      /**   Taiwan Localization
Export Type  */  
   GUIExportType:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   Rpt2DepositAmt:number,
      /**   Taiwan Localization
Export Mark  */  
   GUIExportMark:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   Rpt3DepositAmt:number,
      /**   Taiwan Localization
Export Bill Type  */  
   GUIExportBillType:string,
      /**  Deposit unallocated amount in base currency  */  
   DepUnallocatedAmt:number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Deposit unallocated amount in document currency  */  
   DocDepUnallocatedAmt:number,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   Rpt1DepUnallocatedAmt:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   Rpt2DepUnallocatedAmt:number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   ReadyToBill:boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   Rpt3DepUnallocatedAmt:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Customer Agent Name  */  
   CustAgentName:string,
      /**  Customer Agent Tax Region Number  */  
   CustAgentTaxRegNo:string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   ExportType:string,
      /**  Export Report Number  */  
   ExportReportNo:string,
      /**  Real Estate Number  */  
   RealEstateNo:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  CycleCode  */  
   CycleCode:string,
      /**  Duration  */  
   Duration:number,
      /**  EndDate  */  
   EndDate:string,
      /**  MaxValueAmt  */  
   MaxValueAmt:number,
      /**  DocMaxValueAmt  */  
   DocMaxValueAmt:number,
      /**  Rpt1MaxValueAmt  */  
   Rpt1MaxValueAmt:number,
      /**  Rpt2MaxValueAmt  */  
   Rpt2MaxValueAmt:number,
      /**  Rpt3MaxValueAmt  */  
   Rpt3MaxValueAmt:number,
      /**  HoldInvoice  */  
   HoldInvoice:boolean,
      /**  CopyLatestInvoice  */  
   CopyLatestInvoice:boolean,
      /**  OverrideEndDate  */  
   OverrideEndDate:boolean,
      /**  CycleInactive  */  
   CycleInactive:boolean,
      /**  RecurSource  */  
   RecurSource:boolean,
      /**  InstanceNum  */  
   InstanceNum:number,
      /**  RecurBalance  */  
   RecurBalance:number,
      /**  DocRecurBalance  */  
   DocRecurBalance:number,
      /**  Rpt1RecurBalance  */  
   Rpt1RecurBalance:number,
      /**  Rpt2RecurBalance  */  
   Rpt2RecurBalance:number,
      /**  Rpt3RecurBalance  */  
   Rpt3RecurBalance:number,
      /**  LastDate  */  
   LastDate:string,
      /**  RecurringState  */  
   RecurringState:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsAddedToGTI  */  
   IsAddedToGTI:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  CMReason  */  
   CMReason:string,
      /**  THIsImmatAdjustment  */  
   THIsImmatAdjustment:boolean,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  RevisionDate  */  
   RevisionDate:string,
      /**  RevisionNum  */  
   RevisionNum:number,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  TWGUIGroup  */  
   TWGUIGroup:string,
      /**  TWPeriodPrefix  */  
   TWPeriodPrefix:string,
      /**  Indicates if the Invoice is in Collections status  */  
   InvInCollections:boolean,
      /**   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  */  
   CollectionsCust:boolean,
      /**  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  */  
   CounterARForm:number,
      /**  flag indicates if Revenue of the invoice has been already posted  */  
   PostedRecog:boolean,
      /**  Confirmation Date  */  
   CNConfirmDate:string,
      /**  MXSATSeal  */  
   MXSATSeal:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXTaxRcptType  */  
   MXTaxRcptType:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXCertifiedTimestamp  */  
   MXCertifiedTimestamp:string,
      /**  MXSATCertificateSN  */  
   MXSATCertificateSN:string,
      /**  MXDigitalSeal  */  
   MXDigitalSeal:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXCertificate  */  
   MXCertificate:string,
      /**  MXApprovalYear  */  
   MXApprovalYear:number,
      /**  MXCBB  */  
   MXCBB:string,
      /**  MXApprovalNum  */  
   MXApprovalNum:number,
      /**  MXOriginalStringTFD  */  
   MXOriginalStringTFD:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXCertificateSN  */  
   MXCertificateSN:string,
      /**  MXOriginalAmount  */  
   MXOriginalAmount:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MXOriginalDate  */  
   MXOriginalDate:string,
      /**  MXOriginalSeries  */  
   MXOriginalSeries:string,
      /**  MXOriginalFolio  */  
   MXOriginalFolio:string,
      /**  MXTaxRegime  */  
   MXTaxRegime:string,
      /**  MXOriginalString  */  
   MXOriginalString:string,
      /**  MXPaymentName  */  
   MXPaymentName:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  EInvStatus  */  
   EInvStatus:number,
      /**  EInvTimestamp  */  
   EInvTimestamp:string,
      /**  EInvUpdatedBy  */  
   EInvUpdatedBy:string,
      /**  EInvException  */  
   EInvException:string,
      /**  Flagged that this invoice has taxes which were necessary or is necessary now.  */  
   WithTaxConfirm:boolean,
      /**  UseAltBillToID  */  
   UseAltBillToID:boolean,
      /**  MXCancelledDate  */  
   MXCancelledDate:string,
      /**  Overpaid  */  
   Overpaid:boolean,
      /**  OrdExchangeRate  */  
   OrdExchangeRate:number,
      /**  PEAPPayNum  */  
   PEAPPayNum:number,
      /**  PEBankNumber  */  
   PEBankNumber:string,
      /**  PECharges  */  
   PECharges:number,
      /**  PECommissions  */  
   PECommissions:number,
      /**  PEDetTaxAmt  */  
   PEDetTaxAmt:number,
      /**  PEDetTaxCurrencyCode  */  
   PEDetTaxCurrencyCode:string,
      /**  PEDischargeAmt  */  
   PEDischargeAmt:number,
      /**  PEDischargeDate  */  
   PEDischargeDate:string,
      /**  PEInterest  */  
   PEInterest:number,
      /**  PENoPayPenalty  */  
   PENoPayPenalty:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  PEBOEPosted  */  
   PEBOEPosted:boolean,
      /**  DocPEInterest  */  
   DocPEInterest:number,
      /**  DocPECommissions  */  
   DocPECommissions:number,
      /**  DocPECharges  */  
   DocPECharges:number,
      /**  DocPENoPayPenalty  */  
   DocPENoPayPenalty:number,
      /**  DocPEDischargeAmt  */  
   DocPEDischargeAmt:number,
      /**  DocPEDetTaxAmt  */  
   DocPEDetTaxAmt:number,
      /**  Rpt1PEInterest  */  
   Rpt1PEInterest:number,
      /**  Rpt1PECommissions  */  
   Rpt1PECommissions:number,
      /**  Rpt1PECharges  */  
   Rpt1PECharges:number,
      /**  Rpt1PENoPayPenalty  */  
   Rpt1PENoPayPenalty:number,
      /**  Rpt1PEDischargeAmt  */  
   Rpt1PEDischargeAmt:number,
      /**  Rpt2PEInterest  */  
   Rpt2PEInterest:number,
      /**  Rpt2PECommissions  */  
   Rpt2PECommissions:number,
      /**  Rpt2PECharges  */  
   Rpt2PECharges:number,
      /**  Rpt2PENoPayPenalty  */  
   Rpt2PENoPayPenalty:number,
      /**  Rpt2PEDischargeAmt  */  
   Rpt2PEDischargeAmt:number,
      /**  Rpt3PEInterest  */  
   Rpt3PEInterest:number,
      /**  Rpt3PECommissions  */  
   Rpt3PECommissions:number,
      /**  Rpt3PECharges  */  
   Rpt3PECharges:number,
      /**  Rpt3PENoPayPenalty  */  
   Rpt3PENoPayPenalty:number,
      /**  Rpt3PEDischargeAmt  */  
   Rpt3PEDischargeAmt:number,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
      /**  PEGuaranteeName  */  
   PEGuaranteeName:string,
      /**  PEGuaranteeAddress1  */  
   PEGuaranteeAddress1:string,
      /**  PEGuaranteeAddress2  */  
   PEGuaranteeAddress2:string,
      /**  PEGuaranteeAddress3  */  
   PEGuaranteeAddress3:string,
      /**  PEGuaranteeCity  */  
   PEGuaranteeCity:string,
      /**  PEGuaranteeState  */  
   PEGuaranteeState:string,
      /**  PEGuaranteeZip  */  
   PEGuaranteeZip:string,
      /**  PEGuaranteeCountry  */  
   PEGuaranteeCountry:string,
      /**  PEGuaranteeTaxID  */  
   PEGuaranteeTaxID:string,
      /**  PEGuaranteePhoneNum  */  
   PEGuaranteePhoneNum:string,
      /**  PEBOEStatus  */  
   PEBOEStatus:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  Document Name  */  
   TWGUIExportDocumentName:string,
      /**  Remarks  */  
   TWGUIExportRemarks:string,
      /**  Verification  */  
   TWGUIExportVerification:string,
      /**  PEDebitNoteReasonCode  */  
   PEDebitNoteReasonCode:string,
      /**  PEDebitNote  */  
   PEDebitNote:boolean,
      /**  MXPartPmt  */  
   MXPartPmt:boolean,
      /**  Tax Invoice Type  */  
   CNTaxInvoiceType:number,
      /**  MXExportOperationType  */  
   MXExportOperationType:string,
      /**  MXExportCustDocCode  */  
   MXExportCustDocCode:string,
      /**  MXExportCertOriginNum  */  
   MXExportCertOriginNum:string,
      /**  MXExportConfNum  */  
   MXExportConfNum:string,
      /**  MXExportCertOrigin  */  
   MXExportCertOrigin:boolean,
      /**  MXIncoterm  */  
   MXIncoterm:string,
      /**  AGDocConcept  */  
   AGDocConcept:number,
      /**  Electronic Invoice reference number  */  
   EInvRefNum:string,
      /**  Export document reference number  */  
   ExportDocRefNum:string,
      /**  Export document date  */  
   ExportDocDate:string,
      /**  Tax Transaction ID  */  
   INTaxTransactionID:string,
      /**  MXMovingReasonFlag  */  
   MXMovingReasonFlag:boolean,
      /**  MXMovingReason  */  
   MXMovingReason:string,
      /**  MXNumRegIdTrib  */  
   MXNumRegIdTrib:string,
      /**  MXResidenCountryNum  */  
   MXResidenCountryNum:number,
      /**  MXPurchaseType  */  
   MXPurchaseType:string,
      /**  MXConfirmationCode  */  
   MXConfirmationCode:string,
      /**  MXExternalCode  */  
   MXExternalCode:string,
      /**  This invoice was created via an integration with a third-party field service.  */  
   ServiceInvoice:boolean,
      /**  MXDomesticTransfer  */  
   MXDomesticTransfer:boolean,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  Shipping Port Code  */  
   INShippingPortCode:string,
      /**  Export Procedure  */  
   INExportProcedure:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
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
      /**  Quote number to which this invoice record is associated with.  */  
   QuoteNum:number,
      /**  The help desk case related to this invoice.  */  
   HDCaseNum:number,
      /**  Indicates that the credit hold was overridden for this invoice.  */  
   CreditOverride:boolean,
      /**  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  */  
   CreditOverrideDate:string,
      /**  The user id that override the invoice credit hold.  */  
   CreditOverrideUserID:string,
      /**  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  */  
   CreditHold:boolean,
      /**  Peru Electronic Invoice XML Type  */  
   PEXMLType:number,
      /**  COCreditMemoReasonCode  */  
   COCreditMemoReasonCode:string,
      /**  CODebitMemoReasonCode  */  
   CODebitMemoReasonCode:string,
      /**  COReasonDesc  */  
   COReasonDesc:string,
      /**  CODebitNote  */  
   CODebitNote:boolean,
      /**  PEDetractionTranNum  */  
   PEDetractionTranNum:number,
      /**  PEProductCode  */  
   PEProductCode:string,
      /**  PECollectionGroupID  */  
   PECollectionGroupID:string,
      /**  PE Caption Code  */  
   PECaptionCode:string,
      /**  PE Caption Code Description  */  
   PECaption:string,
      /**  PE Reference DocumentType 1  */  
   PERefDocumentType:string,
      /**  PE Reference Document Number 1  */  
   PERefDocumentNumber:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PE Reference DocumentType 2  */  
   PERefDocumentType2:string,
      /**  PE Reference DocumentType 3  */  
   PERefDocumentType3:string,
      /**  PE Reference DocumentType 4  */  
   PERefDocumentType4:string,
      /**  PE Reference DocumentType 5  */  
   PERefDocumentType5:string,
      /**  PE Reference Document Number 2  */  
   PERefDocumentNumber2:string,
      /**  PE Reference Document Number 3  */  
   PERefDocumentNumber3:string,
      /**  PE Reference Document Number 4  */  
   PERefDocumentNumber4:string,
      /**  PE Reference Document Number 5  */  
   PERefDocumentNumber5:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  Date and Time of E-invoice generation.  */  
   ELIEInvUpdatedOn:string,
      /**  COOperType  */  
   COOperType:string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   CentralCollection:boolean,
      /**  Company that created this invoice.  */  
   CColChildCompany:string,
      /**  Central Collection company.  */  
   CColParentCompany:string,
      /**  Order number on the invoicing company.  */  
   CColOrderNum:number,
      /**  Invoice number on the invoicing company.  */  
   CColChildInvoiceNum:number,
      /**  Invoice number on central collection company  */  
   CColInvoiceNum:number,
      /**  Legal number on the invoicing company invoice.  */  
   CColChildLegalNumber:string,
      /**  Legal number on central collection company.  */  
   CColLegalNumber:string,
      /**  Invoice reference on the Invoicing Company.  */  
   CColInvoiceRef:number,
      /**  Invoice Balance in the Central Collection company.  */  
   CColInvBal:number,
      /**  Central Collection Doc Invoice Balance.  */  
   DocCColInvBal:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   CColInvAmt:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   DocCColInvAmt:number,
      /**  Rpt 1 Parent Invoice Balance  */  
   Rpt1CColInvBal:number,
      /**  Rpt 2 Parent Invoice Balance  */  
   Rpt2CColInvBal:number,
      /**  Rpt 3 Parent Invoice Balance  */  
   Rpt3CColInvBal:number,
      /**  Rpt 1 Child Invoice Amount  */  
   Rpt1CColInvAmt:number,
      /**  Rpt 2 Child Invoice Amount  */  
   Rpt2CColInvAmt:number,
      /**  Rpt 3 Child Invoice Amount  */  
   Rpt3CColInvAmt:number,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  User terminal name  */  
   ELIEInvTerminalName:string,
      /**  User terminal IP  */  
   ELIEInvTerminalIP:string,
      /**  GL Description  */  
   Description:string,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  Indicates if the Central Collection parent invoice is open.  */  
   CColOpenInvoice:boolean,
      /**  AGQRCodeData  */  
   AGQRCodeData:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  */  
   CallLine:number,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstInvoiceNum  */  
   MXSubstInvoiceNum:number,
      /**  MXExportType  */  
   MXExportType:string,
      /**  MXGlobalInvoicePeriod  */  
   MXGlobalInvoicePeriod:string,
      /**  MXGlobalInvoiceMonth  */  
   MXGlobalInvoiceMonth:string,
      /**  ELIEInvServiceProviderStatus  */  
   ELIEInvServiceProviderStatus:number,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  */  
   AmountDue:number,
      /**  The amount of the payment to apply to the invoice  */  
   ApplyAmt:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
   BankNetPay:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  This external field captures the IMCashGrp.GroupID used in object BankFileImport.p  */  
   CashGroupID:string,
   DiscAmt:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  This new column should display payment discount amounts for invoices that are still within discount terms  */  
   Discount:number,
   DiscountAvailable:boolean,
      /**  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  */  
   DocAmountDue:number,
   DocDiscAmt:number,
   DocGrossPay:number,
   DocNetPay:number,
      /**  Due Date should be higthlighted if number of business days between selection date and invoice due date is less that 2 (for subsequent recurrent payment type) or 5 (for one-off or first recurrent payment types) days  */  
   DueDateHighLighted:boolean,
   GrossPay:number,
   IsCreditMemo:boolean,
      /**  DueDate from Select Invoices dialog.  */  
   PmtDueDate:string,
   Rpt1DiscAmt:number,
   Rpt1GrossPay:number,
   Rpt2DiscAmt:number,
   Rpt2GrossPay:number,
   Rpt3DiscAmt:number,
   Rpt3GrossPay:number,
   Selected:boolean,
      /**  Taxable Write Off  */  
   TaxableWriteOff:boolean,
      /**  Write Off  */  
   WriteOff:boolean,
      /**  Write Off Account  */  
   WriteOffAccount:string,
      /**  Write Off Account Description  */  
   WriteOffAccountDesc:string,
      /**  Write Off Amount  */  
   WriteOffAmount:number,
      /**  Allows uset to enter comment for Write Off.  */  
   WriteOffComment:string,
      /**  This new column should enable the user to enter a draft payment amount ? a part of the check amount that is to be allocated to the invoice  */  
   AllocAmount:number,
   BitFlag:number,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARInvSelTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  InvoiceNum of ARInvcSel  */  
   InvoiceNum:number,
   BitFlag:number,
   COADescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLShortAcct:string,
   GLAccountGLAcctDisp:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARInvSelTableset{
   ARInvSel:Erp_Tablesets_ARInvSelRow[],
   ARInvSelTGLC:Erp_Tablesets_ARInvSelTGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankFileImportParamRow{
   Company:string,
   GroupID:string,
   EFTHeadUID:number,
   EFTHeadName:string,
   ImportFile:string,
   ImportFormat:string,
   ClientImportFileName:string,
   ServerImportFileName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankFileImportParamTableset{
   BankFileImportParam:Erp_Tablesets_BankFileImportParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankFileImportTableset{
   CashGrpImport:Erp_Tablesets_CashGrpImportRow[],
   CashHeadImport:Erp_Tablesets_CashHeadImportRow[],
   CashDtlImport:Erp_Tablesets_CashDtlImportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashDtlImportRow{
      /**  Company  */  
   Company:string,
      /**  GroupID  */  
   GroupID:string,
      /**  HeadNum  */  
   HeadNum:number,
      /**  InvoiceNum  */  
   InvoiceNum:number,
      /**  InvoiceRef  */  
   InvoiceRef:number,
      /**  TranType  */  
   TranType:string,
      /**  Posted  */  
   Posted:boolean,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalPeriod  */  
   FiscalPeriod:number,
      /**  GLPosted  */  
   GLPosted:boolean,
      /**  TranDate  */  
   TranDate:string,
      /**  CheckRef  */  
   CheckRef:string,
      /**  TranAmt  */  
   TranAmt:number,
      /**  DocTranAmt  */  
   DocTranAmt:number,
      /**  CustNum  */  
   CustNum:number,
      /**  Discount  */  
   Discount:number,
      /**  DocDiscount  */  
   DocDiscount:number,
      /**  Comment  */  
   Comment:string,
      /**  Reference  */  
   Reference:string,
      /**  ExchangeRate  */  
   ExchangeRate:number,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  GLRefType  */  
   GLRefType:string,
      /**  GLRefCode  */  
   GLRefCode:string,
      /**  DebitNote  */  
   DebitNote:boolean,
      /**  DNComments  */  
   DNComments:string,
      /**  DNAmount  */  
   DNAmount:number,
      /**  DocDnAmount  */  
   DocDnAmount:number,
      /**  DNCustNbr  */  
   DNCustNbr:string,
      /**  RoundDiff  */  
   RoundDiff:number,
      /**  Rpt1Discount  */  
   Rpt1Discount:number,
      /**  Rpt2Discount  */  
   Rpt2Discount:number,
      /**  Rpt3Discount  */  
   Rpt3Discount:number,
      /**  Rpt1DnAmount  */  
   Rpt1DnAmount:number,
      /**  Rpt2DnAmount  */  
   Rpt2DnAmount:number,
      /**  Rpt3DnAmount  */  
   Rpt3DnAmount:number,
      /**  Rpt1TranAmt  */  
   Rpt1TranAmt:number,
      /**  Rpt2TranAmt  */  
   Rpt2TranAmt:number,
      /**  Rpt3TranAmt  */  
   Rpt3TranAmt:number,
      /**  RateGrpCode  */  
   RateGrpCode:string,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  TaxRegionCode  */  
   TaxRegionCode:string,
      /**  GetDfltTaxIds  */  
   GetDfltTaxIds:boolean,
      /**  WithholdAmt  */  
   WithholdAmt:number,
      /**  DocWithholdAmt  */  
   DocWithholdAmt:number,
      /**  Rpt1WithholdAmt  */  
   Rpt1WithholdAmt:number,
      /**  Rpt2WithholdAmt  */  
   Rpt2WithholdAmt:number,
      /**  Rpt3WithholdAmt  */  
   Rpt3WithholdAmt:number,
      /**  SelfAssessAmt  */  
   SelfAssessAmt:number,
      /**  DocSelfAssessAmt  */  
   DocSelfAssessAmt:number,
      /**  Rpt1SelfAssessAmt  */  
   Rpt1SelfAssessAmt:number,
      /**  Rpt2SelfAssessAmt  */  
   Rpt2SelfAssessAmt:number,
      /**  Rpt3SelfAssessAmt  */  
   Rpt3SelfAssessAmt:number,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  DocTaxAmt  */  
   DocTaxAmt:number,
      /**  Rpt1TaxAmt  */  
   Rpt1TaxAmt:number,
      /**  Rpt2TaxAmt  */  
   Rpt2TaxAmt:number,
      /**  Rpt3TaxAmt  */  
   Rpt3TaxAmt:number,
      /**  RedStorno  */  
   RedStorno:boolean,
      /**  TaxReceiptDate  */  
   TaxReceiptDate:string,
      /**  TaxReceiptNo  */  
   TaxReceiptNo:string,
      /**  WHTCertificateDate  */  
   WHTCertificateDate:string,
      /**  WHTCertificateNo  */  
   WHTCertificateNo:string,
      /**  PCashDeskID  */  
   PCashDeskID:string,
      /**  GainLossType  */  
   GainLossType:string,
      /**  PCashRefNum  */  
   PCashRefNum:number,
      /**  ReverseGL  */  
   ReverseGL:boolean,
      /**  RevalueDate  */  
   RevalueDate:string,
      /**  RevalueBal  */  
   RevalueBal:number,
      /**  DocRevalueBal  */  
   DocRevalueBal:number,
      /**  Rpt1RevalueBal  */  
   Rpt1RevalueBal:number,
      /**  Rpt2RevalueBal  */  
   Rpt2RevalueBal:number,
      /**  Rpt3RevalueBal  */  
   Rpt3RevalueBal:number,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  MainSite  */  
   MainSite:boolean,
      /**  SiteCode  */  
   SiteCode:string,
      /**  BranchID  */  
   BranchID:string,
      /**  InvoiceDate  */  
   InvoiceDate:string,
      /**  TaxRemarks  */  
   TaxRemarks:string,
      /**  NonDeductCode  */  
   NonDeductCode:string,
      /**  NonDeductAmt  */  
   NonDeductAmt:number,
      /**  NonDeductDocAmt  */  
   NonDeductDocAmt:number,
      /**  NonDeductRpt1Amt  */  
   NonDeductRpt1Amt:number,
      /**  NonDeductRpt2Amt  */  
   NonDeductRpt2Amt:number,
      /**  NonDeductRpt3Amt  */  
   NonDeductRpt3Amt:number,
      /**  AssetTypeCode  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  CreditCard  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  InvDueDate  */  
   InvDueDate:string,
      /**  ManualMatch  */  
   ManualMatch:boolean,
      /**  BillingNumber  */  
   BillingNumber:string,
      /**  SEPADDMsgID  */  
   SEPADDMsgID:string,
      /**  SEPADDPmtID  */  
   SEPADDPmtID:string,
      /**  PmtDueDate  */  
   PmtDueDate:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  WriteOffHeadNumRef  */  
   WriteOffHeadNumRef:number,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  TaxableAdjustment  */  
   TaxableAdjustment:boolean,
   BankNetPay:number,
   DispCurrencyCode:string,
   DocNetPay:number,
   InvPayStatus:string,
   DocRemainInvBal:number,
   InvOpenBalance:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashGrpImportListRow{
      /**  Company  */  
   Company:string,
      /**  GroupID  */  
   GroupID:string,
      /**  TranDate  */  
   TranDate:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalPeriod  */  
   FiscalPeriod:number,
      /**  ActiveUserID  */  
   ActiveUserID:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  Cashbook  */  
   Cashbook:boolean,
      /**  DebNoteOnly  */  
   DebNoteOnly:boolean,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  PromissoryNote  */  
   PromissoryNote:boolean,
      /**  PMUID  */  
   PMUID:number,
      /**  EIPaymSent  */  
   EIPaymSent:boolean,
      /**  PIStatus  */  
   PIStatus:string,
      /**  PIStatusGrp  */  
   PIStatusGrp:boolean,
      /**  PIType  */  
   PIType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Bank Branch Code  */  
   BankAcctBankBranchCode:string,
      /**  Swift Number or ABA Routing Number  */  
   BankAcctBankIdentifier:string,
      /**  The Bank's full name.  */  
   BankAcctBankName:string,
      /**  The account number for the bank account. Used for reference only.  */  
   BankAcctCheckingAccount:string,
      /**  Currency.CurrencyCode of the currency that the bank account is denominated in.  */  
   BankAcctCurrencyCode:string,
      /**  Full description of the bank account.  */  
   BankAcctDescription:string,
      /**  IBAN Code  */  
   BankAcctIBANCode:string,
   CurrencyCurrDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
      /**  Name of the payment method  */  
   PayMethodName:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PayMethodSummarizePerCustomer:boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PayMethodType:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashGrpImportListTableset{
   CashGrpImportList:Erp_Tablesets_CashGrpImportListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashGrpImportRow{
      /**  Company  */  
   Company:string,
      /**  GroupID  */  
   GroupID:string,
      /**  TranDate  */  
   TranDate:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalPeriod  */  
   FiscalPeriod:number,
      /**  ActiveUserID  */  
   ActiveUserID:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  Cashbook  */  
   Cashbook:boolean,
      /**  DebNoteOnly  */  
   DebNoteOnly:boolean,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  PromissoryNote  */  
   PromissoryNote:boolean,
      /**  PMUID  */  
   PMUID:number,
      /**  EIPaymSent  */  
   EIPaymSent:boolean,
      /**  PIStatus  */  
   PIStatus:string,
      /**  PIStatusGrp  */  
   PIStatusGrp:boolean,
      /**  PIType  */  
   PIType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  BankBatchID  */  
   BankBatchID:string,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  ProcessStatus  */  
   ProcessStatus:string,
      /**  ImportFileName  */  
   ImportFileName:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrDesc:string,
   LockForChanges:boolean,
   ProcessButtonEnabled:boolean,
   ProcessStatusDisplay:string,
      /**  Enable matching Credit Memo with Invoice  */  
   EnableMatchCMemoWithInv:boolean,
   BitFlag:number,
   BankAcctBankBranchCode:string,
   BankAcctCurrencyCode:string,
   BankAcctDescription:string,
   BankAcctBankName:string,
   BankAcctBankIdentifier:string,
   BankAcctIBANCode:string,
   BankAcctCheckingAccount:string,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   PayMethodType:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadImportRow{
      /**  Company  */  
   Company:string,
      /**  GroupID  */  
   GroupID:string,
      /**  HeadNum  */  
   HeadNum:number,
      /**  Posted  */  
   Posted:boolean,
      /**  TranType  */  
   TranType:string,
      /**  CheckRef  */  
   CheckRef:string,
      /**  OrderNum  */  
   OrderNum:number,
      /**  InvoiceNum  */  
   InvoiceNum:number,
      /**  TranAmt  */  
   TranAmt:number,
      /**  DocTranAmt  */  
   DocTranAmt:number,
      /**  CustID  */  
   CustID:string,
      /**  TranDate  */  
   TranDate:string,
      /**  CustNum  */  
   CustNum:number,
      /**  UnAppliedAmt  */  
   UnAppliedAmt:number,
      /**  DocUnAppliedAmt  */  
   DocUnAppliedAmt:number,
      /**  AppliedAmt  */  
   AppliedAmt:number,
      /**  DocAppliedAmt  */  
   DocAppliedAmt:number,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalPeriod  */  
   FiscalPeriod:number,
      /**  Reference  */  
   Reference:string,
      /**  GLPosted  */  
   GLPosted:boolean,
      /**  CreditMemoNum  */  
   CreditMemoNum:number,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  ExchangeRate  */  
   ExchangeRate:number,
      /**  TaxRegionCode  */  
   TaxRegionCode:string,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  DocTaxAmt  */  
   DocTaxAmt:number,
      /**  CashBookNum  */  
   CashBookNum:number,
      /**  CashbookLine  */  
   CashbookLine:number,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  ExternalID  */  
   ExternalID:string,
      /**  GLRefType  */  
   GLRefType:string,
      /**  GLRefCode  */  
   GLRefCode:string,
      /**  CardMemberName  */  
   CardMemberName:string,
      /**  CardNumber  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  ExpirationMonth  */  
   ExpirationMonth:number,
      /**  ExpirationYear  */  
   ExpirationYear:number,
      /**  CardID  */  
   CardID:string,
      /**  CardmemberReference  */  
   CardmemberReference:string,
      /**  ProcessCard  */  
   ProcessCard:string,
      /**  CCAmount  */  
   CCAmount:number,
      /**  CCFreight  */  
   CCFreight:number,
      /**  CCTax  */  
   CCTax:number,
      /**  CCTotal  */  
   CCTotal:number,
      /**  CCDocAmount  */  
   CCDocAmount:number,
      /**  CCDocFreight  */  
   CCDocFreight:number,
      /**  CCDocTax  */  
   CCDocTax:number,
      /**  CCDocTotal  */  
   CCDocTotal:number,
      /**  CCStreetAddr  */  
   CCStreetAddr:string,
      /**  CCZip  */  
   CCZip:string,
      /**  DebNoteOnly  */  
   DebNoteOnly:boolean,
      /**  Rpt1AppliedAmt  */  
   Rpt1AppliedAmt:number,
      /**  Rpt2AppliedAmt  */  
   Rpt2AppliedAmt:number,
      /**  Rpt3AppliedAmt  */  
   Rpt3AppliedAmt:number,
      /**  Rpt1TaxAmt  */  
   Rpt1TaxAmt:number,
      /**  Rpt2TaxAmt  */  
   Rpt2TaxAmt:number,
      /**  Rpt3TaxAmt  */  
   Rpt3TaxAmt:number,
      /**  Rpt1TranAmt  */  
   Rpt1TranAmt:number,
      /**  Rpt2TranAmt  */  
   Rpt2TranAmt:number,
      /**  Rpt3TranAmt  */  
   Rpt3TranAmt:number,
      /**  Rpt1UnAppliedAmt  */  
   Rpt1UnAppliedAmt:number,
      /**  Rpt2UnAppliedAmt  */  
   Rpt2UnAppliedAmt:number,
      /**  Rpt3UnAppliedAmt  */  
   Rpt3UnAppliedAmt:number,
      /**  RateGrpCode  */  
   RateGrpCode:string,
      /**  DocDepApplied  */  
   DocDepApplied:number,
      /**  Rpt1CCAmount  */  
   Rpt1CCAmount:number,
      /**  Rpt2CCAmount  */  
   Rpt2CCAmount:number,
      /**  Rpt3CCAmount  */  
   Rpt3CCAmount:number,
      /**  Rpt1CCFreight  */  
   Rpt1CCFreight:number,
      /**  Rpt2CCFreight  */  
   Rpt2CCFreight:number,
      /**  Rpt3CCFreight  */  
   Rpt3CCFreight:number,
      /**  Rpt1CCTax  */  
   Rpt1CCTax:number,
      /**  Rpt2CCTax  */  
   Rpt2CCTax:number,
      /**  Rpt3CCTax  */  
   Rpt3CCTax:number,
      /**  Rpt1CCTotal  */  
   Rpt1CCTotal:number,
      /**  Rpt2CCTotal  */  
   Rpt2CCTotal:number,
      /**  Rpt3CCTotal  */  
   Rpt3CCTotal:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  ReadyToCalc  */  
   ReadyToCalc:boolean,
      /**  RecalcBeforePost  */  
   RecalcBeforePost:boolean,
      /**  GetDfltTaxIds  */  
   GetDfltTaxIds:boolean,
      /**  WithholdAmt  */  
   WithholdAmt:number,
      /**  DocWithholdAmt  */  
   DocWithholdAmt:number,
      /**  Rpt1WithholdAmt  */  
   Rpt1WithholdAmt:number,
      /**  Rpt2WithholdAmt  */  
   Rpt2WithholdAmt:number,
      /**  Rpt3WithholdAmt  */  
   Rpt3WithholdAmt:number,
      /**  SelfAssessAmt  */  
   SelfAssessAmt:number,
      /**  DocSelfAssessAmt  */  
   DocSelfAssessAmt:number,
      /**  Rpt1SelfAssessAmt  */  
   Rpt1SelfAssessAmt:number,
      /**  Rpt2SelfAssessAmt  */  
   Rpt2SelfAssessAmt:number,
      /**  Rpt3SelfAssessAmt  */  
   Rpt3SelfAssessAmt:number,
      /**  ReceiptCurrencyCode  */  
   ReceiptCurrencyCode:string,
      /**  ReceiptAmt  */  
   ReceiptAmt:number,
      /**  BankRcptExchangeRate  */  
   BankRcptExchangeRate:number,
      /**  SettlementExchangeRate  */  
   SettlementExchangeRate:number,
      /**  CMCurrencyCode  */  
   CMCurrencyCode:string,
      /**  CMAmount  */  
   CMAmount:number,
      /**  ReverseRef  */  
   ReverseRef:number,
      /**  ReverseDate  */  
   ReverseDate:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  TaxWhld  */  
   TaxWhld:number,
      /**  DiscountDate  */  
   DiscountDate:string,
      /**  TaxWhldCalc  */  
   TaxWhldCalc:number,
      /**  ContractDate  */  
   ContractDate:string,
      /**  Plant  */  
   Plant:string,
      /**  UnallocatedAmt  */  
   UnallocatedAmt:number,
      /**  DocUnallocatedAmt  */  
   DocUnallocatedAmt:number,
      /**  Rpt1UnallocatedAmt  */  
   Rpt1UnallocatedAmt:number,
      /**  Rpt2UnallocatedAmt  */  
   Rpt2UnallocatedAmt:number,
      /**  Rpt3UnallocatedAmt  */  
   Rpt3UnallocatedAmt:number,
      /**  ApplyHeadNum  */  
   ApplyHeadNum:number,
      /**  AllocatedAmt  */  
   AllocatedAmt:number,
      /**  DocAllocatedAmt  */  
   DocAllocatedAmt:number,
      /**  Rpt1AllocatedAmt  */  
   Rpt1AllocatedAmt:number,
      /**  Rpt2AllocatedAmt  */  
   Rpt2AllocatedAmt:number,
      /**  Rpt3AllocatedAmt  */  
   Rpt3AllocatedAmt:number,
      /**  Comment  */  
   Comment:string,
      /**  PMUID  */  
   PMUID:number,
      /**  PCashDeskID  */  
   PCashDeskID:string,
      /**  BankTranID  */  
   BankTranID:string,
      /**  PCashRefNum  */  
   PCashRefNum:number,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  MainSite  */  
   MainSite:boolean,
      /**  SiteCode  */  
   SiteCode:string,
      /**  BranchID  */  
   BranchID:string,
      /**  InvoiceDate  */  
   InvoiceDate:string,
      /**  TaxRemarks  */  
   TaxRemarks:string,
      /**  NonDeductCode  */  
   NonDeductCode:string,
      /**  NonDeductAmt  */  
   NonDeductAmt:number,
      /**  NonDeductDocAmt  */  
   NonDeductDocAmt:number,
      /**  NonDeductRpt1Amt  */  
   NonDeductRpt1Amt:number,
      /**  NonDeductRpt2Amt  */  
   NonDeductRpt2Amt:number,
      /**  NonDeductRpt3Amt  */  
   NonDeductRpt3Amt:number,
      /**  AssetTypeCode  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  CreditCard  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  BankTransDate  */  
   BankTransDate:string,
      /**  CustNameFromFile  */  
   CustNameFromFile:string,
      /**  OCRNumber  */  
   OCRNumber:string,
      /**  ImportLineStatus  */  
   ImportLineStatus:string,
      /**  ImportLineError  */  
   ImportLineError:string,
      /**  DescFromImport  */  
   DescFromImport:string,
      /**  InvNumList  */  
   InvNumList:string,
      /**  InvAmtList  */  
   InvAmtList:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  ManualMatch  */  
   ManualMatch:boolean,
      /**  CreditMemo  */  
   CreditMemo:boolean,
      /**  CMNum  */  
   CMNum:number,
      /**  CMDocAmount  */  
   CMDocAmount:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  CHISRPartyID  */  
   CHISRPartyID:string,
      /**  CHISRRefNumAvailableToChange  */  
   CHISRRefNumAvailableToChange:boolean,
      /**  BankBatchID  */  
   BankBatchID:string,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  RcptCurAppliedAmt  */  
   RcptCurAppliedAmt:number,
      /**  RcptCurUnAppliedAmt  */  
   RcptCurUnAppliedAmt:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXPaySupplementFlag  */  
   MXPaySupplementFlag:boolean,
      /**  LockboxID  */  
   LockboxID:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXOriginalCheckRef  */  
   MXOriginalCheckRef:string,
      /**  MXConfirmationCode  */  
   MXConfirmationCode:string,
      /**  MXBankID  */  
   MXBankID:string,
      /**  ReversedReason  */  
   ReversedReason:string,
      /**  CCCity  */  
   CCCity:string,
      /**  CCState  */  
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
      /**  Adjustment  */  
   Adjustment:boolean,
      /**  AdjustmentRef  */  
   AdjustmentRef:number,
      /**  AdjustmentReason  */  
   AdjustmentReason:string,
      /**  WriteOffAmount  */  
   WriteOffAmount:number,
      /**  DocWriteOffAmount  */  
   DocWriteOffAmount:number,
      /**  Rpt1WriteOffAmount  */  
   Rpt1WriteOffAmount:number,
      /**  Rpt2WriteOffAmount  */  
   Rpt2WriteOffAmount:number,
      /**  Rpt3WriteOffAmount  */  
   Rpt3WriteOffAmount:number,
      /**  MXCertifiedTimestamp  */  
   MXCertifiedTimestamp:string,
      /**  MXSATSeal  */  
   MXSATSeal:string,
      /**  MXDigitalSeal  */  
   MXDigitalSeal:string,
      /**  MXSATCertificateSN  */  
   MXSATCertificateSN:string,
      /**  MXOriginalStringTFD  */  
   MXOriginalStringTFD:string,
      /**  MXCertificate  */  
   MXCertificate:string,
      /**  MXCertificateSN  */  
   MXCertificateSN:string,
      /**  SourceGroupID  */  
   SourceGroupID:string,
      /**  SourceHeadNum  */  
   SourceHeadNum:number,
      /**  SEC  */  
   SEC:string,
      /**  ACHTranCode  */  
   ACHTranCode:number,
      /**  CustomerBankID  */  
   CustomerBankID:string,
      /**  CustomerBankAcctNumber  */  
   CustomerBankAcctNumber:string,
      /**  CustomerBankSwiftNum  */  
   CustomerBankSwiftNum:string,
      /**  CustomerBankIBANCode  */  
   CustomerBankIBANCode:string,
      /**  CustomerBankNameOnAccount  */  
   CustomerBankNameOnAccount:string,
      /**  CustomerBankAddress1  */  
   CustomerBankAddress1:string,
      /**  CustomerBankAddress2  */  
   CustomerBankAddress2:string,
      /**  CustomerBankAddress3  */  
   CustomerBankAddress3:string,
      /**  CustomerBankCity  */  
   CustomerBankCity:string,
      /**  CustomerBankState  */  
   CustomerBankState:string,
      /**  CustomerBankPostalCode  */  
   CustomerBankPostalCode:string,
      /**  CustomerBankCountryNum  */  
   CustomerBankCountryNum:number,
      /**  ARRemittanceSlipPrinted  */  
   ARRemittanceSlipPrinted:boolean,
      /**  CustomerBankName  */  
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
      /**  Cash Rec Group ID  */  
   CashRecGroupID:string,
      /**  Cash Rec Head Num  */  
   CashRecHeadNum:number,
      /**  RvJrnUID  */  
   RvJrnUID:number,
      /**  ProcessStatus  */  
   ProcessStatus:string,
      /**  NettingID  */  
   NettingID:number,
      /**  GL Description for the Reverse process  */  
   RevDescription:string,
      /**  GL Description for AR - Apply Credit Memo  */  
   CMDescription:string,
      /**  BankReceiptAmt  */  
   BankReceiptAmt:number,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstHeadNum  */  
   MXSubstHeadNum:number,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
   BankRcptXRateLabel:string,
      /**  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  */  
   CHImportStatus:boolean,
      /**  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  */  
   EnableCust:boolean,
   SettlementXRateLabel:string,
   LockForChanges:boolean,
   ProcessStatusDisplay:string,
   BitFlag:number,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   RcptCurrencyCurrSymbol:string,
   SettlementCurrencyCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtBankFileImportTableset{
   CashGrpImport:Erp_Tablesets_CashGrpImportRow[],
   CashHeadImport:Erp_Tablesets_CashHeadImportRow[],
   CashDtlImport:Erp_Tablesets_CashDtlImportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param cGroupID
   */  
export interface GetBankFileImportParam_input{
      /**  The Cash Group ID  */  
   cGroupID:string,
}

export interface GetBankFileImportParam_output{
   returnObj:Erp_Tablesets_BankFileImportParamTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_BankFileImportTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_BankFileImportTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_BankFileImportTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface GetGroupInfo_input{
      /**  Group ID  */  
   groupID:string,
}

export interface GetGroupInfo_output{
parameters : {
      /**  output parameters  */  
   processStatus:string,
   processStatusDisplay:string,
   processButtonEnabled:boolean,
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
   returnObj:Erp_Tablesets_CashGrpImportListTableset[],
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
export interface GetNewCashDtlImport_input{
   ds:Erp_Tablesets_BankFileImportTableset[],
   groupID:string,
   headNum:number,
   invoiceNum:number,
}

export interface GetNewCashDtlImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashGrpImportNoLock_input{
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface GetNewCashGrpImportNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashGrpImport_input{
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface GetNewCashGrpImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewCashHeadImport_input{
   ds:Erp_Tablesets_BankFileImportTableset[],
   groupID:string,
}

export interface GetNewCashHeadImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

   /** Required : 
      @param whereClauseCashGrpImport
      @param whereClauseCashHeadImport
      @param whereClauseCashDtlImport
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCashGrpImport:string,
   whereClauseCashHeadImport:string,
   whereClauseCashDtlImport:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_BankFileImportTableset[],
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
export interface ImportBankFileExpress_input{
   ds:Erp_Tablesets_BankFileImportParamTableset[],
}

export interface ImportBankFileExpress_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportParamTableset[],
   opPaymentsFoundWithErrorsMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ImportBankFile_input{
   ds:Erp_Tablesets_BankFileImportParamTableset[],
}

export interface ImportBankFile_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportParamTableset[],
   opCMemoPaymentsNotFoundMessage:string,
   opPaymentsFoundWithErrorsMessage:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface LockGroup_input{
      /**  Selected Group ID  */  
   groupID:string,
}

export interface LockGroup_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipGroupID
      @param ipHeadNum
      @param ipISRRefNum
   */  
export interface MatchCHCashHeadImport_input{
      /**  GroupID  */  
   ipGroupID:string,
      /**  Head Number  */  
   ipHeadNum:number,
      /**  New ISR Reference number  */  
   ipISRRefNum:string,
}

export interface MatchCHCashHeadImport_output{
      /**  Result of matching  */  
   returnObj:boolean,
}

   /** Required : 
      @param matchGroupID
   */  
export interface MatchPayments_input{
      /**  The Group to match  */  
   matchGroupID:string,
}

export interface MatchPayments_output{
}

   /** Required : 
      @param cGroupID
   */  
export interface ProcessReceipts_input{
      /**  The Group to match  */  
   cGroupID:string,
}

export interface ProcessReceipts_output{
parameters : {
      /**  output parameters  */  
   cReturnMsg:string,
   lClearRcds:boolean,
}
}

   /** Required : 
      @param groupID
   */  
export interface ResetBankFileImportExpressGroup_input{
      /**  GroupID  */  
   groupID:string,
}

export interface ResetBankFileImportExpressGroup_output{
}

   /** Required : 
      @param pcGroupID
      @param piHeadNum
   */  
export interface SelectInvoices_input{
      /**  AR Check Group ID  */  
   pcGroupID:string,
      /**  IMCashRec header number  */  
   piHeadNum:number,
}

export interface SelectInvoices_output{
   returnObj:Erp_Tablesets_ARInvSelTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface UnlockGroup_input{
      /**  The Group ID selected by the user.  */  
   groupID:string,
}

export interface UnlockGroup_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtBankFileImportTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtBankFileImportTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_BankFileImportTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFileImportTableset[],
}
}

