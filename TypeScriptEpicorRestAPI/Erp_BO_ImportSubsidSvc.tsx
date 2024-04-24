import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ImportSubsidSvc
// Description: Import Consolidation from Subsidiary object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/$metadata", {
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
   Description: Get ImportSubsids items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportSubsids
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsImportRow
   */  
export function get_ImportSubsids(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportSubsids
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportSubsids(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ImportSubsid item
   Description: Calls GetByID to retrieve the ImportSubsid item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportSubsid
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsImportRow
   */  
export function get_ImportSubsids_Company_GenID(Company:string, GenID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids(" + Company + "," + GenID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportSubsid for the service
   Description: Calls UpdateExt to update ImportSubsid. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportSubsid
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportSubsids_Company_GenID(Company:string, GenID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids(" + Company + "," + GenID + ")", {
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
   Summary: Call UpdateExt to delete ImportSubsid item
   Description: Call UpdateExt to delete ImportSubsid item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportSubsid
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportSubsids_Company_GenID(Company:string, GenID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids(" + Company + "," + GenID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsImportListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportListRow)
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
export function get_GetRows(whereClauseConsImport:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseConsImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsImport=" + whereClauseConsImport
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GetRows" + params, {
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
export function get_GetByID(genID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof genID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "genID=" + genID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GetList" + params, {
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
   Summary: Invoke method GroupChangeWarning
   Description: Purpose:
Parameters:
<param name="ipBook">book id</param><param name="ds">ImportSubsid dataset row</param><param name="warnMsg">A warning message is returned if the book changes and the gljrngrp exists.</param>
Notes:
   OperationID: GroupChangeWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupChangeWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupChangeWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GroupChangeWarning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GroupChangeWarning", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateJournal
   Description: Purpose:
Parameters:
<param name="ipJournalCode">journal code</param><param name="ds">ImportSubsid dataset row</param>
   OperationID: ValidateJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateJournal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ValidateJournal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBookCalendar
   Description: Purpose: retrive the book's calendar so it can be displayed on the form.
Parameters:
<param name="ipBookID">book id</param><param name="ds">ImportSubsid dataset row</param>
Notes:
   OperationID: GetBookCalendar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBookCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBookCalendar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GetBookCalendar", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckGroupID
   Description: Purpose:
Parameters:
<param name="ipGroupID">Journal Group to Create for this import</param><param name="ds">ImportSubsid dataset row</param><param name="opCreateGroup">prompt asking if it is okay to create the group</param>
Notes:
   OperationID: CheckGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGroupID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/CheckGroupID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckFiscalYear
   Description: Method to call when validating fiscal year
   OperationID: CheckFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFiscalYear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/CheckFiscalYear", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckFiscalPeriod
   Description: This method provides a warning message to present to the user if the given
Fiscal Year/Period has already been imported.  The user should be given the
choice to import it again.
            
The user's answer to the question "This fiscal period has previously been imported. Do you want to import it again?"
should be stored in MCConGen.OkToRegenerate.
            
In v6.10 Vantage, the user was never warned of a duplicate import--the system just
quietly did as it was told.
            
An exception is thrown if:
- no MCConGen dataset row is found
- the given Fiscal Year/Period is not valid
   OperationID: CheckFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFiscalPeriod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/CheckFiscalPeriod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateJournal
   Description: This method generates Journal Entries from a MCConsolImport dataset.
It is expected that the UI will first read a file from disk to create the
MCConsolImport dataset.
            
Each row in the MCConsolImport dataset that fails to "import" gets
updated with the reason for the failure in MCConsolImport.ImportErrorMsg,
and these are returned to the client;  if there are any technical failures,
such as improper datatypes in the input, all the
non-failing rows are backed out, and an exception is thrown.
Less serious failures, such as "Account not found", prevent only the import
of the problematic line--the remainder can still be accepted.
            
When successful, a MCConGen record is created in the database to indicate the
consolidation was performed.
            
An exception is thrown if:
- the GLJrnGrp indicated by the GroupId is nto found
- the fiscal period indicated by the GLJrnGrp is invalid
- the filename is blank
   OperationID: GenerateJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateJournal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GenerateJournal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ParseInputFile
   Description: Web support.
   OperationID: ParseInputFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseInputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseInputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ParseInputFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ParseInputFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConsImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GetNewConsImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsImportListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsImportRow[],
}

export interface Erp_Tablesets_ConsImportListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Description  */  
   "Description":string,
      /**  Unique Book Identifier  This is the book the import file is being loaded to.  */  
   "BookID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Date the input file was imported  */  
   "ImportDate":string,
      /**  Date used on the GLJrnDtl  */  
   "ApplyDate":string,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   "JournalCode":string,
      /**  Journal Header Description  */  
   "JrnlHeadDesc":string,
      /**   Indicates the status of the Import from Subsidiary.
C = Complete  */  
   "ImportStatus":string,
      /**  Import/Export file name.  */  
   "ImportFileName":string,
      /**  The consolidation generation log.  */  
   "GenerationLog":string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  logical indicating if it is okay to regenerate  */  
   "OkToRegenerate":boolean,
      /**  Date of Last Import  */  
   "LastImportDate":string,
      /**  Last Journal Group imported  */  
   "LastGroup":string,
      /**  Description of the last import  */  
   "LastDescription":string,
      /**  Last generation ID  */  
   "LastGenID":number,
      /**  Last Import File Name  */  
   "LastImportFile":string,
      /**  Logical indicating the user wants to create a new GLJrnGrp record.  */  
   "OkayToAddNewGroup":boolean,
      /**  Logical indicating the group fields are to be disabled.  */  
   "DisableGroupFields":boolean,
      /**  Calendar description.  */  
   "FiscalCalDescription":string,
      /**  Descripiton of Book  */  
   "GLBookDescription":string,
      /**  Indicates the base currency for the book  */  
   "GLBookCurrencyCode":string,
      /**  Journal  Description.  */  
   "JrnlCodeJrnlDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsImportRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Description  */  
   "Description":string,
      /**  Unique Book Identifier  This is the book the import file is being loaded to.  */  
   "BookID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Date the input file was imported  */  
   "ImportDate":string,
      /**  Date used on the GLJrnDtl  */  
   "ApplyDate":string,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   "JournalCode":string,
      /**  Journal Header Description  */  
   "JrnlHeadDesc":string,
      /**   Indicates the status of the Import from Subsidiary.
C = Complete  */  
   "ImportStatus":string,
      /**  Import/Export file name.  */  
   "ImportFileName":string,
      /**  The consolidation generation log.  */  
   "GenerationLog":string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  logical indicating if it is okay to regenerate  */  
   "OkToRegenerate":boolean,
      /**  Date of Last Import  */  
   "LastImportDate":string,
      /**  Last Journal Group imported  */  
   "LastGroup":string,
      /**  Description of the last import  */  
   "LastDescription":string,
      /**  Last generation ID  */  
   "LastGenID":number,
      /**  Last Import File Name  */  
   "LastImportFile":string,
      /**  Logical indicating the user wants to create a new GLJrnGrp record.  */  
   "OkayToAddNewGroup":boolean,
      /**  Logical indicating the group fields are to be disabled.  */  
   "DisableGroupFields":boolean,
   "BitFlag":number,
   "FiscalCalDescription":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
   "JrnlCodeJrnlDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipFiscalPeriod
      @param ds
   */  
export interface CheckFiscalPeriod_input{
      /**  fiscal period to validate  */  
   ipFiscalPeriod:number,
   ds:Erp_Tablesets_ImportSubsidTableset[],
}

export interface CheckFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
   pcMsg:string,
}
}

   /** Required : 
      @param proposedFiscalYear
      @param proposedSuffix
      @param ipCalendar
   */  
export interface CheckFiscalYear_input{
      /**  The proposed Fiscal Year  */  
   proposedFiscalYear:number,
      /**  The proposed Fiscal Year suffix  */  
   proposedSuffix:string,
      /**  Calendar ID  */  
   ipCalendar:string,
}

export interface CheckFiscalYear_output{
}

   /** Required : 
      @param ipGroupID
      @param ds
   */  
export interface CheckGroupID_input{
   ipGroupID:string,
   ds:Erp_Tablesets_ImportSubsidTableset[],
}

export interface CheckGroupID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
   opCreateGroup:string,
}
}

   /** Required : 
      @param genID
   */  
export interface DeleteByID_input{
   genID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ConsImportListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Description  */  
   Description:string,
      /**  Unique Book Identifier  This is the book the import file is being loaded to.  */  
   BookID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Date the input file was imported  */  
   ImportDate:string,
      /**  Date used on the GLJrnDtl  */  
   ApplyDate:string,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   JournalCode:string,
      /**  Journal Header Description  */  
   JrnlHeadDesc:string,
      /**   Indicates the status of the Import from Subsidiary.
C = Complete  */  
   ImportStatus:string,
      /**  Import/Export file name.  */  
   ImportFileName:string,
      /**  The consolidation generation log.  */  
   GenerationLog:string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  logical indicating if it is okay to regenerate  */  
   OkToRegenerate:boolean,
      /**  Date of Last Import  */  
   LastImportDate:string,
      /**  Last Journal Group imported  */  
   LastGroup:string,
      /**  Description of the last import  */  
   LastDescription:string,
      /**  Last generation ID  */  
   LastGenID:number,
      /**  Last Import File Name  */  
   LastImportFile:string,
      /**  Logical indicating the user wants to create a new GLJrnGrp record.  */  
   OkayToAddNewGroup:boolean,
      /**  Logical indicating the group fields are to be disabled.  */  
   DisableGroupFields:boolean,
      /**  Calendar description.  */  
   FiscalCalDescription:string,
      /**  Descripiton of Book  */  
   GLBookDescription:string,
      /**  Indicates the base currency for the book  */  
   GLBookCurrencyCode:string,
      /**  Journal  Description.  */  
   JrnlCodeJrnlDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsImportListTableset{
   ConsImportList:Erp_Tablesets_ConsImportListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConsImportRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Description  */  
   Description:string,
      /**  Unique Book Identifier  This is the book the import file is being loaded to.  */  
   BookID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Date the input file was imported  */  
   ImportDate:string,
      /**  Date used on the GLJrnDtl  */  
   ApplyDate:string,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   JournalCode:string,
      /**  Journal Header Description  */  
   JrnlHeadDesc:string,
      /**   Indicates the status of the Import from Subsidiary.
C = Complete  */  
   ImportStatus:string,
      /**  Import/Export file name.  */  
   ImportFileName:string,
      /**  The consolidation generation log.  */  
   GenerationLog:string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  logical indicating if it is okay to regenerate  */  
   OkToRegenerate:boolean,
      /**  Date of Last Import  */  
   LastImportDate:string,
      /**  Last Journal Group imported  */  
   LastGroup:string,
      /**  Description of the last import  */  
   LastDescription:string,
      /**  Last generation ID  */  
   LastGenID:number,
      /**  Last Import File Name  */  
   LastImportFile:string,
      /**  Logical indicating the user wants to create a new GLJrnGrp record.  */  
   OkayToAddNewGroup:boolean,
      /**  Logical indicating the group fields are to be disabled.  */  
   DisableGroupFields:boolean,
   BitFlag:number,
   FiscalCalDescription:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
   JrnlCodeJrnlDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   BookMode:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  */  
   PostErrorLog:string,
      /**  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  */  
   JEDate:string,
      /**  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   FiscalYear:number,
      /**  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   FiscalPeriod:number,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  */  
   FiscalPeriodType:string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   CloseFiscalPeriod:number,
      /**  It is true, if all records for this group were posted.  */  
   Posted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Periods List. The value will be populated in the BO logic containing Ordinary or Closing periods.  */  
   DspFiscalPeriod:string,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   HasDetails:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  Indicates that Book Mode cannot be changed by user  */  
   BookModeDisabled:boolean,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods
S - Opening
Calculated based on the Book Selected.  */  
   DspFiscalPeriodType:string,
   BitFlag:number,
   BookIDCurrencyCode:string,
   BookIDDescription:string,
   BookIDCorrAccounting:boolean,
   FiscalCalDescription:string,
   JournalCodeAllowStatJournals:boolean,
   JournalCodeJrnlDescription:string,
   RateGrpCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportSubsidTableset{
   ConsImport:Erp_Tablesets_ConsImportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MCConsolImportExportRow{
      /**  Transaction amount.  */  
   DebitAmt:number,
      /**  Transaction amount.  */  
   CreditAmt:number,
      /**  A character string made up of Div, Dept, Chart and Segment abbreviations concatenated into the full GL account description.  This should be formatted exactly how the user expects to see their account numbers (including separators).  */  
   AcctDesc:string,
      /**  Reason import of this record failed.  Blank implies no error occurred.  */  
   ImportErrorMsg:string,
   SegValue1:string,
      /**  GL Account  */  
   GLAccount:string,
      /**  Segment Value 2  */  
   SegValue2:string,
   SegValue3:string,
      /**  Segment Value 4  */  
   SegValue4:string,
      /**  Segment Value 5  */  
   SegValue5:string,
      /**  Segment Value 6  */  
   SegValue6:string,
      /**  Segment Value 7  */  
   SegValue7:string,
      /**  Segment Value 8  */  
   SegValue8:string,
      /**  Segment Value 9  */  
   SegValue9:string,
      /**  SegmentValue 10  */  
   SegValue10:string,
      /**  Segment Value 11  */  
   SegValue11:string,
      /**  Segment Value 12  */  
   SegValue12:string,
      /**  Segment Value 13  */  
   SegValue13:string,
      /**  Segment Value 14  */  
   SegValue14:string,
      /**  Segment Value 15  */  
   SegValue15:string,
      /**  Segment Value 16  */  
   SegValue16:string,
      /**  Segment Value 17  */  
   SegValue17:string,
      /**  Segment Value 18  */  
   SegValue18:string,
      /**  Segment Value 19  */  
   SegValue19:string,
      /**  Segment Value 20  */  
   SegValue20:string,
      /**  Journal Code  */  
   JournalCode:string,
      /**  Company where the data originated  */  
   SrcCompany:string,
      /**  Source Book ID  */  
   SrcBook:string,
      /**  Source GL Account  */  
   SrcGLAccount:string,
      /**  Source  Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Num  */  
   SrcJournalNum:number,
      /**  Source COA Code  */  
   SrcCOACode:string,
      /**  Source Journal LIne  */  
   SrcJournalLIne:number,
      /**  External COA code  */  
   ExtCOACode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MCConsolImportExportTableset{
   MCConsolImportExport:Erp_Tablesets_MCConsolImportExportRow[],
   GLJrnGrp:Erp_Tablesets_GLJrnGrpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtImportSubsidTableset{
   ConsImport:Erp_Tablesets_ConsImportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param ds1
   */  
export interface GenerateJournal_input{
   ds:Erp_Tablesets_ImportSubsidTableset[],
   ds1:Erp_Tablesets_MCConsolImportExportTableset[],
}

export interface GenerateJournal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
   ds1:Erp_Tablesets_MCConsolImportExportTableset[],
}
}

   /** Required : 
      @param ipBookID
      @param ds
   */  
export interface GetBookCalendar_input{
   ipBookID:string,
   ds:Erp_Tablesets_ImportSubsidTableset[],
}

export interface GetBookCalendar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
}
}

   /** Required : 
      @param genID
   */  
export interface GetByID_input{
   genID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ImportSubsidTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ImportSubsidTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ImportSubsidTableset[],
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
   returnObj:Erp_Tablesets_ConsImportListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewConsImport_input{
   ds:Erp_Tablesets_ImportSubsidTableset[],
}

export interface GetNewConsImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
}
}

   /** Required : 
      @param whereClauseConsImport
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseConsImport:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ImportSubsidTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipBook
      @param ds
   */  
export interface GroupChangeWarning_input{
   ipBook:string,
   ds:Erp_Tablesets_ImportSubsidTableset[],
}

export interface GroupChangeWarning_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
   warnMsg:string,
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
      @param sFileSubPath
      @param ds
   */  
export interface ParseInputFile_input{
      /**  Imported file subpath of SpecialFolder.UserData.  */  
   sFileSubPath:string,
   ds:Erp_Tablesets_MCConsolImportExportTableset[],
}

export interface ParseInputFile_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MCConsolImportExportTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtImportSubsidTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtImportSubsidTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ImportSubsidTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
}
}

   /** Required : 
      @param ipJournalCode
      @param ds
   */  
export interface ValidateJournal_input{
   ipJournalCode:string,
   ds:Erp_Tablesets_ImportSubsidTableset[],
}

export interface ValidateJournal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportSubsidTableset[],
}
}

