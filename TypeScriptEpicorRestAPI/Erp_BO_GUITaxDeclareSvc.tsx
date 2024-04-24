import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GUITaxDeclareSvc
// Description: Tax Declaration Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/$metadata", {
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
   Description: Get GUITaxDeclares items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GUITaxDeclares
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUITaxDeclareRow
   */  
export function get_GUITaxDeclares(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GUITaxDeclares
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GUITaxDeclares(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GUITaxDeclare item
   Description: Calls GetByID to retrieve the GUITaxDeclare item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GUITaxDeclare
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclareYear Desc: DeclareYear   Required: True
      @param DeclarePeriod Desc: DeclarePeriod   Required: True
      @param GUISource Desc: GUISource   Required: True   Allow empty value : True
      @param GUIFormatCode Desc: GUIFormatCode   Required: True   Allow empty value : True
      @param TranDocType Desc: TranDocType   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param LegalNumber Desc: LegalNumber   Required: True   Allow empty value : True
      @param GUITaxTypeCode Desc: GUITaxTypeCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
   */  
export function get_GUITaxDeclares_Company_DeclareYear_DeclarePeriod_GUISource_GUIFormatCode_TranDocType_InvoiceNum_LegalNumber_GUITaxTypeCode(Company:string, DeclareYear:string, DeclarePeriod:string, GUISource:string, GUIFormatCode:string, TranDocType:string, InvoiceNum:string, LegalNumber:string, GUITaxTypeCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GUITaxDeclareRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares(" + Company + "," + DeclareYear + "," + DeclarePeriod + "," + GUISource + "," + GUIFormatCode + "," + TranDocType + "," + InvoiceNum + "," + LegalNumber + "," + GUITaxTypeCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GUITaxDeclareRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GUITaxDeclare for the service
   Description: Calls UpdateExt to update GUITaxDeclare. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GUITaxDeclare
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclareYear Desc: DeclareYear   Required: True
      @param DeclarePeriod Desc: DeclarePeriod   Required: True
      @param GUISource Desc: GUISource   Required: True   Allow empty value : True
      @param GUIFormatCode Desc: GUIFormatCode   Required: True   Allow empty value : True
      @param TranDocType Desc: TranDocType   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param LegalNumber Desc: LegalNumber   Required: True   Allow empty value : True
      @param GUITaxTypeCode Desc: GUITaxTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GUITaxDeclareRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GUITaxDeclares_Company_DeclareYear_DeclarePeriod_GUISource_GUIFormatCode_TranDocType_InvoiceNum_LegalNumber_GUITaxTypeCode(Company:string, DeclareYear:string, DeclarePeriod:string, GUISource:string, GUIFormatCode:string, TranDocType:string, InvoiceNum:string, LegalNumber:string, GUITaxTypeCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares(" + Company + "," + DeclareYear + "," + DeclarePeriod + "," + GUISource + "," + GUIFormatCode + "," + TranDocType + "," + InvoiceNum + "," + LegalNumber + "," + GUITaxTypeCode + ")", {
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
   Summary: Call UpdateExt to delete GUITaxDeclare item
   Description: Call UpdateExt to delete GUITaxDeclare item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GUITaxDeclare
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeclareYear Desc: DeclareYear   Required: True
      @param DeclarePeriod Desc: DeclarePeriod   Required: True
      @param GUISource Desc: GUISource   Required: True   Allow empty value : True
      @param GUIFormatCode Desc: GUIFormatCode   Required: True   Allow empty value : True
      @param TranDocType Desc: TranDocType   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param LegalNumber Desc: LegalNumber   Required: True   Allow empty value : True
      @param GUITaxTypeCode Desc: GUITaxTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GUITaxDeclares_Company_DeclareYear_DeclarePeriod_GUISource_GUIFormatCode_TranDocType_InvoiceNum_LegalNumber_GUITaxTypeCode(Company:string, DeclareYear:string, DeclarePeriod:string, GUISource:string, GUIFormatCode:string, TranDocType:string, InvoiceNum:string, LegalNumber:string, GUITaxTypeCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GUITaxDeclares(" + Company + "," + DeclareYear + "," + DeclarePeriod + "," + GUISource + "," + GUIFormatCode + "," + TranDocType + "," + InvoiceNum + "," + LegalNumber + "," + GUITaxTypeCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUITaxDeclareListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseGUITaxDeclare:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGUITaxDeclare!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGUITaxDeclare=" + whereClauseGUITaxDeclare
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(declareYear:string, declarePeriod:string, guISource:string, guIFormatCode:string, tranDocType:string, invoiceNum:string, legalNumber:string, guITaxTypeCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof declareYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "declareYear=" + declareYear
   }
   if(typeof declarePeriod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "declarePeriod=" + declarePeriod
   }
   if(typeof guISource!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "guISource=" + guISource
   }
   if(typeof guIFormatCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "guIFormatCode=" + guIFormatCode
   }
   if(typeof tranDocType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranDocType=" + tranDocType
   }
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }
   if(typeof legalNumber!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "legalNumber=" + legalNumber
   }
   if(typeof guITaxTypeCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "guITaxTypeCode=" + guITaxTypeCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetList" + params, {
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
   Summary: Invoke method ChangeTranDocTypeID
   Description: Method to call when changing the Transaction Document Type.
   OperationID: ChangeTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranDocTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/ChangeTranDocTypeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UserIsTaxDeclarationAdmin
   Description: Check if Current User is in Tax Declaration Admin Security Group
   OperationID: UserIsTaxDeclarationAdmin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UserIsTaxDeclarationAdmin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserIsTaxDeclarationAdmin(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/UserIsTaxDeclarationAdmin", {
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
   Summary: Invoke method CalcAmountIncludeTax
   Description: This method should be called to calculate include amount tax.
   OperationID: CalcAmountIncludeTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcAmountIncludeTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAmountIncludeTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcAmountIncludeTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/CalcAmountIncludeTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGUITaxDeclareFromExisting
   Description: Create new row using existing one as source (after adjusting the source row key field values
   OperationID: GetNewGUITaxDeclareFromExisting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGUITaxDeclareFromExisting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGUITaxDeclareFromExisting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGUITaxDeclareFromExisting(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetNewGUITaxDeclareFromExisting", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSourceRecordsChain
   Description: Retrieve the chain of source records
   OperationID: GetSourceRecordsChain
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSourceRecordsChain_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceRecordsChain_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSourceRecordsChain(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetSourceRecordsChain", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGUITaxDeclare
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGUITaxDeclare
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGUITaxDeclare_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGUITaxDeclare_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGUITaxDeclare(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetNewGUITaxDeclare", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GUITaxDeclareSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GUITaxDeclareListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUITaxDeclareRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GUITaxDeclareRow[],
}

export interface Erp_Tablesets_GUITaxDeclareListRow{
      /**  Company  */  
   "Company":string,
      /**  DeclareYear  */  
   "DeclareYear":number,
      /**  DeclarePeriod  */  
   "DeclarePeriod":number,
      /**  GUISource  */  
   "GUISource":string,
      /**  GUIFormatCode  */  
   "GUIFormatCode":string,
      /**  TranDocType  */  
   "TranDocType":string,
      /**  InvoiceNum  */  
   "InvoiceNum":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  GUITaxTypeCode  */  
   "GUITaxTypeCode":string,
      /**  InvoiceDate  */  
   "InvoiceDate":string,
      /**  TaxInPrice  */  
   "TaxInPrice":boolean,
      /**  ExportDate  */  
   "ExportDate":string,
      /**  ExportBillNum  */  
   "ExportBillNum":string,
      /**  ExportBillType  */  
   "ExportBillType":string,
      /**  ExportMark  */  
   "ExportMark":string,
      /**  ExportType  */  
   "ExportType":string,
      /**  ImportTaxBasis  */  
   "ImportTaxBasis":number,
      /**  ImportTaxAmt  */  
   "ImportTaxAmt":number,
      /**  GUIDeductCode  */  
   "GUIDeductCode":string,
      /**  SellerGUICode  */  
   "SellerGUICode":string,
      /**  BuyerGUICode  */  
   "BuyerGUICode":string,
      /**  AmtExclTax  */  
   "AmtExclTax":number,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  ManualInsert  */  
   "ManualInsert":boolean,
      /**  PartnerNum  */  
   "PartnerNum":number,
      /**  GUIGroup  */  
   "GUIGroup":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GUITaxDeclareRow{
      /**  Company  */  
   "Company":string,
      /**  DeclareYear  */  
   "DeclareYear":number,
      /**  DeclarePeriod  */  
   "DeclarePeriod":number,
      /**  GUISource  */  
   "GUISource":string,
      /**  GUIFormatCode  */  
   "GUIFormatCode":string,
      /**  TranDocType  */  
   "TranDocType":string,
      /**  InvoiceNum  */  
   "InvoiceNum":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  GUITaxTypeCode  */  
   "GUITaxTypeCode":string,
      /**  InvoiceDate  */  
   "InvoiceDate":string,
      /**  TaxInPrice  */  
   "TaxInPrice":boolean,
      /**  ExportDate  */  
   "ExportDate":string,
      /**  ExportBillNum  */  
   "ExportBillNum":string,
      /**  ExportBillType  */  
   "ExportBillType":string,
      /**  ExportMark  */  
   "ExportMark":string,
      /**  ExportType  */  
   "ExportType":string,
      /**  ImportTaxBasis  */  
   "ImportTaxBasis":number,
      /**  ImportTaxAmt  */  
   "ImportTaxAmt":number,
      /**  GUIDeductCode  */  
   "GUIDeductCode":string,
      /**  SellerGUICode  */  
   "SellerGUICode":string,
      /**  BuyerGUICode  */  
   "BuyerGUICode":string,
      /**  AmtExclTax  */  
   "AmtExclTax":number,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  ManualInsert  */  
   "ManualInsert":boolean,
      /**  PartnerNum  */  
   "PartnerNum":number,
      /**  GUIGroup  */  
   "GUIGroup":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SourceSysRowID  */  
   "SourceSysRowID":string,
      /**  Total Amount  */  
   "TotalAmt":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface CalcAmountIncludeTax_input{
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}

export interface CalcAmountIncludeTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}
}

   /** Required : 
      @param TranDocTypeID
      @param ds
   */  
export interface ChangeTranDocTypeID_input{
      /**  Transaction Document Type.  */  
   TranDocTypeID:string,
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}

export interface ChangeTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}
}

   /** Required : 
      @param declareYear
      @param declarePeriod
      @param guISource
      @param guIFormatCode
      @param tranDocType
      @param invoiceNum
      @param legalNumber
      @param guITaxTypeCode
   */  
export interface DeleteByID_input{
   declareYear:number,
   declarePeriod:number,
   guISource:string,
   guIFormatCode:string,
   tranDocType:string,
   invoiceNum:string,
   legalNumber:string,
   guITaxTypeCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GUITaxDeclareListRow{
      /**  Company  */  
   Company:string,
      /**  DeclareYear  */  
   DeclareYear:number,
      /**  DeclarePeriod  */  
   DeclarePeriod:number,
      /**  GUISource  */  
   GUISource:string,
      /**  GUIFormatCode  */  
   GUIFormatCode:string,
      /**  TranDocType  */  
   TranDocType:string,
      /**  InvoiceNum  */  
   InvoiceNum:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  GUITaxTypeCode  */  
   GUITaxTypeCode:string,
      /**  InvoiceDate  */  
   InvoiceDate:string,
      /**  TaxInPrice  */  
   TaxInPrice:boolean,
      /**  ExportDate  */  
   ExportDate:string,
      /**  ExportBillNum  */  
   ExportBillNum:string,
      /**  ExportBillType  */  
   ExportBillType:string,
      /**  ExportMark  */  
   ExportMark:string,
      /**  ExportType  */  
   ExportType:string,
      /**  ImportTaxBasis  */  
   ImportTaxBasis:number,
      /**  ImportTaxAmt  */  
   ImportTaxAmt:number,
      /**  GUIDeductCode  */  
   GUIDeductCode:string,
      /**  SellerGUICode  */  
   SellerGUICode:string,
      /**  BuyerGUICode  */  
   BuyerGUICode:string,
      /**  AmtExclTax  */  
   AmtExclTax:number,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  ManualInsert  */  
   ManualInsert:boolean,
      /**  PartnerNum  */  
   PartnerNum:number,
      /**  GUIGroup  */  
   GUIGroup:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GUITaxDeclareListTableset{
   GUITaxDeclareList:Erp_Tablesets_GUITaxDeclareListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GUITaxDeclareRow{
      /**  Company  */  
   Company:string,
      /**  DeclareYear  */  
   DeclareYear:number,
      /**  DeclarePeriod  */  
   DeclarePeriod:number,
      /**  GUISource  */  
   GUISource:string,
      /**  GUIFormatCode  */  
   GUIFormatCode:string,
      /**  TranDocType  */  
   TranDocType:string,
      /**  InvoiceNum  */  
   InvoiceNum:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  GUITaxTypeCode  */  
   GUITaxTypeCode:string,
      /**  InvoiceDate  */  
   InvoiceDate:string,
      /**  TaxInPrice  */  
   TaxInPrice:boolean,
      /**  ExportDate  */  
   ExportDate:string,
      /**  ExportBillNum  */  
   ExportBillNum:string,
      /**  ExportBillType  */  
   ExportBillType:string,
      /**  ExportMark  */  
   ExportMark:string,
      /**  ExportType  */  
   ExportType:string,
      /**  ImportTaxBasis  */  
   ImportTaxBasis:number,
      /**  ImportTaxAmt  */  
   ImportTaxAmt:number,
      /**  GUIDeductCode  */  
   GUIDeductCode:string,
      /**  SellerGUICode  */  
   SellerGUICode:string,
      /**  BuyerGUICode  */  
   BuyerGUICode:string,
      /**  AmtExclTax  */  
   AmtExclTax:number,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  ManualInsert  */  
   ManualInsert:boolean,
      /**  PartnerNum  */  
   PartnerNum:number,
      /**  GUIGroup  */  
   GUIGroup:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SourceSysRowID  */  
   SourceSysRowID:string,
      /**  Total Amount  */  
   TotalAmt:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GUITaxDeclareSourceTableset{
   GUITaxDeclare:Erp_Tablesets_GUITaxDeclareRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GUITaxDeclareTableset{
   GUITaxDeclare:Erp_Tablesets_GUITaxDeclareRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGUITaxDeclareTableset{
   GUITaxDeclare:Erp_Tablesets_GUITaxDeclareRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param declareYear
      @param declarePeriod
      @param guISource
      @param guIFormatCode
      @param tranDocType
      @param invoiceNum
      @param legalNumber
      @param guITaxTypeCode
   */  
export interface GetByID_input{
   declareYear:number,
   declarePeriod:number,
   guISource:string,
   guIFormatCode:string,
   tranDocType:string,
   invoiceNum:string,
   legalNumber:string,
   guITaxTypeCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GUITaxDeclareTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GUITaxDeclareTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GUITaxDeclareTableset[],
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
   returnObj:Erp_Tablesets_GUITaxDeclareListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param sourceRecordSysRowID
      @param ds
   */  
export interface GetNewGUITaxDeclareFromExisting_input{
      /**  SysRowID of source record  */  
   sourceRecordSysRowID:string,
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}

export interface GetNewGUITaxDeclareFromExisting_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}
}

   /** Required : 
      @param ds
      @param declareYear
      @param declarePeriod
      @param guISource
      @param guIFormatCode
      @param tranDocType
      @param invoiceNum
      @param legalNumber
   */  
export interface GetNewGUITaxDeclare_input{
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
   declareYear:number,
   declarePeriod:number,
   guISource:string,
   guIFormatCode:string,
   tranDocType:string,
   invoiceNum:string,
   legalNumber:string,
}

export interface GetNewGUITaxDeclare_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}
}

   /** Required : 
      @param whereClauseGUITaxDeclare
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGUITaxDeclare:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GUITaxDeclareTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param sourceRecordSysRowID
   */  
export interface GetSourceRecordsChain_input{
      /**  Source Record ID for Current Record  */  
   sourceRecordSysRowID:string,
}

export interface GetSourceRecordsChain_output{
   returnObj:Erp_Tablesets_GUITaxDeclareSourceTableset[],
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
   ds:Erp_Tablesets_UpdExtGUITaxDeclareTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGUITaxDeclareTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GUITaxDeclareTableset[],
}
}

export interface UserIsTaxDeclarationAdmin_output{
      /**  User is in Tax Declaration Admin Security Group  */  
   returnObj:boolean,
}

