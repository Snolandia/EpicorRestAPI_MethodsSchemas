import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DataExportSvc
// Description: Data Export Tool
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/$metadata", {
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
   Description: Get DataExports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportDefRow
   */  
export function get_DataExports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExport item
   Description: Calls GetByID to retrieve the DataExport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
   */  
export function get_DataExports_Company_DefinitionID(Company:string, DefinitionID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExport for the service
   Description: Calls UpdateExt to update DataExport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExports_Company_DefinitionID(Company:string, DefinitionID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")", {
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
   Summary: Call UpdateExt to delete DataExport item
   Description: Call UpdateExt to delete DataExport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExports_Company_DefinitionID(Company:string, DefinitionID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")", {
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
   Description: Get DataExportHistories items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportHistories1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportHistoryRow
   */  
export function get_DataExports_Company_DefinitionID_DataExportHistories(Company:string, DefinitionID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportHistories", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportHistory item
   Description: Calls GetByID to retrieve the DataExportHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportHistory1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   */  
export function get_DataExports_Company_DefinitionID_DataExportHistories_Company_DefinitionID_iCounter(Company:string, DefinitionID:string, iCounter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataExportOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportOptions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportOptionRow
   */  
export function get_DataExports_Company_DefinitionID_DataExportOptions(Company:string, DefinitionID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportOptions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportOption item
   Description: Calls GetByID to retrieve the DataExportOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportOption1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param OptionName Desc: OptionName   Required: True   Allow empty value : True
      @param TableOption Desc: TableOption   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   */  
export function get_DataExports_Company_DefinitionID_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company:string, DefinitionID:string, OptionName:string, TableOption:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataExportTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportTables1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableRow
   */  
export function get_DataExports_Company_DefinitionID_DataExportTables(Company:string, DefinitionID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportTable item
   Description: Calls GetByID to retrieve the DataExportTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTable1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   */  
export function get_DataExports_Company_DefinitionID_DataExportTables_Company_DefinitionID_TableName(Company:string, DefinitionID:string, TableName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DataExportHistories items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportHistories
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportHistoryRow
   */  
export function get_DataExportHistories(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportHistories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportHistories(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportHistory item
   Description: Calls GetByID to retrieve the DataExportHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   */  
export function get_DataExportHistories_Company_DefinitionID_iCounter(Company:string, DefinitionID:string, iCounter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportHistory for the service
   Description: Calls UpdateExt to update DataExportHistory. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportHistories_Company_DefinitionID_iCounter(Company:string, DefinitionID:string, iCounter:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")", {
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
   Summary: Call UpdateExt to delete DataExportHistory item
   Description: Call UpdateExt to delete DataExportHistory item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportHistories_Company_DefinitionID_iCounter(Company:string, DefinitionID:string, iCounter:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")", {
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
   Description: Get DataExportOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportOptions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportOptionRow
   */  
export function get_DataExportOptions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportOption item
   Description: Calls GetByID to retrieve the DataExportOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportOption
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param OptionName Desc: OptionName   Required: True   Allow empty value : True
      @param TableOption Desc: TableOption   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   */  
export function get_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company:string, DefinitionID:string, OptionName:string, TableOption:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportOptionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportOptionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportOption for the service
   Description: Calls UpdateExt to update DataExportOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportOption
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param OptionName Desc: OptionName   Required: True   Allow empty value : True
      @param TableOption Desc: TableOption   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company:string, DefinitionID:string, OptionName:string, TableOption:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")", {
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
   Summary: Call UpdateExt to delete DataExportOption item
   Description: Call UpdateExt to delete DataExportOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportOption
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param OptionName Desc: OptionName   Required: True   Allow empty value : True
      @param TableOption Desc: TableOption   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company:string, DefinitionID:string, OptionName:string, TableOption:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")", {
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
   Description: Get DataExportTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableRow
   */  
export function get_DataExportTables(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportTable item
   Description: Calls GetByID to retrieve the DataExportTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTable
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   */  
export function get_DataExportTables_Company_DefinitionID_TableName(Company:string, DefinitionID:string, TableName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportTable for the service
   Description: Calls UpdateExt to update DataExportTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportTable
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportTables_Company_DefinitionID_TableName(Company:string, DefinitionID:string, TableName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")", {
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
   Summary: Call UpdateExt to delete DataExportTable item
   Description: Call UpdateExt to delete DataExportTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportTable
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportTables_Company_DefinitionID_TableName(Company:string, DefinitionID:string, TableName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")", {
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
   Description: Get DataExportColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportColumns1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnRow
   */  
export function get_DataExportTables_Company_DefinitionID_TableName_DataExportColumns(Company:string, DefinitionID:string, TableName:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportColumn item
   Description: Calls GetByID to retrieve the DataExportColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumn1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   */  
export function get_DataExportTables_Company_DefinitionID_TableName_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataExportTableAttributes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportTableAttributes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableAttributeRow
   */  
export function get_DataExportTables_Company_DefinitionID_TableName_DataExportTableAttributes(Company:string, DefinitionID:string, TableName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableAttributes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportTableAttribute item
   Description: Calls GetByID to retrieve the DataExportTableAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableAttribute1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   */  
export function get_DataExportTables_Company_DefinitionID_TableName_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company:string, DefinitionID:string, TableName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportTableAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportTableAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataExportTableParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportTableParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableParamRow
   */  
export function get_DataExportTables_Company_DefinitionID_TableName_DataExportTableParams(Company:string, DefinitionID:string, TableName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportTableParam item
   Description: Calls GetByID to retrieve the DataExportTableParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   */  
export function get_DataExportTables_Company_DefinitionID_TableName_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company:string, DefinitionID:string, TableName:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportTableParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportTableParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DataExportColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportColumns
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnRow
   */  
export function get_DataExportColumns(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportColumn item
   Description: Calls GetByID to retrieve the DataExportColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   */  
export function get_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportColumn for the service
   Description: Calls UpdateExt to update DataExportColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportColumn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")", {
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
   Summary: Call UpdateExt to delete DataExportColumn item
   Description: Call UpdateExt to delete DataExportColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportColumn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")", {
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
   Description: Get DataExportColumnAttributes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportColumnAttributes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnAttributeRow
   */  
export function get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnAttributes(Company:string, DefinitionID:string, TableName:string, ColumnName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnAttributes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportColumnAttribute item
   Description: Calls GetByID to retrieve the DataExportColumnAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnAttribute1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   */  
export function get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportColumnAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportColumnAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataExportColumnLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportColumnLinks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnLinkRow
   */  
export function get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnLinks(Company:string, DefinitionID:string, TableName:string, ColumnName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnLinks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportColumnLink item
   Description: Calls GetByID to retrieve the DataExportColumnLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnLink1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   */  
export function get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company:string, DefinitionID:string, TableName:string, ColumnName:string, iCounter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportColumnLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportColumnLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DataExportColumnAttributes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportColumnAttributes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnAttributeRow
   */  
export function get_DataExportColumnAttributes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportColumnAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportColumnAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportColumnAttribute item
   Description: Calls GetByID to retrieve the DataExportColumnAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnAttribute
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   */  
export function get_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportColumnAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportColumnAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportColumnAttribute for the service
   Description: Calls UpdateExt to update DataExportColumnAttribute. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportColumnAttribute
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, AttributeName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")", {
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
   Summary: Call UpdateExt to delete DataExportColumnAttribute item
   Description: Call UpdateExt to delete DataExportColumnAttribute item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportColumnAttribute
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company:string, DefinitionID:string, TableName:string, ColumnName:string, AttributeName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")", {
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
   Description: Get DataExportColumnLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportColumnLinks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnLinkRow
   */  
export function get_DataExportColumnLinks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportColumnLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportColumnLinks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportColumnLink item
   Description: Calls GetByID to retrieve the DataExportColumnLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   */  
export function get_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company:string, DefinitionID:string, TableName:string, ColumnName:string, iCounter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportColumnLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportColumnLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportColumnLink for the service
   Description: Calls UpdateExt to update DataExportColumnLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportColumnLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company:string, DefinitionID:string, TableName:string, ColumnName:string, iCounter:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")", {
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
   Summary: Call UpdateExt to delete DataExportColumnLink item
   Description: Call UpdateExt to delete DataExportColumnLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportColumnLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param iCounter Desc: iCounter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company:string, DefinitionID:string, TableName:string, ColumnName:string, iCounter:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")", {
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
   Description: Get DataExportTableAttributes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportTableAttributes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableAttributeRow
   */  
export function get_DataExportTableAttributes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportTableAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportTableAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportTableAttribute item
   Description: Calls GetByID to retrieve the DataExportTableAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableAttribute
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   */  
export function get_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company:string, DefinitionID:string, TableName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportTableAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportTableAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportTableAttribute for the service
   Description: Calls UpdateExt to update DataExportTableAttribute. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportTableAttribute
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company:string, DefinitionID:string, TableName:string, AttributeName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")", {
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
   Summary: Call UpdateExt to delete DataExportTableAttribute item
   Description: Call UpdateExt to delete DataExportTableAttribute item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportTableAttribute
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company:string, DefinitionID:string, TableName:string, AttributeName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")", {
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
   Description: Get DataExportTableParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportTableParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableParamRow
   */  
export function get_DataExportTableParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportTableParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataExportTableParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataExportTableParam item
   Description: Calls GetByID to retrieve the DataExportTableParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   */  
export function get_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company:string, DefinitionID:string, TableName:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataExportTableParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataExportTableParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataExportTableParam for the service
   Description: Calls UpdateExt to update DataExportTableParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportTableParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company:string, DefinitionID:string, TableName:string, ParamName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")", {
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
   Summary: Call UpdateExt to delete DataExportTableParam item
   Description: Call UpdateExt to delete DataExportTableParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportTableParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company:string, DefinitionID:string, TableName:string, ParamName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportDefListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDataExportDef:string, whereClauseDataExportHistory:string, whereClauseDataExportOption:string, whereClauseDataExportTable:string, whereClauseDataExportColumn:string, whereClauseDataExportColumnAttribute:string, whereClauseDataExportColumnLink:string, whereClauseDataExportTableAttribute:string, whereClauseDataExportTableParam:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDataExportDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportDef=" + whereClauseDataExportDef
   }
   if(typeof whereClauseDataExportHistory!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportHistory=" + whereClauseDataExportHistory
   }
   if(typeof whereClauseDataExportOption!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportOption=" + whereClauseDataExportOption
   }
   if(typeof whereClauseDataExportTable!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportTable=" + whereClauseDataExportTable
   }
   if(typeof whereClauseDataExportColumn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportColumn=" + whereClauseDataExportColumn
   }
   if(typeof whereClauseDataExportColumnAttribute!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportColumnAttribute=" + whereClauseDataExportColumnAttribute
   }
   if(typeof whereClauseDataExportColumnLink!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportColumnLink=" + whereClauseDataExportColumnLink
   }
   if(typeof whereClauseDataExportTableAttribute!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportTableAttribute=" + whereClauseDataExportTableAttribute
   }
   if(typeof whereClauseDataExportTableParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataExportTableParam=" + whereClauseDataExportTableParam
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetRows" + params, {
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
export function get_GetByID(definitionID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof definitionID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "definitionID=" + definitionID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetList" + params, {
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
   Summary: Invoke method DuplicateDefinition
   OperationID: DuplicateDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateDefinition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DuplicateDefinition", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportDefinition
   OperationID: ExportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportDefinition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/ExportDefinition", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportDefinition
   OperationID: ImportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportDefinition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/ImportDefinition", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Generate
   OperationID: Generate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Generate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Generate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/Generate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateToServerFolder
   OperationID: GenerateToServerFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateToServerFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateToServerFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateToServerFolder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GenerateToServerFolder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDateFormats
   Description: This method returns a list of date formats
   OperationID: GetDateFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateFormats_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDateFormats(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetDateFormats", {
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
   Summary: Invoke method GetFieldList
   Description: This method returns a list of Fields
   OperationID: GetFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetFieldList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTableList
   Description: This method returns a list of Tables
   OperationID: GetTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetTableList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetForeignTblFieldList
   Description: This method returns a list of Foreign Fields excluding already used for links
   OperationID: GetForeignTblFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetForeignTblFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForeignTblFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetForeignTblFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetForeignTblFieldList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOwnTblFieldList
   Description: This method returns a list of Own Fields excluding already used for links
   OperationID: GetOwnTblFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOwnTblFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOwnTblFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOwnTblFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetOwnTblFieldList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetForeignTableList
   Description: This method returns a list of Foreign Key Tables
   OperationID: GetForeignTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetForeignTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForeignTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetForeignTableList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetForeignTableList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTablesListWithWrongSource
   Description: Get the list of tables, for which data source do not exist.
   OperationID: GetTablesListWithWrongSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTablesListWithWrongSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesListWithWrongSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTablesListWithWrongSource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetTablesListWithWrongSource", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsPostingsExist
   Description: Check that postings exist in specified period.
   OperationID: IsPostingsExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsPostingsExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPostingsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsPostingsExist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/IsPostingsExist", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeGLBook
   Description: Call method when the over rides the check # in Process Payment.
   OperationID: OnChangeGLBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGLBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGLBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeGLBook(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/OnChangeGLBook", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnRetrieveColumns
   OperationID: OnRetrieveColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnRetrieveColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnRetrieveColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnRetrieveColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/OnRetrieveColumns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshDataExportDef
   Description: This method will refresh data in tableset for DataExportDef table.
<param name="ds" type="Erp.Tablesets.DataExportDataSet">Erp.Tablesets.DataExportDataSet</param>
   OperationID: RefreshDataExportDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshDataExportDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshDataExportDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshDataExportDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/RefreshDataExportDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetGDPdUMode
   Description: <param name="ds" type="Erp.Tablesets.DataExportDataSet">Erp.Tablesets.DataExportDataSet</param>
   OperationID: SetGDPdUMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetGDPdUMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetGDPdUMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetGDPdUMode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/SetGDPdUMode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StoreData
   Description: This method will require that all dataset records have a value of 'A' in the corresponding
rowident field/column.
<param name="ipDefinitionID">Definition ID</param><param name="ds" type="Erp.Tablesets.DataExportDataSet">Erp.Tablesets.DataExportDataSet</param>
   OperationID: StoreData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StoreData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StoreData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StoreData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/StoreData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportHistory
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportHistory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportHistory", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportOption
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportOption", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportColumn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportColumn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportColumnAttribute
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportColumnAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportColumnAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportColumnAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportColumnAttribute(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportColumnAttribute", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportColumnLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportColumnLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportColumnLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportColumnLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportColumnLink(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportColumnLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportTableAttribute
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportTableAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportTableAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportTableAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportTableAttribute(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportTableAttribute", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDataExportTableParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportTableParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportTableParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportTableParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataExportTableParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetNewDataExportTableParam", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnAttributeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportColumnAttributeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnLinkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportColumnLinkRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportColumnRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportDefListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportDefRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportHistoryRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportHistoryRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportOptionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportOptionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableAttributeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportTableAttributeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportTableParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataExportTableRow[],
}

export interface Erp_Tablesets_DataExportColumnAttributeRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  TableName  */  
   "TableName":string,
      /**  ColumnName  */  
   "ColumnName":string,
      /**  AttributeName  */  
   "AttributeName":string,
      /**  AttributeValue  */  
   "AttributeValue":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportColumnLinkRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  TableName  */  
   "TableName":string,
      /**  ColumnName  */  
   "ColumnName":string,
      /**  iCounter  */  
   "iCounter":number,
      /**  TblColumnName  */  
   "TblColumnName":string,
      /**  ForeignTblColumnName  */  
   "ForeignTblColumnName":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportColumnRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  TableName  */  
   "TableName":string,
      /**  ColumnName  */  
   "ColumnName":string,
      /**  Description  */  
   "Description":string,
      /**  ColumnType  */  
   "ColumnType":string,
      /**  Accuracy  */  
   "Accuracy":number,
      /**  IsVarPrimaryKey  */  
   "IsVarPrimaryKey":boolean,
      /**  IsForeignKey  */  
   "IsForeignKey":boolean,
      /**  ForeignKeyTableName  */  
   "ForeignKeyTableName":string,
      /**  ForeignKeyColumnName  */  
   "ForeignKeyColumnName":string,
      /**  ColumnOrder  */  
   "ColumnOrder":number,
      /**  FooterSType  */  
   "FooterSType":string,
      /**  FooterSOrder  */  
   "FooterSOrder":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Alias  */  
   "Alias":string,
      /**  FooterSNode  */  
   "FooterSNode":string,
      /**  IsHidden  */  
   "IsHidden":boolean,
      /**  DisplayName  */  
   "DisplayName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportDefListRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  Description  */  
   "Description":string,
      /**  SelectionMethod  */  
   "SelectionMethod":string,
      /**  ExportFolder  */  
   "ExportFolder":string,
      /**  DateFormat  */  
   "DateFormat":string,
      /**  DecimalSeparator  */  
   "DecimalSeparator":string,
      /**  ThousandSeparator  */  
   "ThousandSeparator":string,
      /**  IsReleased  */  
   "IsReleased":boolean,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  Comments  */  
   "Comments":string,
      /**  BookID  */  
   "BookID":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  StartDate  */  
   "StartDate":string,
      /**  StartDateToken  */  
   "StartDateToken":string,
      /**  StartPeriod  */  
   "StartPeriod":number,
      /**  EndDate  */  
   "EndDate":string,
      /**  EndDateToken  */  
   "EndDateToken":string,
      /**  EndPeriod  */  
   "EndPeriod":number,
      /**  LastRunDate  */  
   "LastRunDate":string,
      /**  LastRunBy  */  
   "LastRunBy":string,
      /**  UpdatedDate  */  
   "UpdatedDate":string,
      /**  UpdatedBy  */  
   "UpdatedBy":string,
      /**  URLforDTD  */  
   "URLforDTD":string,
      /**  IsUsed  */  
   "IsUsed":boolean,
      /**  GenerateIndex  */  
   "GenerateIndex":boolean,
      /**  CommonFileName  */  
   "CommonFileName":string,
      /**  RootNodeName  */  
   "RootNodeName":string,
      /**  DSymbol  */  
   "DSymbol":string,
      /**  LESymbol  */  
   "LESymbol":string,
      /**  QSymbol  */  
   "QSymbol":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  FileType  */  
   "FileType":string,
      /**  IsCommonFile  */  
   "IsCommonFile":boolean,
      /**  AddRecordType  */  
   "AddRecordType":boolean,
      /**  AddCommonFooter  */  
   "AddCommonFooter":boolean,
      /**  CommonFooter  */  
   "CommonFooter":string,
      /**  Encoding  */  
   "Encoding":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportDefRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  Description  */  
   "Description":string,
      /**  SelectionMethod  */  
   "SelectionMethod":string,
      /**  ExportFolder  */  
   "ExportFolder":string,
      /**  DateFormat  */  
   "DateFormat":string,
      /**  DecimalSeparator  */  
   "DecimalSeparator":string,
      /**  ThousandSeparator  */  
   "ThousandSeparator":string,
      /**  IsReleased  */  
   "IsReleased":boolean,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  Comments  */  
   "Comments":string,
      /**  BookID  */  
   "BookID":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  StartDate  */  
   "StartDate":string,
      /**  StartDateToken  */  
   "StartDateToken":string,
      /**  StartPeriod  */  
   "StartPeriod":number,
      /**  EndDate  */  
   "EndDate":string,
      /**  EndDateToken  */  
   "EndDateToken":string,
      /**  EndPeriod  */  
   "EndPeriod":number,
      /**  LastRunDate  */  
   "LastRunDate":string,
      /**  LastRunBy  */  
   "LastRunBy":string,
      /**  UpdatedDate  */  
   "UpdatedDate":string,
      /**  UpdatedBy  */  
   "UpdatedBy":string,
      /**  URLforDTD  */  
   "URLforDTD":string,
      /**  IsUsed  */  
   "IsUsed":boolean,
      /**  GenerateIndex  */  
   "GenerateIndex":boolean,
      /**  CommonFileName  */  
   "CommonFileName":string,
      /**  RootNodeName  */  
   "RootNodeName":string,
      /**  DSymbol  */  
   "DSymbol":string,
      /**  LESymbol  */  
   "LESymbol":string,
      /**  QSymbol  */  
   "QSymbol":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  FileType  */  
   "FileType":string,
      /**  IsCommonFile  */  
   "IsCommonFile":boolean,
      /**  AddRecordType  */  
   "AddRecordType":boolean,
      /**  AddCommonFooter  */  
   "AddCommonFooter":boolean,
      /**  CommonFooter  */  
   "CommonFooter":string,
      /**  Encoding  */  
   "Encoding":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportHistoryRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  iCounter  */  
   "iCounter":number,
      /**  Action  */  
   "Action":string,
      /**  ActionDate  */  
   "ActionDate":string,
      /**  UserID  */  
   "UserID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportOptionRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  OptionName  */  
   "OptionName":string,
      /**  TableOption  */  
   "TableOption":string,
      /**  OptionType  */  
   "OptionType":string,
      /**  DefaultOption  */  
   "DefaultOption":boolean,
      /**  IntegerCol  */  
   "IntegerCol":number,
      /**  DecimalCol  */  
   "DecimalCol":number,
      /**  LogicalCol  */  
   "LogicalCol":boolean,
      /**  StringCol  */  
   "StringCol":string,
      /**  DateCol  */  
   "DateCol":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportTableAttributeRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  TableName  */  
   "TableName":string,
      /**  AttributeName  */  
   "AttributeName":string,
      /**  AttributeValue  */  
   "AttributeValue":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportTableParamRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  TableName  */  
   "TableName":string,
      /**  ParamName  */  
   "ParamName":string,
      /**  ParamType  */  
   "ParamType":string,
      /**  ReportParameter  */  
   "ReportParameter":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataExportTableRow{
      /**  Company  */  
   "Company":string,
      /**  DefinitionID  */  
   "DefinitionID":string,
      /**  TableName  */  
   "TableName":string,
      /**  Description  */  
   "Description":string,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  FileName  */  
   "FileName":string,
      /**  GenerateMethod  */  
   "GenerateMethod":string,
      /**  DataSource  */  
   "DataSource":string,
      /**  DataSourceID  */  
   "DataSourceID":string,
      /**  ExportFileType  */  
   "ExportFileType":string,
      /**  IncludeHeader  */  
   "IncludeHeader":boolean,
      /**  DSymbol  */  
   "DSymbol":string,
      /**  ExportMethod  */  
   "ExportMethod":string,
      /**  TableOrder  */  
   "TableOrder":number,
      /**  AddHeader  */  
   "AddHeader":string,
      /**  AddFooter  */  
   "AddFooter":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param definitionID
   */  
export interface DeleteByID_input{
   definitionID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipGDPdUMode
      @param ipSourceDefinitionID
      @param ipTargetDefinitionID
   */  
export interface DuplicateDefinition_input{
      /**  GDPdU Mode  */  
   ipGDPdUMode:boolean,
      /**  Source Definition ID  */  
   ipSourceDefinitionID:string,
      /**  Target (new) Definition ID  */  
   ipTargetDefinitionID:string,
}

export interface DuplicateDefinition_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

export interface Erp_Tablesets_DataExportColumnAttributeRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  TableName  */  
   TableName:string,
      /**  ColumnName  */  
   ColumnName:string,
      /**  AttributeName  */  
   AttributeName:string,
      /**  AttributeValue  */  
   AttributeValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportColumnLinkRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  TableName  */  
   TableName:string,
      /**  ColumnName  */  
   ColumnName:string,
      /**  iCounter  */  
   iCounter:number,
      /**  TblColumnName  */  
   TblColumnName:string,
      /**  ForeignTblColumnName  */  
   ForeignTblColumnName:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportColumnRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  TableName  */  
   TableName:string,
      /**  ColumnName  */  
   ColumnName:string,
      /**  Description  */  
   Description:string,
      /**  ColumnType  */  
   ColumnType:string,
      /**  Accuracy  */  
   Accuracy:number,
      /**  IsVarPrimaryKey  */  
   IsVarPrimaryKey:boolean,
      /**  IsForeignKey  */  
   IsForeignKey:boolean,
      /**  ForeignKeyTableName  */  
   ForeignKeyTableName:string,
      /**  ForeignKeyColumnName  */  
   ForeignKeyColumnName:string,
      /**  ColumnOrder  */  
   ColumnOrder:number,
      /**  FooterSType  */  
   FooterSType:string,
      /**  FooterSOrder  */  
   FooterSOrder:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Alias  */  
   Alias:string,
      /**  FooterSNode  */  
   FooterSNode:string,
      /**  IsHidden  */  
   IsHidden:boolean,
      /**  DisplayName  */  
   DisplayName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportDefListRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  Description  */  
   Description:string,
      /**  SelectionMethod  */  
   SelectionMethod:string,
      /**  ExportFolder  */  
   ExportFolder:string,
      /**  DateFormat  */  
   DateFormat:string,
      /**  DecimalSeparator  */  
   DecimalSeparator:string,
      /**  ThousandSeparator  */  
   ThousandSeparator:string,
      /**  IsReleased  */  
   IsReleased:boolean,
      /**  Inactive  */  
   Inactive:boolean,
      /**  Comments  */  
   Comments:string,
      /**  BookID  */  
   BookID:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  StartDate  */  
   StartDate:string,
      /**  StartDateToken  */  
   StartDateToken:string,
      /**  StartPeriod  */  
   StartPeriod:number,
      /**  EndDate  */  
   EndDate:string,
      /**  EndDateToken  */  
   EndDateToken:string,
      /**  EndPeriod  */  
   EndPeriod:number,
      /**  LastRunDate  */  
   LastRunDate:string,
      /**  LastRunBy  */  
   LastRunBy:string,
      /**  UpdatedDate  */  
   UpdatedDate:string,
      /**  UpdatedBy  */  
   UpdatedBy:string,
      /**  URLforDTD  */  
   URLforDTD:string,
      /**  IsUsed  */  
   IsUsed:boolean,
      /**  GenerateIndex  */  
   GenerateIndex:boolean,
      /**  CommonFileName  */  
   CommonFileName:string,
      /**  RootNodeName  */  
   RootNodeName:string,
      /**  DSymbol  */  
   DSymbol:string,
      /**  LESymbol  */  
   LESymbol:string,
      /**  QSymbol  */  
   QSymbol:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  FileType  */  
   FileType:string,
      /**  IsCommonFile  */  
   IsCommonFile:boolean,
      /**  AddRecordType  */  
   AddRecordType:boolean,
      /**  AddCommonFooter  */  
   AddCommonFooter:boolean,
      /**  CommonFooter  */  
   CommonFooter:string,
      /**  Encoding  */  
   Encoding:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportDefRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  Description  */  
   Description:string,
      /**  SelectionMethod  */  
   SelectionMethod:string,
      /**  ExportFolder  */  
   ExportFolder:string,
      /**  DateFormat  */  
   DateFormat:string,
      /**  DecimalSeparator  */  
   DecimalSeparator:string,
      /**  ThousandSeparator  */  
   ThousandSeparator:string,
      /**  IsReleased  */  
   IsReleased:boolean,
      /**  Inactive  */  
   Inactive:boolean,
      /**  Comments  */  
   Comments:string,
      /**  BookID  */  
   BookID:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  StartDate  */  
   StartDate:string,
      /**  StartDateToken  */  
   StartDateToken:string,
      /**  StartPeriod  */  
   StartPeriod:number,
      /**  EndDate  */  
   EndDate:string,
      /**  EndDateToken  */  
   EndDateToken:string,
      /**  EndPeriod  */  
   EndPeriod:number,
      /**  LastRunDate  */  
   LastRunDate:string,
      /**  LastRunBy  */  
   LastRunBy:string,
      /**  UpdatedDate  */  
   UpdatedDate:string,
      /**  UpdatedBy  */  
   UpdatedBy:string,
      /**  URLforDTD  */  
   URLforDTD:string,
      /**  IsUsed  */  
   IsUsed:boolean,
      /**  GenerateIndex  */  
   GenerateIndex:boolean,
      /**  CommonFileName  */  
   CommonFileName:string,
      /**  RootNodeName  */  
   RootNodeName:string,
      /**  DSymbol  */  
   DSymbol:string,
      /**  LESymbol  */  
   LESymbol:string,
      /**  QSymbol  */  
   QSymbol:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  FileType  */  
   FileType:string,
      /**  IsCommonFile  */  
   IsCommonFile:boolean,
      /**  AddRecordType  */  
   AddRecordType:boolean,
      /**  AddCommonFooter  */  
   AddCommonFooter:boolean,
      /**  CommonFooter  */  
   CommonFooter:string,
      /**  Encoding  */  
   Encoding:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportHistoryRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  iCounter  */  
   iCounter:number,
      /**  Action  */  
   Action:string,
      /**  ActionDate  */  
   ActionDate:string,
      /**  UserID  */  
   UserID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportListTableset{
   DataExportDefList:Erp_Tablesets_DataExportDefListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DataExportOptionRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  OptionName  */  
   OptionName:string,
      /**  TableOption  */  
   TableOption:string,
      /**  OptionType  */  
   OptionType:string,
      /**  DefaultOption  */  
   DefaultOption:boolean,
      /**  IntegerCol  */  
   IntegerCol:number,
      /**  DecimalCol  */  
   DecimalCol:number,
      /**  LogicalCol  */  
   LogicalCol:boolean,
      /**  StringCol  */  
   StringCol:string,
      /**  DateCol  */  
   DateCol:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportTableAttributeRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  TableName  */  
   TableName:string,
      /**  AttributeName  */  
   AttributeName:string,
      /**  AttributeValue  */  
   AttributeValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportTableParamRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  TableName  */  
   TableName:string,
      /**  ParamName  */  
   ParamName:string,
      /**  ParamType  */  
   ParamType:string,
      /**  ReportParameter  */  
   ReportParameter:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportTableRow{
      /**  Company  */  
   Company:string,
      /**  DefinitionID  */  
   DefinitionID:string,
      /**  TableName  */  
   TableName:string,
      /**  Description  */  
   Description:string,
      /**  Inactive  */  
   Inactive:boolean,
      /**  FileName  */  
   FileName:string,
      /**  GenerateMethod  */  
   GenerateMethod:string,
      /**  DataSource  */  
   DataSource:string,
      /**  DataSourceID  */  
   DataSourceID:string,
      /**  ExportFileType  */  
   ExportFileType:string,
      /**  IncludeHeader  */  
   IncludeHeader:boolean,
      /**  DSymbol  */  
   DSymbol:string,
      /**  ExportMethod  */  
   ExportMethod:string,
      /**  TableOrder  */  
   TableOrder:number,
      /**  AddHeader  */  
   AddHeader:string,
      /**  AddFooter  */  
   AddFooter:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataExportTableset{
   DataExportDef:Erp_Tablesets_DataExportDefRow[],
   DataExportHistory:Erp_Tablesets_DataExportHistoryRow[],
   DataExportOption:Erp_Tablesets_DataExportOptionRow[],
   DataExportTable:Erp_Tablesets_DataExportTableRow[],
   DataExportColumn:Erp_Tablesets_DataExportColumnRow[],
   DataExportColumnAttribute:Erp_Tablesets_DataExportColumnAttributeRow[],
   DataExportColumnLink:Erp_Tablesets_DataExportColumnLinkRow[],
   DataExportTableAttribute:Erp_Tablesets_DataExportTableAttributeRow[],
   DataExportTableParam:Erp_Tablesets_DataExportTableParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtDataExportTableset{
   DataExportDef:Erp_Tablesets_DataExportDefRow[],
   DataExportHistory:Erp_Tablesets_DataExportHistoryRow[],
   DataExportOption:Erp_Tablesets_DataExportOptionRow[],
   DataExportTable:Erp_Tablesets_DataExportTableRow[],
   DataExportColumn:Erp_Tablesets_DataExportColumnRow[],
   DataExportColumnAttribute:Erp_Tablesets_DataExportColumnAttributeRow[],
   DataExportColumnLink:Erp_Tablesets_DataExportColumnLinkRow[],
   DataExportTableAttribute:Erp_Tablesets_DataExportTableAttributeRow[],
   DataExportTableParam:Erp_Tablesets_DataExportTableParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipDefinitionID
      @param ipExportFile
   */  
export interface ExportDefinition_input{
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  Export Filename, entered by user  */  
   ipExportFile:string,
}

export interface ExportDefinition_output{
parameters : {
      /**  output parameters  */  
   opExportFile:string,
}
}

   /** Required : 
      @param ipGDPdUMode
      @param ipDefinitionID
      @param ipTestMode
      @param ipDTDFile
      @param ds
   */  
export interface GenerateToServerFolder_input{
      /**  GDPdU Mode  */  
   ipGDPdUMode:boolean,
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  Test mode  */  
   ipTestMode:boolean,
      /**  Path to DTD file on server  */  
   ipDTDFile:string,
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface GenerateToServerFolder_output{
parameters : {
      /**  output parameters  */  
   opErrMessage:string,
   opFilesQty:number,
   opExportSubFolder:string,
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ipGDPdUMode
      @param ipDefinitionID
      @param ipTestMode
      @param ds
   */  
export interface Generate_input{
      /**  GDPdU Mode  */  
   ipGDPdUMode:boolean,
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  Test mode  */  
   ipTestMode:boolean,
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface Generate_output{
parameters : {
      /**  output parameters  */  
   opErrMessage:string,
   opFilesQty:number,
   opFilesForExport:string,
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param definitionID
   */  
export interface GetByID_input{
   definitionID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DataExportTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DataExportTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DataExportTableset[],
}

export interface GetDateFormats_output{
parameters : {
      /**  output parameters  */  
   opDateFormats:string,
}
}

   /** Required : 
      @param ipDefinitionID
      @param ipcurrentTable
      @param ipcurrentColumn
      @param ipDataType
   */  
export interface GetFieldList_input{
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  current Table  */  
   ipcurrentTable:string,
      /**  current Column  */  
   ipcurrentColumn:string,
      /**  column Type  */  
   ipDataType:string,
}

export interface GetFieldList_output{
parameters : {
      /**  output parameters  */  
   opFieldList:string,
}
}

   /** Required : 
      @param ipDefinitionID
      @param ipcurrentTable
   */  
export interface GetForeignTableList_input{
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  Current Table  */  
   ipcurrentTable:string,
}

export interface GetForeignTableList_output{
parameters : {
      /**  output parameters  */  
   opTableList:string,
}
}

   /** Required : 
      @param ipDefinitionID
      @param ipcurrentTable
      @param ipcurrentColumn
      @param ipcurrentForeignTblColumnName
   */  
export interface GetForeignTblFieldList_input{
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  current Table  */  
   ipcurrentTable:string,
      /**  current Column  */  
   ipcurrentColumn:string,
      /**  foreign Table column  */  
   ipcurrentForeignTblColumnName:string,
}

export interface GetForeignTblFieldList_output{
parameters : {
      /**  output parameters  */  
   opFieldList:string,
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
   returnObj:Erp_Tablesets_DataExportListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param definitionID
      @param tableName
      @param columnName
   */  
export interface GetNewDataExportColumnAttribute_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
   tableName:string,
   columnName:string,
}

export interface GetNewDataExportColumnAttribute_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param definitionID
      @param tableName
      @param columnName
   */  
export interface GetNewDataExportColumnLink_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
   tableName:string,
   columnName:string,
}

export interface GetNewDataExportColumnLink_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param definitionID
      @param tableName
   */  
export interface GetNewDataExportColumn_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
   tableName:string,
}

export interface GetNewDataExportColumn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDataExportDef_input{
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface GetNewDataExportDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param definitionID
   */  
export interface GetNewDataExportHistory_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
}

export interface GetNewDataExportHistory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param definitionID
      @param optionName
   */  
export interface GetNewDataExportOption_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
   optionName:string,
}

export interface GetNewDataExportOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param definitionID
      @param tableName
   */  
export interface GetNewDataExportTableAttribute_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
   tableName:string,
}

export interface GetNewDataExportTableAttribute_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param definitionID
      @param tableName
   */  
export interface GetNewDataExportTableParam_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
   tableName:string,
}

export interface GetNewDataExportTableParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param definitionID
   */  
export interface GetNewDataExportTable_input{
   ds:Erp_Tablesets_DataExportTableset[],
   definitionID:string,
}

export interface GetNewDataExportTable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ipDefinitionID
      @param ipcurrentTable
      @param ipcurrentColumn
      @param ipcurrentOwnColumn
   */  
export interface GetOwnTblFieldList_input{
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  current Table  */  
   ipcurrentTable:string,
      /**  current Column  */  
   ipcurrentColumn:string,
      /**  current Own Column  */  
   ipcurrentOwnColumn:string,
}

export interface GetOwnTblFieldList_output{
parameters : {
      /**  output parameters  */  
   opFieldList:string,
}
}

   /** Required : 
      @param whereClauseDataExportDef
      @param whereClauseDataExportHistory
      @param whereClauseDataExportOption
      @param whereClauseDataExportTable
      @param whereClauseDataExportColumn
      @param whereClauseDataExportColumnAttribute
      @param whereClauseDataExportColumnLink
      @param whereClauseDataExportTableAttribute
      @param whereClauseDataExportTableParam
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDataExportDef:string,
   whereClauseDataExportHistory:string,
   whereClauseDataExportOption:string,
   whereClauseDataExportTable:string,
   whereClauseDataExportColumn:string,
   whereClauseDataExportColumnAttribute:string,
   whereClauseDataExportColumnLink:string,
   whereClauseDataExportTableAttribute:string,
   whereClauseDataExportTableParam:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DataExportTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipDefinitionID
      @param ipcurrentTable
      @param ipcurrentColumn
      @param ipDataType
   */  
export interface GetTableList_input{
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  Current Table  */  
   ipcurrentTable:string,
      /**  Current Column  */  
   ipcurrentColumn:string,
      /**  Column Type  */  
   ipDataType:string,
}

export interface GetTableList_output{
parameters : {
      /**  output parameters  */  
   opTableList:string,
}
}

   /** Required : 
      @param ipDefinitionID
   */  
export interface GetTablesListWithWrongSource_input{
      /**  Definition  */  
   ipDefinitionID:string,
}

export interface GetTablesListWithWrongSource_output{
parameters : {
      /**  output parameters  */  
   opTablesList:string,
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
      @param ipGDPdUMode
      @param ipImportFile
      @param ipNewDefinitionID
      @param ipCheckDefinitionExistance
   */  
export interface ImportDefinition_input{
      /**  GDPdU Mode  */  
   ipGDPdUMode:boolean,
      /**  Data Definition template file  */  
   ipImportFile:string,
      /**  New Definition ID, entered by user  */  
   ipNewDefinitionID:string,
      /**  Check whether new definition id alredy exists in db  */  
   ipCheckDefinitionExistance:boolean,
}

export interface ImportDefinition_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opNewDefinitionID:string,
}
}

   /** Required : 
      @param ipGLBook
      @param ipFiscalYear
      @param ipStartPeriod
      @param ipEndPeriod
   */  
export interface IsPostingsExist_input{
      /**  Fiscal Year  */  
   ipGLBook:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Start period  */  
   ipStartPeriod:number,
      /**  End period  */  
   ipEndPeriod:number,
}

export interface IsPostingsExist_output{
parameters : {
      /**  output parameters  */  
   opResult:boolean,
}
}

   /** Required : 
      @param ipGLBook
      @param ipFiscalYear
      @param ipStartPeriod
      @param ipEndPeriod
      @param ds
   */  
export interface OnChangeGLBook_input{
      /**  Fiscal Year  */  
   ipGLBook:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Start period  */  
   ipStartPeriod:number,
      /**  End period  */  
   ipEndPeriod:number,
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface OnChangeGLBook_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ipDefinitionID
      @param ipGenMethod
      @param ipTableName
      @param ipDataSourceID
      @param ds
   */  
export interface OnRetrieveColumns_input{
      /**  Definition ID  */  
   ipDefinitionID:string,
      /**  Generation method  */  
   ipGenMethod:string,
      /**  Table Name  */  
   ipTableName:string,
      /**  Data Source ID  */  
   ipDataSourceID:string,
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface OnRetrieveColumns_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RefreshDataExportDef_input{
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface RefreshDataExportDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface SetGDPdUMode_input{
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface SetGDPdUMode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ipDefinitionID
      @param ds
   */  
export interface StoreData_input{
   ipDefinitionID:string,
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface StoreData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDataExportTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDataExportTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DataExportTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataExportTableset[],
}
}

