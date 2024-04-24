import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DataCheckSvc
// Description: Data Health check server
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/$metadata", {
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
   Description: Get DataChecks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataChecks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckRow
   */  
export function get_DataChecks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataChecks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataCheck item
   Description: Calls GetByID to retrieve the DataCheck item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheck
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckRow
   */  
export function get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataCheckRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataCheckRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataCheck for the service
   Description: Calls UpdateExt to update DataCheck. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheck
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Summary: Call UpdateExt to delete DataCheck item
   Description: Call UpdateExt to delete DataCheck item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheck
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Description: Get DataCheckDDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataCheckDDefs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckDDefRow
   */  
export function get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckDDefs(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckDDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataCheckDDef item
   Description: Calls GetByID to retrieve the DataCheckDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckDDef1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   */  
export function get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataCheckDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataCheckDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataCheckParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataCheckParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckParamRow
   */  
export function get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckParams(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataCheckParam item
   Description: Calls GetByID to retrieve the DataCheckParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   */  
export function get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataCheckParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataCheckParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataCheckRpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataCheckRpts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckRptRow
   */  
export function get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckRpts(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckRpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataCheckRpt item
   Description: Calls GetByID to retrieve the DataCheckRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckRpt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   */  
export function get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataCheckRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataCheckRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DataCheckDDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataCheckDDefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckDDefRow
   */  
export function get_DataCheckDDefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataCheckDDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataCheckDDefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataCheckDDef item
   Description: Calls GetByID to retrieve the DataCheckDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckDDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   */  
export function get_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataCheckDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataCheckDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataCheckDDef for the service
   Description: Calls UpdateExt to update DataCheckDDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheckDDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
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
   Summary: Call UpdateExt to delete DataCheckDDef item
   Description: Call UpdateExt to delete DataCheckDDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheckDDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
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
   Description: Get DataCheckParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataCheckParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckParamRow
   */  
export function get_DataCheckParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataCheckParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataCheckParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataCheckParam item
   Description: Calls GetByID to retrieve the DataCheckParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   */  
export function get_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataCheckParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataCheckParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataCheckParam for the service
   Description: Calls UpdateExt to update DataCheckParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheckParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Summary: Call UpdateExt to delete DataCheckParam item
   Description: Call UpdateExt to delete DataCheckParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheckParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Description: Get DataCheckRpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataCheckRpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckRptRow
   */  
export function get_DataCheckRpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataCheckRpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataCheckRpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataCheckRpt item
   Description: Calls GetByID to retrieve the DataCheckRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckRpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   */  
export function get_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataCheckRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataCheckRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataCheckRpt for the service
   Description: Calls UpdateExt to update DataCheckRpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheckRpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
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
   Summary: Call UpdateExt to delete DataCheckRpt item
   Description: Call UpdateExt to delete DataCheckRpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheckRpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataChecklistRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataChecklistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataChecklistRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDataCheck:string, whereClauseDataCheckDDef:string, whereClauseDataCheckParam:string, whereClauseDataCheckRpt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDataCheck!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataCheck=" + whereClauseDataCheck
   }
   if(typeof whereClauseDataCheckDDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataCheckDDef=" + whereClauseDataCheckDDef
   }
   if(typeof whereClauseDataCheckParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataCheckParam=" + whereClauseDataCheckParam
   }
   if(typeof whereClauseDataCheckRpt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataCheckRpt=" + whereClauseDataCheckRpt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetRows" + params, {
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
export function get_GetByID(company:string, localName:string, key1:string, key2:string, key3:string, key4:string, key5:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof localName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "localName=" + localName
   }
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }
   if(typeof key4!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key4=" + key4
   }
   if(typeof key5!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key5=" + key5
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsCustom
   Description: Retrieve DataCheck rows from Local001 table and populate temp tables
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetRowsCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDCustom
   Description: Get DataCheck data for given DataCheckId
   OperationID: GetByIDCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetByIDCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StartCheck
   Description: Start Check
   OperationID: StartCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/StartCheck", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateCheck
   Description: Update Check
   OperationID: UpdateCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/UpdateCheck", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelCheck
   Description: Cancel Check
   OperationID: CancelCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/CancelCheck", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrentInstallation
   Description: Get the current tenant and installation ids
   OperationID: GetCurrentInstallation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentInstallation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentInstallation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentInstallation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetCurrentInstallation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTenants
   Description: Get all the tenants and installation ids
   OperationID: GetTenants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTenants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTenants_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTenants(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetTenants", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectAll
   Description: Select all the current report records
   OperationID: SelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/SelectAll", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnSelectAll
   Description: UnSelect all the current report records
   OperationID: UnSelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnSelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnSelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnSelectAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/UnSelectAll", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateParameterComponents
   Description: Generate the necessary components to fill parameters from ds.
   OperationID: GenerateParameterComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateParameterComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateParameterComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateParameterComponents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GenerateParameterComponents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompanies
   Description: Get the companies available.
   OperationID: GetCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompanies(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetCompanies", {
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
   Summary: Invoke method GetNewDataCheck
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDataCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetNewDataCheck", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckDDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataCheckDDefRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataCheckParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataCheckRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataCheckRptRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataChecklistRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataChecklistRow[],
}

export interface Erp_Tablesets_DataCheckDDefRow{
   "Company":string,
   "LocalName":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "seqnum":number,
   "DataCheckddefid":string,
   "tblname":string,
   "colname":string,
   "width":number,
   "datatype":string,
   "tabseq":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataCheckParamRow{
   "Company":string,
   "LocalName":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "Label01":string,
   "Value01":string,
   "BlankOK01":boolean,
   "DataType01":string,
   "ViewType01":string,
   "Label02":string,
   "Value02":string,
   "BlankOK02":boolean,
   "DataType02":string,
   "ViewType02":string,
   "Label03":string,
   "Value03":string,
   "BlankOK03":boolean,
   "DataType03":string,
   "ViewType03":string,
   "Label04":string,
   "Value04":string,
   "BlankOK04":boolean,
   "DataType04":string,
   "ViewType04":string,
   "Label05":string,
   "Value05":string,
   "BlankOK05":boolean,
   "DataType05":string,
   "ViewType05":string,
   "Label06":string,
   "Value06":string,
   "BlankOK06":boolean,
   "DataType06":string,
   "ViewType06":string,
   "Label07":string,
   "Value07":string,
   "BlankOK07":boolean,
   "DataType07":string,
   "ViewType07":string,
   "Label08":string,
   "Value08":string,
   "BlankOK08":boolean,
   "DataType08":string,
   "ViewType08":string,
   "Label09":string,
   "Value09":string,
   "BlankOK09":boolean,
   "DataType09":string,
   "ViewType09":string,
   "Label10":string,
   "Value10":string,
   "BlankOK10":boolean,
   "DataType10":string,
   "ViewType10":string,
   "Label11":string,
   "Value11":string,
   "BlankOK11":boolean,
   "DataType11":string,
   "ViewType11":string,
   "Label12":string,
   "Value12":string,
   "BlankOK12":boolean,
   "DataType12":string,
   "ViewType12":string,
   "Label13":string,
   "Value13":string,
   "BlankOK13":boolean,
   "DataType13":string,
   "ViewType13":string,
   "Label14":string,
   "Value14":string,
   "BlankOK14":boolean,
   "DataType14":string,
   "ViewType14":string,
   "Label15":string,
   "Value15":string,
   "BlankOK15":boolean,
   "DataType15":string,
   "ViewType15":string,
   "Label16":string,
   "Value16":string,
   "BlankOK16":boolean,
   "DataType16":string,
   "ViewType16":string,
   "Label17":string,
   "Value17":string,
   "BlankOK17":boolean,
   "DataType17":string,
   "ViewType17":string,
   "Label18":string,
   "Value18":string,
   "BlankOK18":boolean,
   "DataType18":string,
   "ViewType18":string,
   "Label19":string,
   "Value19":string,
   "BlankOK19":boolean,
   "DataType19":string,
   "ViewType19":string,
   "Label20":string,
   "Value20":string,
   "BlankOK20":boolean,
   "DataType20":string,
   "ViewType20":string,
   "BlankCompOK":boolean,
   "LabelComp":string,
   "ViewTypeComp":string,
   "ValueComp":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataCheckRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Available":boolean,
   "AvailDesc":string,
   "ExpiresInd":boolean,
   "Generic":boolean,
   "NotGeneric":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataCheckRptRow{
   "Company":string,
   "LocalName":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "UpdInd":boolean,
   "UpdTable":string,
   "value01":string,
   "value02":string,
   "value03":string,
   "value04":string,
   "value05":string,
   "value06":string,
   "value07":string,
   "value08":string,
   "value09":string,
   "value10":string,
   "value11":string,
   "value12":string,
   "value13":string,
   "value14":string,
   "value15":string,
   "value16":string,
   "value17":string,
   "value18":string,
   "value19":string,
   "value20":string,
   "value21":string,
   "value22":string,
   "value23":string,
   "value24":string,
   "value25":string,
   "value26":string,
   "value27":string,
   "value28":string,
   "value29":string,
   "value30":string,
   "value31":string,
   "value32":string,
   "value33":string,
   "value34":string,
   "value35":string,
   "value36":string,
   "value37":string,
   "value38":string,
   "value39":string,
   "value40":string,
   "value41":string,
   "value42":string,
   "value43":string,
   "value44":string,
   "value45":string,
   "value46":string,
   "value47":string,
   "value48":string,
   "value49":string,
   "value50":string,
   "value51":string,
   "value52":string,
   "value53":string,
   "value54":string,
   "value55":string,
   "value56":string,
   "value57":string,
   "value58":string,
   "value59":string,
   "value60":string,
   "value61":string,
   "value62":string,
   "value63":string,
   "value64":string,
   "value65":string,
   "value66":string,
   "value67":string,
   "value68":string,
   "value69":string,
   "value70":string,
   "value71":string,
   "value72":string,
   "value73":string,
   "value74":string,
   "value75":string,
   "value76":string,
   "value77":string,
   "value78":string,
   "value79":string,
   "value80":string,
   "value81":string,
   "value82":string,
   "value83":string,
   "value84":string,
   "value85":string,
   "value86":string,
   "value87":string,
   "value88":string,
   "value89":string,
   "value90":string,
   "value91":string,
   "value92":string,
   "value93":string,
   "value94":string,
   "value95":string,
   "value96":string,
   "value97":string,
   "value98":string,
   "value99":string,
   "seqId":number,
      /**  name of tab control record is displayed on  */  
   "tblname":string,
   "UpdXml":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataChecklistRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param SysRowId
      @param DataCheckId
      @param DataCheckSPName
      @param PageSize
      @param ds
   */  
export interface CancelCheck_input{
      /**  SysRowId of Data Fix record  */  
   SysRowId:string,
      /**  Data Check ID  */  
   DataCheckId:string,
      /**  Data Check Stored Procedure  */  
   DataCheckSPName:string,
      /**  Number of report records to return  */  
   PageSize:number,
   ds:Erp_Tablesets_DataCheckTableset[],
}

export interface CancelCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataCheckTableset[],
}
}

   /** Required : 
      @param company
      @param localName
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
   */  
export interface DeleteByID_input{
   company:string,
   localName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DataCheckDDefRow{
   Company:string,
   LocalName:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   seqnum:number,
   DataCheckddefid:string,
   tblname:string,
   colname:string,
   width:number,
   datatype:string,
   tabseq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataCheckListTableset{
   DataChecklist:Erp_Tablesets_DataChecklistRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DataCheckParamRow{
   Company:string,
   LocalName:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   Label01:string,
   Value01:string,
   BlankOK01:boolean,
   DataType01:string,
   ViewType01:string,
   Label02:string,
   Value02:string,
   BlankOK02:boolean,
   DataType02:string,
   ViewType02:string,
   Label03:string,
   Value03:string,
   BlankOK03:boolean,
   DataType03:string,
   ViewType03:string,
   Label04:string,
   Value04:string,
   BlankOK04:boolean,
   DataType04:string,
   ViewType04:string,
   Label05:string,
   Value05:string,
   BlankOK05:boolean,
   DataType05:string,
   ViewType05:string,
   Label06:string,
   Value06:string,
   BlankOK06:boolean,
   DataType06:string,
   ViewType06:string,
   Label07:string,
   Value07:string,
   BlankOK07:boolean,
   DataType07:string,
   ViewType07:string,
   Label08:string,
   Value08:string,
   BlankOK08:boolean,
   DataType08:string,
   ViewType08:string,
   Label09:string,
   Value09:string,
   BlankOK09:boolean,
   DataType09:string,
   ViewType09:string,
   Label10:string,
   Value10:string,
   BlankOK10:boolean,
   DataType10:string,
   ViewType10:string,
   Label11:string,
   Value11:string,
   BlankOK11:boolean,
   DataType11:string,
   ViewType11:string,
   Label12:string,
   Value12:string,
   BlankOK12:boolean,
   DataType12:string,
   ViewType12:string,
   Label13:string,
   Value13:string,
   BlankOK13:boolean,
   DataType13:string,
   ViewType13:string,
   Label14:string,
   Value14:string,
   BlankOK14:boolean,
   DataType14:string,
   ViewType14:string,
   Label15:string,
   Value15:string,
   BlankOK15:boolean,
   DataType15:string,
   ViewType15:string,
   Label16:string,
   Value16:string,
   BlankOK16:boolean,
   DataType16:string,
   ViewType16:string,
   Label17:string,
   Value17:string,
   BlankOK17:boolean,
   DataType17:string,
   ViewType17:string,
   Label18:string,
   Value18:string,
   BlankOK18:boolean,
   DataType18:string,
   ViewType18:string,
   Label19:string,
   Value19:string,
   BlankOK19:boolean,
   DataType19:string,
   ViewType19:string,
   Label20:string,
   Value20:string,
   BlankOK20:boolean,
   DataType20:string,
   ViewType20:string,
   BlankCompOK:boolean,
   LabelComp:string,
   ViewTypeComp:string,
   ValueComp:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataCheckRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Available:boolean,
   AvailDesc:string,
   ExpiresInd:boolean,
   Generic:boolean,
   NotGeneric:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataCheckRptRow{
   Company:string,
   LocalName:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   UpdInd:boolean,
   UpdTable:string,
   value01:string,
   value02:string,
   value03:string,
   value04:string,
   value05:string,
   value06:string,
   value07:string,
   value08:string,
   value09:string,
   value10:string,
   value11:string,
   value12:string,
   value13:string,
   value14:string,
   value15:string,
   value16:string,
   value17:string,
   value18:string,
   value19:string,
   value20:string,
   value21:string,
   value22:string,
   value23:string,
   value24:string,
   value25:string,
   value26:string,
   value27:string,
   value28:string,
   value29:string,
   value30:string,
   value31:string,
   value32:string,
   value33:string,
   value34:string,
   value35:string,
   value36:string,
   value37:string,
   value38:string,
   value39:string,
   value40:string,
   value41:string,
   value42:string,
   value43:string,
   value44:string,
   value45:string,
   value46:string,
   value47:string,
   value48:string,
   value49:string,
   value50:string,
   value51:string,
   value52:string,
   value53:string,
   value54:string,
   value55:string,
   value56:string,
   value57:string,
   value58:string,
   value59:string,
   value60:string,
   value61:string,
   value62:string,
   value63:string,
   value64:string,
   value65:string,
   value66:string,
   value67:string,
   value68:string,
   value69:string,
   value70:string,
   value71:string,
   value72:string,
   value73:string,
   value74:string,
   value75:string,
   value76:string,
   value77:string,
   value78:string,
   value79:string,
   value80:string,
   value81:string,
   value82:string,
   value83:string,
   value84:string,
   value85:string,
   value86:string,
   value87:string,
   value88:string,
   value89:string,
   value90:string,
   value91:string,
   value92:string,
   value93:string,
   value94:string,
   value95:string,
   value96:string,
   value97:string,
   value98:string,
   value99:string,
   seqId:number,
      /**  name of tab control record is displayed on  */  
   tblname:string,
   UpdXml:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataCheckTableset{
   DataCheck:Erp_Tablesets_DataCheckRow[],
   DataCheckDDef:Erp_Tablesets_DataCheckDDefRow[],
   DataCheckParam:Erp_Tablesets_DataCheckParamRow[],
   DataCheckRpt:Erp_Tablesets_DataCheckRptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DataChecklistRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtDataCheckTableset{
   DataCheck:Erp_Tablesets_DataCheckRow[],
   DataCheckDDef:Erp_Tablesets_DataCheckDDefRow[],
   DataCheckParam:Erp_Tablesets_DataCheckParamRow[],
   DataCheckRpt:Erp_Tablesets_DataCheckRptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateParameterComponents_input{
   ds:Erp_Tablesets_DataCheckTableset[],
}

export interface GenerateParameterComponents_output{
   returnObj:string,
}

   /** Required : 
      @param DataCheckId
      @param PageSize
   */  
export interface GetByIDCustom_input{
      /**  The Data Fix Id  */  
   DataCheckId:string,
      /**  number of report records to return  */  
   PageSize:number,
}

export interface GetByIDCustom_output{
   returnObj:Erp_Tablesets_DataCheckTableset[],
}

   /** Required : 
      @param company
      @param localName
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
   */  
export interface GetByID_input{
   company:string,
   localName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DataCheckTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DataCheckTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DataCheckTableset[],
}

export interface GetCompanies_output{
parameters : {
      /**  output parameters  */  
   companies:string,
}
}

   /** Required : 
      @param TenantID
      @param InstallationID
   */  
export interface GetCurrentInstallation_input{
      /**  Tenant Id  */  
   TenantID:string,
      /**  Installation ID  */  
   InstallationID:string,
}

export interface GetCurrentInstallation_output{
parameters : {
      /**  output parameters  */  
   TenantID:string,
   InstallationID:string,
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
   returnObj:Erp_Tablesets_DataCheckListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param localName
      @param key1
      @param key2
      @param key3
      @param key4
   */  
export interface GetNewDataCheck_input{
   ds:Erp_Tablesets_DataCheckTableset[],
   company:string,
   localName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
}

export interface GetNewDataCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataCheckTableset[],
}
}

   /** Required : 
      @param dataCheckWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  where clause for data fixes  */  
   dataCheckWhereClause:string,
      /**  pagesize  */  
   pageSize:number,
      /**  Absolute page size  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_DataCheckTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseDataCheck
      @param whereClauseDataCheckDDef
      @param whereClauseDataCheckParam
      @param whereClauseDataCheckRpt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDataCheck:string,
   whereClauseDataCheckDDef:string,
   whereClauseDataCheckParam:string,
   whereClauseDataCheckRpt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DataCheckTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param Tenants
      @param InstallationIDs
   */  
export interface GetTenants_input{
      /**  Tenants  */  
   Tenants:string,
      /**  Installation IDs  */  
   InstallationIDs:string,
}

export interface GetTenants_output{
parameters : {
      /**  output parameters  */  
   Tenants:string,
   InstallationIDs:string,
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
      @param DataCheckId
      @param ds
   */  
export interface SelectAll_input{
      /**  Data Fix Id  */  
   DataCheckId:string,
   ds:Erp_Tablesets_DataCheckTableset[],
}

export interface SelectAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataCheckTableset[],
}
}

   /** Required : 
      @param SysRowId
      @param DataCheckId
      @param DataCheckSPName
      @param InstallationID
      @param PageSize
      @param agentID
      @param ds
   */  
export interface StartCheck_input{
      /**  SysRowId of Data Fix record  */  
   SysRowId:string,
      /**  Data Check ID  */  
   DataCheckId:string,
      /**  Data Check Stored Procedure  */  
   DataCheckSPName:string,
      /**  Installation ID of tenant  */  
   InstallationID:string,
      /**  Number of Records to return  */  
   PageSize:number,
      /**  Task Agent  */  
   agentID:string,
   ds:Erp_Tablesets_DataCheckTableset[],
}

export interface StartCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataCheckTableset[],
}
}

   /** Required : 
      @param DataCheckId
      @param ds
   */  
export interface UnSelectAll_input{
      /**  Data Fix Id  */  
   DataCheckId:string,
   ds:Erp_Tablesets_DataCheckTableset[],
}

export interface UnSelectAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataCheckTableset[],
}
}

   /** Required : 
      @param SysRowId
      @param DataCheckId
      @param DataCheckSPName
      @param PageSize
      @param ds
   */  
export interface UpdateCheck_input{
      /**  SysRowId of Data Fix record  */  
   SysRowId:string,
      /**  Data Check ID  */  
   DataCheckId:string,
      /**  Data Check Stored Procedure  */  
   DataCheckSPName:string,
      /**  Number of Records to return  */  
   PageSize:number,
   ds:Erp_Tablesets_DataCheckTableset[],
}

export interface UpdateCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataCheckTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDataCheckTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDataCheckTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DataCheckTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataCheckTableset[],
}
}

