import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ExtPRLayoutSvc
// Description: ExtPRLayoutSvc class
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/$metadata", {
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
   Description: Get ExtPRLayouts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRLayouts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportLayoutRow
   */  
export function get_ExtPRLayouts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtPRLayouts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtPRLayout item
   Description: Calls GetByID to retrieve the ExtPRLayout item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRLayout
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
   */  
export function get_ExtPRLayouts_Company_PayExportLayoutID(Company:string, PayExportLayoutID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtPRExportLayoutRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtPRExportLayoutRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtPRLayout for the service
   Description: Calls UpdateExt to update ExtPRLayout. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRLayout
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRExportLayoutRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtPRLayouts_Company_PayExportLayoutID(Company:string, PayExportLayoutID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")", {
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
   Summary: Call UpdateExt to delete ExtPRLayout item
   Description: Call UpdateExt to delete ExtPRLayout item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRLayout
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtPRLayouts_Company_PayExportLayoutID(Company:string, PayExportLayoutID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")", {
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
   Description: Get ExtPRExportSeqs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPRExportSeqs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportSeqRow
   */  
export function get_ExtPRLayouts_Company_PayExportLayoutID_ExtPRExportSeqs(Company:string, PayExportLayoutID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")/ExtPRExportSeqs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtPRExportSeq item
   Description: Calls GetByID to retrieve the ExtPRExportSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRExportSeq1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   */  
export function get_ExtPRLayouts_Company_PayExportLayoutID_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company:string, PayExportLayoutID:string, SchemaName:string, TableName:string, ColumnName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtPRExportSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRLayouts(" + Company + "," + PayExportLayoutID + ")/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtPRExportSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ExtPRExportSeqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRExportSeqs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportSeqRow
   */  
export function get_ExtPRExportSeqs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRExportSeqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtPRExportSeqs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtPRExportSeq item
   Description: Calls GetByID to retrieve the ExtPRExportSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRExportSeq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   */  
export function get_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company:string, PayExportLayoutID:string, SchemaName:string, TableName:string, ColumnName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtPRExportSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtPRExportSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtPRExportSeq for the service
   Description: Calls UpdateExt to update ExtPRExportSeq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRExportSeq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRExportSeqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company:string, PayExportLayoutID:string, SchemaName:string, TableName:string, ColumnName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")", {
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
   Summary: Call UpdateExt to delete ExtPRExportSeq item
   Description: Call UpdateExt to delete ExtPRExportSeq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRExportSeq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PayExportLayoutID Desc: PayExportLayoutID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param ColumnName Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtPRExportSeqs_Company_PayExportLayoutID_SchemaName_TableName_ColumnName(Company:string, PayExportLayoutID:string, SchemaName:string, TableName:string, ColumnName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/ExtPRExportSeqs(" + Company + "," + PayExportLayoutID + "," + SchemaName + "," + TableName + "," + ColumnName + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRExportLayoutListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutListRow)
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
export function get_GetRows(whereClauseExtPRExportLayout:string, whereClauseExtPRExportSeq:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseExtPRExportLayout!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtPRExportLayout=" + whereClauseExtPRExportLayout
   }
   if(typeof whereClauseExtPRExportSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtPRExportSeq=" + whereClauseExtPRExportSeq
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetRows" + params, {
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
export function get_GetByID(payExportLayoutID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof payExportLayoutID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "payExportLayoutID=" + payExportLayoutID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetList" + params, {
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
   Summary: Invoke method MoveOnePosition
   Description: This method moves the layout field sequences Up/Down one position in the  grid and returns the whole updated data table.
   OperationID: MoveOnePosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveOnePosition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/MoveOnePosition", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getSourceTables
   Description: This method is used to fill the source table combo since this table doesn't have its own BO.
   OperationID: getSourceTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/getSourceTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getSourceTables(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/getSourceTables", {
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
   Summary: Invoke method getSourceFields
   Description: This method is used to fill the source field combo since this table doesn't have its own BO.
   OperationID: getSourceFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getSourceFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getSourceFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getSourceFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/getSourceFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method changeColumnName
   Description: Call this method to get the column description (Link Field)
   OperationID: changeColumnName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/changeColumnName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/changeColumnName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_changeColumnName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/changeColumnName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method changeLayoutDescription
   Description: Call this method to validate if the description already exists.
   OperationID: changeLayoutDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/changeLayoutDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/changeLayoutDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_changeLayoutDescription(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/changeLayoutDescription", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LayoutIDExists
   Description: This method is called to check if a  Layout id exists
   OperationID: LayoutIDExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LayoutIDExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LayoutIDExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LayoutIDExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/LayoutIDExists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPredefinedLayout
   Description: Creates and returns the External Layout Tableset using the default ADP layout.
   OperationID: GetPredefinedLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPredefinedLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPredefinedLayout(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetPredefinedLayout", {
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
   Summary: Invoke method UpdateExportLayoutFieldParent
   Description: Update Parent ID for ExtPRExportSeq during parent creation for new ADP layouts.
   OperationID: UpdateExportLayoutFieldParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExportLayoutFieldParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExportLayoutFieldParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExportLayoutFieldParent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/UpdateExportLayoutFieldParent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtPRExportLayout
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRExportLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRExportLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRExportLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtPRExportLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetNewExtPRExportLayout", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtPRExportSeq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRExportSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRExportSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRExportSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtPRExportSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetNewExtPRExportSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRLayoutSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtPRExportLayoutListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportLayoutRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtPRExportLayoutRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRExportSeqRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtPRExportSeqRow[],
}

export interface Erp_Tablesets_ExtPRExportLayoutListRow{
      /**  Company  */  
   "Company":string,
      /**  Payroll layout ID  */  
   "PayExportLayoutID":string,
      /**  Payroll layout description  */  
   "Description":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtPRExportLayoutRow{
      /**  Company  */  
   "Company":string,
      /**  Payroll layout ID  */  
   "PayExportLayoutID":string,
      /**  Payroll layout description  */  
   "Description":string,
      /**  Short Character #1  */  
   "ShortChar01":string,
      /**  Short Character #2  */  
   "ShortChar02":string,
      /**  Short Character #3  */  
   "ShortChar03":string,
      /**  Short Character #4  */  
   "ShortChar04":string,
      /**  Short Character #5  */  
   "ShortChar05":string,
      /**  Long Character #1  */  
   "Character01":string,
      /**  Long Character #2  */  
   "Character02":string,
      /**  Long Character #3  */  
   "Character03":string,
      /**  Long Character #4  */  
   "Character04":string,
      /**  Long Character #5  */  
   "Character05":string,
      /**  Numeric #1  */  
   "Number01":number,
      /**  Numeric #2  */  
   "Number02":number,
      /**  Numeric #3  */  
   "Number03":number,
      /**  Numeric #4  */  
   "Number04":number,
      /**  Numeric #5  */  
   "Number05":number,
      /**  Integer #1  */  
   "Number06":number,
      /**  Integer #2  */  
   "Number07":number,
      /**  Integer #3  */  
   "Number08":number,
      /**  Integer #4  */  
   "Number09":number,
      /**  Integer #5  */  
   "Number10":number,
      /**  Date #1  */  
   "Date01":string,
      /**  Date #2  */  
   "Date02":string,
      /**  Date #3  */  
   "Date03":string,
      /**  Boolean #1  */  
   "Checkbox01":boolean,
      /**  Boolean #2  */  
   "Checkbox02":boolean,
      /**  Boolean #3  */  
   "Checkbox03":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtPRExportSeqRow{
      /**  Company  */  
   "Company":string,
      /**  Payroll Layout ID  */  
   "PayExportLayoutID":string,
      /**  Epicor Source Schema  */  
   "SchemaName":string,
      /**  Epicor Source Table  */  
   "TableName":string,
      /**  Epicor Source Column  */  
   "ColumnName":string,
      /**  Order of the fields to be exported  */  
   "Seq":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ColumnTitle  */  
   "ColumnTitle":string,
      /**  Column Description  */  
   "Description":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param payExportLayoutID
   */  
export interface DeleteByID_input{
   payExportLayoutID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ExtPRExportLayoutListRow{
      /**  Company  */  
   Company:string,
      /**  Payroll layout ID  */  
   PayExportLayoutID:string,
      /**  Payroll layout description  */  
   Description:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtPRExportLayoutListTableset{
   ExtPRExportLayoutList:Erp_Tablesets_ExtPRExportLayoutListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ExtPRExportLayoutRow{
      /**  Company  */  
   Company:string,
      /**  Payroll layout ID  */  
   PayExportLayoutID:string,
      /**  Payroll layout description  */  
   Description:string,
      /**  Short Character #1  */  
   ShortChar01:string,
      /**  Short Character #2  */  
   ShortChar02:string,
      /**  Short Character #3  */  
   ShortChar03:string,
      /**  Short Character #4  */  
   ShortChar04:string,
      /**  Short Character #5  */  
   ShortChar05:string,
      /**  Long Character #1  */  
   Character01:string,
      /**  Long Character #2  */  
   Character02:string,
      /**  Long Character #3  */  
   Character03:string,
      /**  Long Character #4  */  
   Character04:string,
      /**  Long Character #5  */  
   Character05:string,
      /**  Numeric #1  */  
   Number01:number,
      /**  Numeric #2  */  
   Number02:number,
      /**  Numeric #3  */  
   Number03:number,
      /**  Numeric #4  */  
   Number04:number,
      /**  Numeric #5  */  
   Number05:number,
      /**  Integer #1  */  
   Number06:number,
      /**  Integer #2  */  
   Number07:number,
      /**  Integer #3  */  
   Number08:number,
      /**  Integer #4  */  
   Number09:number,
      /**  Integer #5  */  
   Number10:number,
      /**  Date #1  */  
   Date01:string,
      /**  Date #2  */  
   Date02:string,
      /**  Date #3  */  
   Date03:string,
      /**  Boolean #1  */  
   Checkbox01:boolean,
      /**  Boolean #2  */  
   Checkbox02:boolean,
      /**  Boolean #3  */  
   Checkbox03:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtPRExportSeqRow{
      /**  Company  */  
   Company:string,
      /**  Payroll Layout ID  */  
   PayExportLayoutID:string,
      /**  Epicor Source Schema  */  
   SchemaName:string,
      /**  Epicor Source Table  */  
   TableName:string,
      /**  Epicor Source Column  */  
   ColumnName:string,
      /**  Order of the fields to be exported  */  
   Seq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ColumnTitle  */  
   ColumnTitle:string,
      /**  Column Description  */  
   Description:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtPRExportSrcFldRow{
      /**  Company  */  
   Company:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  TableName  */  
   TableName:string,
      /**  ColumnName  */  
   ColumnName:string,
      /**  Description  */  
   Description:string,
      /**  Comment  */  
   Comment:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtPRExportSrcFldTableset{
   ExtPRExportSrcFld:Erp_Tablesets_ExtPRExportSrcFldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ExtPRExportSrcTblRow{
      /**  Company  */  
   Company:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  TableName  */  
   TableName:string,
      /**  Description  */  
   Description:string,
      /**  Comment  */  
   Comment:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtPRExportSrcTblTableset{
   ExtPRExportSrcTbl:Erp_Tablesets_ExtPRExportSrcTblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ExtPRLayoutTableset{
   ExtPRExportLayout:Erp_Tablesets_ExtPRExportLayoutRow[],
   ExtPRExportSeq:Erp_Tablesets_ExtPRExportSeqRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtExtPRLayoutTableset{
   ExtPRExportLayout:Erp_Tablesets_ExtPRExportLayoutRow[],
   ExtPRExportSeq:Erp_Tablesets_ExtPRExportSeqRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param payExportLayoutID
   */  
export interface GetByID_input{
   payExportLayoutID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ExtPRLayoutTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ExtPRLayoutTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ExtPRLayoutTableset[],
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
   returnObj:Erp_Tablesets_ExtPRExportLayoutListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewExtPRExportLayout_input{
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}

export interface GetNewExtPRExportLayout_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}
}

   /** Required : 
      @param ds
      @param payExportLayoutID
      @param schemaName
      @param tableName
   */  
export interface GetNewExtPRExportSeq_input{
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
   payExportLayoutID:string,
   schemaName:string,
   tableName:string,
}

export interface GetNewExtPRExportSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}
}

export interface GetPredefinedLayout_output{
   returnObj:Erp_Tablesets_ExtPRLayoutTableset[],
}

   /** Required : 
      @param whereClauseExtPRExportLayout
      @param whereClauseExtPRExportSeq
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseExtPRExportLayout:string,
   whereClauseExtPRExportSeq:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ExtPRLayoutTableset[],
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
      @param layoutID
   */  
export interface LayoutIDExists_input{
   layoutID:string,
}

export interface LayoutIDExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param layoutID
      @param schemaName
      @param tableName
      @param columnName
      @param displayOrder
      @param moveDir
   */  
export interface MoveOnePosition_input{
   layoutID:string,
   schemaName:string,
   tableName:string,
   columnName:string,
   displayOrder:number,
   moveDir:string,
}

export interface MoveOnePosition_output{
   returnObj:Erp_Tablesets_ExtPRLayoutTableset[],
}

   /** Required : 
      @param payExportLayoutID
      @param ds
   */  
export interface UpdateExportLayoutFieldParent_input{
   payExportLayoutID:string,
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}

export interface UpdateExportLayoutFieldParent_output{
   returnObj:Erp_Tablesets_ExtPRLayoutTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtExtPRLayoutTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtExtPRLayoutTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}
}

   /** Required : 
      @param proposedColumnName
      @param ds
   */  
export interface changeColumnName_input{
   proposedColumnName:string,
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}

export interface changeColumnName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}
}

   /** Required : 
      @param proposedDescription
      @param ds
   */  
export interface changeLayoutDescription_input{
   proposedDescription:string,
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}

export interface changeLayoutDescription_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtPRLayoutTableset[],
}
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface getSourceFields_input{
   schemaName:string,
   tableName:string,
}

export interface getSourceFields_output{
   returnObj:Erp_Tablesets_ExtPRExportSrcFldTableset[],
}

export interface getSourceTables_output{
   returnObj:Erp_Tablesets_ExtPRExportSrcTblTableset[],
}

