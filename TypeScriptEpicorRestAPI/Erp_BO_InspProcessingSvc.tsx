import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.InspProcessingSvc
// Description: This object supports the following activities:
- Viewing NonConformances from various sources: Inventory, Job Material, Job Operation, SubContract
- Assigning an Inspector to NonConformances which are waiting to be inspected
- Recording the results of an Inspection, and the resulting move of the inspected item to
a job, scrap, corrective action/rework, or inventory
            
The Inspection Processing user interface is the only place where First Articles are entered and maintained.
            
The FirstArt.p object should be used to Add or Delete a First Article, and to get the listing
of previous inspection actions (GetHistory).  To inspect a a First Article, use
InspProcessing.InspectFirstArt().
            
The Inspections user interface also provides an entry point for RMA Dispositions, which is
supported by the RMAProc.p and RMADisp.p objects.
            
When the user commits an Inspection and has selected "Create Corrective Action", it is the UI
that must launch the Corrective Actions UI.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/$metadata", {
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
   Description: Get InspProcessings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspProcessings
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspProcListRow
   */  
export function get_InspProcessings(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspProcListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspProcListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspProcessing item
   Description: Calls GetByID to retrieve the InspProcessing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspProcessing
      @param xID Desc: xID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspProcListRow
   */  
export function get_InspProcessings_xID(xID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspProcListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspProcListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get InspFirstArts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspFirstArts1
      @param xID Desc: xID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspFirstArtRow
   */  
export function get_InspProcessings_xID_InspFirstArts(xID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspFirstArtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspFirstArts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspFirstArtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspFirstArt item
   Description: Calls GetByID to retrieve the InspFirstArt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspFirstArt1
      @param xID Desc: xID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspFirstArtRow
   */  
export function get_InspProcessings_xID_InspFirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(xID:string, Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspFirstArtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspFirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspFirstArtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get InspNonConfs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspNonConfs1
      @param xID Desc: xID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspNonConfRow
   */  
export function get_InspProcessings_xID_InspNonConfs(xID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspNonConfRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspNonConfs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspNonConfRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspNonConf item
   Description: Calls GetByID to retrieve the InspNonConf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspNonConf1
      @param xID Desc: xID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspNonConfRow
   */  
export function get_InspProcessings_xID_InspNonConfs_Company_TranID(xID:string, Company:string, TranID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspNonConfRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspNonConfs(" + Company + "," + TranID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspNonConfRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get InspRcpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspRcpts1
      @param xID Desc: xID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspRcptRow
   */  
export function get_InspProcessings_xID_InspRcpts(xID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspRcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspRcpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspRcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspRcpt item
   Description: Calls GetByID to retrieve the InspRcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspRcpt1
      @param xID Desc: xID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspRcptRow
   */  
export function get_InspProcessings_xID_InspRcpts_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(xID:string, Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, AttributeValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspRcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspRcpts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspRcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspFirstArts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspFirstArts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspFirstArtRow
   */  
export function get_InspFirstArts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspFirstArtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspFirstArts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspFirstArtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspFirstArt item
   Description: Calls GetByID to retrieve the InspFirstArt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspFirstArt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspFirstArtRow
   */  
export function get_InspFirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, ResourceID:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspFirstArtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspFirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspFirstArtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspNonConfs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspNonConfs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspNonConfRow
   */  
export function get_InspNonConfs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspNonConfRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspNonConfs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspNonConfRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspNonConf item
   Description: Calls GetByID to retrieve the InspNonConf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspNonConf
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranID Desc: TranID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspNonConfRow
   */  
export function get_InspNonConfs_Company_TranID(Company:string, TranID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspNonConfRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspNonConfs(" + Company + "," + TranID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspNonConfRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspRcpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspRcpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspRcptRow
   */  
export function get_InspRcpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspRcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspRcpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspRcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspRcpt item
   Description: Calls GetByID to retrieve the InspRcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspRcpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspRcptRow
   */  
export function get_InspRcpts_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, AttributeValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspRcptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspRcpts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspRcptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/LegalNumGenOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SelectedSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SNFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SupplierXRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SupplierXRefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierXRefRow
   */  
export function get_SupplierXRefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SupplierXRef item
   Description: Calls GetByID to retrieve the SupplierXRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SupplierXRef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param VendNum Desc: VendNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
   */  
export function get_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company:string, PartNum:string, VendNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SupplierXRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SupplierXRefRow)
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
   Description: To retrieve the list of items waiting to be inspected (InspProcList dataset).  This combines
onto one screen the browses shown on the various tabs of Inspection Processing screen in
Vantage v6.10.
Note that three of the six tabs are NonConformances, one is First Articles, one is Receipts
(from either POs or SubContracted operations) and one is for RMAs.  In Vantage v6.10, the
columns showing for each tab are different from those in the other tabs; an attempt has been
made here to include "identifying" columns.  This should allow a GetByID() call to load the
appropriate sheet for any of the different types.
            
There is an input parameter for each of these types, for which there should be a corresponding
checkbox.  The rows for a given type will only be fetched if its corresponding input is TRUE.
   OperationID: Get_GetRows
      @param plOperation Desc: If TRUE, include items that were sent to Inspection from a Job Operation.   Required: True
      @param plMaterial Desc: If TRUE, include items that were sent to Inspection from a Job Material.   Required: True
      @param plInventory Desc: If TRUE, include items that were sent to Inspection from Inventory.   Required: True
      @param plFirstArt Desc: If TRUE, include items that were sent to Inspection from a First Article.   Required: True
      @param plReceipt Desc: If TRUE, include items that were sent to Inspection from a PO or SubContract receipt.   Required: True
      @param plRMA Desc: If TRUE, include items that were sent to Inspection from an RMA.   Required: True
      @param pcInspectorID Desc: (optional) The Inspector ID typed in by the user.   Required: True   Allow empty value : True
      @param pcCutOffDate Desc: (optional) Cut Off Date .   Required: True   Allow empty value : True
      @param whereClauseNonConf Desc: (optional)Additional Where conditions for NonConf table.   Required: True   Allow empty value : True
      @param whereClauseFirstArt Desc: (optional)Additional Where conditions for FirstArt table.   Required: True   Allow empty value : True
      @param whereClauseRcvDtl Desc: (optional)Additional Where conditions for RcvDtl table.   Required: True   Allow empty value : True
      @param whereClauseRMA Desc: (optional)Additional Where conditions for RMAHead table.   Required: True   Allow empty value : True
      @param whereClauseSelectedSerialNumbers Desc: (optional)Additional Where conditions for SelectedSerialNumbers table.   Required: True   Allow empty value : True
      @param whereClauseSNFormat Desc: (optional)Additional Where conditions for SNFormat table.   Required: True   Allow empty value : True
      @param whereClauseInspProcList Desc: (optional)Additional Where conditions to be applied to result set.   Required: True   Allow empty value : True
      @param sortBy Desc: Sort By selected in search   Required: True   Allow empty value : True
      @param pageSize Desc: Page Size   Required: True
      @param absolutePage Desc: Absolute page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(plOperation:string, plMaterial:string, plInventory:string, plFirstArt:string, plReceipt:string, plRMA:string, pcInspectorID:string, pcCutOffDate:string, whereClauseNonConf:string, whereClauseFirstArt:string, whereClauseRcvDtl:string, whereClauseRMA:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, whereClauseInspProcList:string, sortBy:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plOperation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plOperation=" + plOperation
   }
   if(typeof plMaterial!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plMaterial=" + plMaterial
   }
   if(typeof plInventory!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plInventory=" + plInventory
   }
   if(typeof plFirstArt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plFirstArt=" + plFirstArt
   }
   if(typeof plReceipt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plReceipt=" + plReceipt
   }
   if(typeof plRMA!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plRMA=" + plRMA
   }
   if(typeof pcInspectorID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcInspectorID=" + pcInspectorID
   }
   if(typeof pcCutOffDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcCutOffDate=" + pcCutOffDate
   }
   if(typeof whereClauseNonConf!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseNonConf=" + whereClauseNonConf
   }
   if(typeof whereClauseFirstArt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFirstArt=" + whereClauseFirstArt
   }
   if(typeof whereClauseRcvDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvDtl=" + whereClauseRcvDtl
   }
   if(typeof whereClauseRMA!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRMA=" + whereClauseRMA
   }
   if(typeof whereClauseSelectedSerialNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   }
   if(typeof whereClauseSNFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNFormat=" + whereClauseSNFormat
   }
   if(typeof whereClauseInspProcList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspProcList=" + whereClauseInspProcList
   }
   if(typeof sortBy!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sortBy=" + sortBy
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetRows" + params, {
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
   Description: To retrieve the Inspection non conformance (InspProcessing dataset) corresponding to the
given TranID and the Operations tab or the Materials tab of the Inspections Processing
screen in Vantage v6.10.
   OperationID: Get_GetByID
      @param pcTranID Desc: The TranID of the NonConformance.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(pcTranID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pcTranID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcTranID=" + pcTranID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetByID" + params, {
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
   Summary: Invoke method AssignInspectorFar
   Description: To assign an Inspector to the First Article.
Validates the Inspector against the database and assigns it to the ttTable
   OperationID: AssignInspectorFar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignInspectorFar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignInspectorFar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignInspectorFar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/AssignInspectorFar", {
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
   Summary: Invoke method AssignInspectorNonConf
   Description: To assign an Inspector to the non conformance(s).
Validates the Inspector against the database and assigns it to the ttTable
   OperationID: AssignInspectorNonConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignInspectorNonConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignInspectorNonConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignInspectorNonConf(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/AssignInspectorNonConf", {
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
   Summary: Invoke method AssignInspectorReceipt
   Description: To assign an Inspector to the PO Receipt(s).
Validates the Inspector against the database and assigns it to the ttTable
   OperationID: AssignInspectorReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignInspectorReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignInspectorReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignInspectorReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/AssignInspectorReceipt", {
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
   Summary: Invoke method CheckPlanningContractBin
   Description: Method to check Contract bin.
   OperationID: CheckPlanningContractBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlanningContractBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlanningContractBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPlanningContractBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/CheckPlanningContractBin", {
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
   Summary: Invoke method CheckSerialNumCount
   Description: This method provides a message suitable for prompting the user to approve
a mismatch between the number of serial numbers selected and the quantity
being inspected.  Note that this mismatch is not always allowed; the
prompt is only offered when:
1) there is a quantity mismatch AND
2) the situation is one that permits the mismatch, if the user approves.
            
This method should be run just before any of the following:
InspectMaterial
InspectOperation
InspectInventory
InspectReceipt
            
If the pcMsg parameter comes back non-empty, present its contents to the user
as a Yes or No question.
Example:  "Number of selected Serial Numbers does not match passed quantity.  Serial Numbers selected: num_1 Total Serial Numbers required: num_2 Continue with quantity discrepancy?"
            
***** Important ***** Important *****
The user is answering the question "Continue with quantity discrepancy?".
Therefore, if the user answers "NO", set the EnforceSerialNumCount field to YES.
and if the user answers "YES", set the EnforceSerialNumCount field to NO
            
An exception is thrown if:
- the InspNonConf or InspRcpt row with a RowMod of "A" or "U" is not found
   OperationID: CheckSerialNumCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSerialNumCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSerialNumCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSerialNumCount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/CheckSerialNumCount", {
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
   Summary: Invoke method ConvQtysToBase
   Description: Convert Quantities to base qtys for serial number processing
   OperationID: ConvQtysToBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvQtysToBase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvQtysToBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvQtysToBase(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/ConvQtysToBase", {
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
   Summary: Invoke method GetDateUser
   Description: This method puts a date/time/user stamp in the text value for the user
   OperationID: GetDateUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDateUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDateUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetDateUser", {
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
   Summary: Invoke method GetFailedLegalNumGenOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for the failed transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GetFailedLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFailedLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFailedLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFailedLegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetFailedLegalNumGenOpts", {
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
   Summary: Invoke method GetFirstArtByID
   Description: To retrieve the Inspection FirstArt (InspProcessing dataset) corresponding to the
given JobNum, AssemblySeq, OprSeq, ResourceID, and SeqNum and the First Article tab
of the Inspections Processing screen in Vantage v6.10.
   OperationID: GetFirstArtByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFirstArtByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFirstArtByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFirstArtByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetFirstArtByID", {
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
   Summary: Invoke method GetInspRcptSelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable for the InspRcpt RowIdent.
   OperationID: GetInspRcptSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspRcptSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspRcptSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInspRcptSelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetInspRcptSelectedSerialNumbers", {
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
   Summary: Invoke method GetInspResultsPassFail
   Description: This method will get the passed/failed quantity from InspResults for Non Conformance
   OperationID: GetInspResultsPassFail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspResultsPassFail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspResultsPassFail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInspResultsPassFail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetInspResultsPassFail", {
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
   Summary: Invoke method GetNonConfPartTranPKs
   Description: Return Primary Keys for generated PartTran records.
   OperationID: GetNonConfPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNonConfPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNonConfPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNonConfPartTranPKs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetNonConfPartTranPKs", {
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
   Summary: Invoke method GetMtlQueueSeqValue
   Description: Search for the MtlQueueSeq value from the MtlQueue row related to the current Non Conformance.
   OperationID: GetMtlQueueSeqValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlQueueSeqValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueSeqValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlQueueSeqValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetMtlQueueSeqValue", {
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
   Summary: Invoke method GetPassedLegalNumGenOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GetPassedLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPassedLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPassedLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPassedLegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetPassedLegalNumGenOpts", {
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
   Summary: Invoke method ValidateTranDocType
   Description: Verify if the selected transaction document type for
passed or failed quantity is valid for inspection transactions,
if it is active and if the user is authorized to use it.
   OperationID: ValidateTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTranDocType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/ValidateTranDocType", {
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
   Summary: Invoke method GetReceiptByID
   Description: To retrieve the Inspection Receipt (InspProcessing dataset) corresponding to the
given VendorNum, PurPoint, PackSlip, and PackLine and the Receipts tab
of the Inspections Processing screen in Vantage v6.10.
   OperationID: GetReceiptByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReceiptByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceiptByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReceiptByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetReceiptByID", {
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
   Summary: Invoke method GetReceiptPartTranPKs
   Description: Return Primary Keys for generated PartTran records.
   OperationID: GetReceiptPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReceiptPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceiptPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReceiptPartTranPKs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetReceiptPartTranPKs", {
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
   Summary: Invoke method GetRowsLP
   Description: To retrieve the list of items waiting to be inspected (InspProcList dataset) on the Landing Page.
   OperationID: GetRowsLP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsLP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsLP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsLP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetRowsLP", {
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
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable for the InspNonConf RowIdent.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetSelectedSerialNumbers", {
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
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method InspectFirstArt
   Description: To process an inspection of First Article (InspFirstArt datatable).
Corresponds to the First Articles tab of the Inspections Processing screen in Vantage v6.10.
Use this method where you would typically use the Update() method, when the item being
inspected is a First Article.
   OperationID: InspectFirstArt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectFirstArt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectFirstArt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectFirstArt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectFirstArt", {
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
   Summary: Invoke method InspectInventory
   Description: To process an inspection of Inventory-related non conformances (NonConf dataset).
Corresponds to the Inventory tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is an Inventory Material.
   OperationID: InspectInventory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectInventory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectInventory", {
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
   Summary: Invoke method InspectInventory2
   Description: To process an inspection of Inventory-related non conformances (NonConf dataset).
Corresponds to the Inventory tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is an Inventory Material.
   OperationID: InspectInventory2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectInventory2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectInventory2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectInventory2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectInventory2", {
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
   Summary: Invoke method InspectMaterial
   Description: To process an inspection of JobMaterial-related non conformances (NonConf dataset).
Corresponds to the Material tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is an Inventory Material.
   OperationID: InspectMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectMaterial(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectMaterial", {
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
   Summary: Invoke method InspectMaterial2
   Description: To process an inspection of JobMaterial-related non conformances (NonConf dataset).
Corresponds to the Material tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is an Inventory Material.
   OperationID: InspectMaterial2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectMaterial2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectMaterial2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectMaterial2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectMaterial2", {
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
   Summary: Invoke method InspectOperation
   Description: To process an inspection of Operations-related non conformances (NonConf dataset).
Corresponds to the Operations tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is a Job Assembly / Job Operation.
   OperationID: InspectOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectOperation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectOperation", {
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
   Summary: Invoke method InspectOperation2
   Description: To process an inspection of Operations-related non conformances (NonConf dataset).
Corresponds to the Operations tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is a Job Assembly / Job Operation.
   OperationID: InspectOperation2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectOperation2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectOperation2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectOperation2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectOperation2", {
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
   Summary: Invoke method InspectReceipt
   Description: To process an inspection of Receipt, either a PO or SubContract.
Corresponds to the PO Receipts tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is a PO Receipt.
   OperationID: InspectReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectReceipt", {
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
   Summary: Invoke method InspectReceipt2
   Description: To process an inspection of Receipt, either a PO or SubContract.
Corresponds to the PO Receipts tab of the Inspections Processing screen in Vantage v6.10.
            
Use this method where you would typically use the Update() method, when the item being
inspected is a PO Receipt.
   OperationID: InspectReceipt2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InspectReceipt2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InspectReceipt2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspectReceipt2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspectReceipt2", {
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
   Summary: Invoke method OnChangeAssemblySeq
   Description: This method validates the piProposedAssemblySeq, then clears the related fields.
            
This method should be run when the Assembly Seq field changes.
            
An exception is thrown if:
- the proposed Assembly Seq does not exist for the given Assembly
   OperationID: OnChangeAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssemblySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangeAssemblySeq", {
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
   Summary: Invoke method OnChangeFailedQty
   Description: This method validates the pdProposedFailedQty, then if zero, clears the related fields.
This method should be run when the FailedQty field changes.
An exception is thrown if:
- Passed Quantity + Failed Quantity greater than the original quantity
   OperationID: OnChangeFailedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFailedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFailedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFailedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangeFailedQty", {
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
   Summary: Invoke method OnChangeFAInspectedQty
   Description: This routine is for First Article inspections only.
Gives a warning message if the proposed Inspected Quantity is less than
the Expected Quantity.
This method should be run when the ttInspFirstArt.InspectedQuantity field changes.
An exception is thrown if:
- No added or modified row is found in the dataset.
   OperationID: OnChangeFAInspectedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFAInspectedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFAInspectedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFAInspectedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangeFAInspectedQty", {
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
   Summary: Invoke method OnChangeIssueComplete
   Description: For use only with Receipt Inspections
            
This method checks for a conflict among:
- the quantity passing inspection,
- the remaining quantity needed,
- the IssuedComplete field in the dataset (aka a checkbox on the screen),
- the IssuedComplete flag stored on the JobMtl or JobOper record
If a conflict is found, this routine returns:
- text intended for prompting the user to give their okay
- the name of the field in the dataset in which to put the user's Okay/NotOkay response.
            
There are four possible scenarios where the user may be asked to confirm an
unusual action:
1) Issuing to a JobMtl that had been marked complete, and now the user indicates
it is no longer considered complete.
Text for prompt returned (may be translated): "The Job Material requirement is Closed...  do you really want it reopened?"
Field in which to record the user's response: IsOkToReopenJobMtl
2) Issuing to a JobMtl that would still need more quantity, but the user
indicates it is considered complete.
Text for prompt returned (may be translated): "Quantity issued is less than requirement...  Are you sure you want to close this material requirement?"
Field in which to record the user's response: IsOkToCloseJobMtl
3) Issuing to a SubContract that had been marked complete, and now the user indicates
it is no longer considered complete.
Text for prompt returned (may be translated): "The Subcontract operation is complete...  do you really want it reopened?"
Field in which to record the user's response: IsOkToReopenSubContract
4) Issuing to a SubContract that would still need more quantity, but the user
indicates it is considered complete.
Text for prompt returned (may be translated): "Quantity issued is less than requirement...  Are you sure you want to close this subcontract operation?"
Field in which to record the user's response: IsOkToCloseSubContract
            
This method should be run when the InspRcpt.IssuedComplete field changes.
            
An exception is thrown if:
-
   OperationID: OnChangeIssueComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIssueComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIssueComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIssueComplete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangeIssueComplete", {
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
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the pcProposedJobNum, then clears the job-related fields.
This method should be run when the InspRcpt.JobNum field changes.
An exception is thrown if:
- No Job exists with the given Job Number
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangeJobNum", {
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
   Summary: Invoke method OnChangeJobSeq
   Description: For use only with Receipt Inspections.
For Inventory Inspections, see OnChangeMtlSeq().
            
This method validates the piProposedJobSeq, then clears the job-related fields.
            
The JobSeq field holds a JobMtl.MtlSeq when passing inspection to a Job Material.
The JobSeq field holds a JobOper.OprSeq when passing inspection to a Job Operation.
            
This method should be run when the InspRcpt.JobSeq field changes.
            
An exception is thrown if:
- No related JobMtl or JobOper exists with the given Job sequence number.
   OperationID: OnChangeJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangeJobSeq", {
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
   Summary: Invoke method OnChangeMtlSeq
   Description: For use only with Inventory Inspections.
For Receipt Inspections, see OnChangeJobSeq().
            
This method validates the pcProposedMtlSeq, then provides the defaults for the
material-related fields.
            
This method should be run when the InsNonConf.MtlSeq field changes.
            
An exception is thrown if:
- No related JobMtl exists with the given sequence number.
   OperationID: OnChangeMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMtlSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangeMtlSeq", {
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
   Summary: Invoke method OnChangePassedIssueTo
   Description: This method validates the pcProposedIssueTo, then sets the default values of the related fields.
            
This method should be run when the PassedIssueTo field changes.  Only Inventory and Receipt
Inspections offer a choice of where to send items passing inspection--so the others have no need
for this routine.
            
An exception is thrown if:
- the proposed PassedIssueTo is not valid.  If this is a radio set as in v6.10, only a
programming error could ever lead to an exception.
   OperationID: OnChangePassedIssueTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePassedIssueTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePassedIssueTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePassedIssueTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangePassedIssueTo", {
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
   Summary: Invoke method OnChangePassedQty
   Description: This method validates the pdProposedPassedQty, then if zero, clears the related fields.
This method should be run when the PassedQty field changes.
An exception is thrown if:
- Passed Quantity + Failed Quantity greater than the original quantity
   OperationID: OnChangePassedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePassedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePassedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePassedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangePassedQty", {
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
   Summary: Invoke method OnChangePassedWhse
   OperationID: OnChangePassedWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePassedWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePassedWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePassedWhse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangePassedWhse", {
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
   Summary: Invoke method OnChangePCID
   Description: Validates that PCID exists
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/OnChangePCID", {
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
   Summary: Invoke method ValidateSN
   Description: validates serial numbers entered on the generic serial number selection/create form called from the pass/fail form
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/ValidateSN", {
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
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/GetCodeDescList", {
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
   Summary: Invoke method DisplayWarnMsg
   OperationID: DisplayWarnMsg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisplayWarnMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisplayWarnMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisplayWarnMsg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/DisplayWarnMsg", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspFirstArtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspFirstArtRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspNonConfRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspNonConfRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspProcListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspProcListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspRcptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspRcptRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SupplierXRefRow[],
}

export interface Erp_Tablesets_InspFirstArtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job number to which this first article transaction applies.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the first article transaction applies to.  */  
   "AssemblySeq":number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   "ResourceID":string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   "SeqNum":number,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   "ExpectedQuantity":number,
      /**  An ID of the person who did the first article inspection.  */  
   "InspectorID":string,
      /**  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  */  
   "EmployeeNum":string,
      /**  This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  */  
   "FAStatus":string,
      /**  System date at time inspection time.  */  
   "ActionDate":string,
      /**  System Time (hr-min-sec) at time of inspection.  */  
   "ActionTime":number,
      /**  Contains comments about the inspection.  */  
   "CommentText":string,
      /**  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  */  
   "InspectedQuantity":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   "UOMCode":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   "JobAsmPartNum":string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   "JobAsmRevisionNum":string,
      /**  Unique ID field to establish relationship with InspProcList  */  
   "xID":string,
   "InspDataRequired":boolean,
   "InspDataEntered":boolean,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "BitFlag":number,
   "EmployeeNumFirstName":string,
   "EmployeeNumLastName":string,
   "EmployeeNumName":string,
   "InspectorIDName":string,
   "JobAsmDescription":string,
   "JobNumPartDescription":string,
   "ResourceIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspNonConfRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quantity of the material to be scrapped.  */  
   "Quantity":number,
      /**  Scrap reason code.  */  
   "ReasonCode":string,
      /**  Job Number of the JobAsmbl record.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  */  
   "MtlSeq":number,
      /**  The field that identifies the Part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Scrap Labor Cost.  */  
   "ScrapLaborCost":number,
      /**  Scrap Burden Cost.  */  
   "ScrapBurdenCost":number,
      /**  Scrap Material Cost.  */  
   "ScrapMaterialCost":number,
      /**  Scrap Material Bur Cost.  */  
   "ScrapMaterialBurCost":number,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   "TrnTyp":string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   "DimCode":string,
      /**  The operation sequence of the Job/Assembly.  */  
   "OprSeq":number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  */  
   "ResourceID":string,
      /**  Describes the Part.  */  
   "Description":string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   "EntryPerson":string,
      /**  Employee ID.  */  
   "EmpID":string,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   "InspectionPending":boolean,
      /**  Defines the Unit of Measure used when part is scrapped.  */  
   "ScrapUM":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The conversion factor used to convert the material.  */  
   "DimConvFactor":number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   "LaborHedSeq":number,
      /**  Used as a foreign key for LaborDtl record.  */  
   "LaborDtlSeq":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  Contains comments about the transaction.  */  
   "PsdCommentText":string,
      /**  Contains comments about the transaction.  */  
   "FldCommentText":string,
      /**  Supplier Purchase Point  */  
   "PurPoint":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Non conformance warehosue code  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "BinNum":string,
      /**  Scrap Labor Cost.  */  
   "ScrapSubCost":number,
      /**  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  */  
   "QtyFrm":string,
      /**  A unique number for the transaction.  Auto increment.  */  
   "TranID":number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  */  
   "Plant":string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   "RMANum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  Receipt Number of related RMARcpt record.  */  
   "RMAReceipt":number,
      /**  Disposition Number of related RMADisp record.  */  
   "RMADisp":number,
      /**  Contains comments about the Non-Conformance transaction.  */  
   "CommentText":string,
      /**  Mtl Mtl unit cost to date.  */  
   "MaterialMtlCost":number,
      /**  Mtl Lab unit cost to date  */  
   "MaterialLabCost":number,
      /**  Mtl Sub Unit cost to date  */  
   "MaterialSubCost":number,
      /**  Material  Burd unit component cost to date  */  
   "MaterialBurCost":number,
      /**  Operation Master Code  */  
   "OpCode":string,
      /**  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  */  
   "ToWarehouseCode":string,
      /**  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  */  
   "ToBinNum":string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   "AQMNCMNum":string,
      /**   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  */  
   "MoveCostsToDMR":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  */  
   "MtlSourceTrnType":string,
      /**  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "ResourceGrpID":string,
      /**  Long description of the Work Center.  */  
   "WrkCntrDesc":string,
      /**  Indicator of user's request to create a MtlQueue for passed items.  */  
   "PassedMove":boolean,
      /**  Location to which passed items are to be moved.  */  
   "PassedWarehouseCode":string,
      /**  Location to which passed items are to be moved.  */  
   "PassedBin":string,
      /**  Indicator of user's request to create a MtlQueue for failed items.  */  
   "FailedMove":boolean,
      /**  Location to which failed items are to be moved.  */  
   "FailedWarehouseCode":string,
      /**  Location to which failed items are to be moved.  */  
   "FailedBin":string,
      /**  Indicator of user's request to create a Corrective Action.  */  
   "CreateCorAct":boolean,
      /**  Issue To specifies where the quantity that passed should be issued. For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  */  
   "PassedIssueTo":string,
      /**  Indicates whether or not the part is complete when it is issued back to the job. If the part is complete (not taken apart) when it is returned to the job, this is YES This field is available if PassedIssueTo is Job Assembly (ASM) or Job Material (MTL).  */  
   "PassedIssuedComplete":boolean,
      /**  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  */  
   "FailedReasonCode":string,
      /**  Flag to indicate whether serial numbers will be required during inspection processing.  */  
   "EnforceSerialNumCount":boolean,
      /**  PartNum of Job Assembly passed part is to be issued to.  */  
   "PassedJobPartNum":string,
      /**  Description of Job Assembly passed part is to be issued to.  */  
   "PassedJobPartDesc":string,
      /**  This is how many of the assemblies are required to produce the END ITEM.  */  
   "PassedJobQty":number,
      /**  Unique ID field to establish relationship with InspProcList  */  
   "xID":string,
   "FailedBinDescription":string,
   "FailedReasonDescription":string,
   "FailedWarehouseDescription":string,
   "PassedBinDescription":string,
   "PassedWarehouseDescription":string,
      /**  Quantity of the material to be scrapped.  */  
   "DimQuantity":number,
      /**  = PassedQty * DimConvFactor  */  
   "DimPassedQty":number,
      /**  = FailedQty * DimConvFactor  */  
   "DimFailedQty":number,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   "AcceptUM":string,
      /**  The Quantity field converted to the UOM defined in the job material  */  
   "TranQty":number,
      /**  The UOM defined in the job material  */  
   "TranUOM":string,
   "RequiredQtyUOM":string,
      /**  To enable/disable Serial Tracking options in UI screens.  */  
   "EnableSerialTracking":boolean,
   "InspDataRequired":boolean,
   "InspDataEntered":boolean,
      /**  It is used to print Inventory Movement after processing.  */  
   "Done":boolean,
      /**  Failed Legal Number  */  
   "FailedLegalNumber":string,
   "FailedLegalNumberID":string,
      /**  Failed Legal Number Message  */  
   "FailedLegalNumberMsg":string,
      /**  Failed Transaction Document Type  */  
   "FailedTranDocTypeID":string,
      /**  Passed Transaction Document Type  */  
   "PassedTranDocTypeID":string,
      /**  Passed Legal Number  */  
   "PassedLegalNumber":string,
      /**  Passed Legal Number ID  */  
   "PassedLegalNumberID":string,
      /**  Passed Legal Number Message  */  
   "PassedLegalNumberMsg":string,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "PassedPCID":string,
   "FailedPCID":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "DMRNumPartDescription":string,
   "InspectorIDName":string,
   "JobNumPartDescription":string,
   "OpCodeOpDesc":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumAttrClassID":string,
   "ToBinNumDescription":string,
   "VendorNumAddress1":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumVendorID":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumState":string,
   "VendorNumCurrencyCode":string,
   "VendorNumTermsCode":string,
   "VendorNumName":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspProcListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quantity of the material to be scrapped.  */  
   "Quantity":number,
      /**  Scrap reason code.  */  
   "ReasonCode":string,
      /**  Job Number of the JobAsmbl record.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  The field that identifies the Part.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   "TrnTyp":string,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   "EntryPerson":string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The operation sequence of the Job/Assembly.  */  
   "OprSeq":number,
   "WarehouseCode":string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "BinNum":string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   "DimCode":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  The ID of the machine that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   "ResourceID":string,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   "ExpectedQuantity":number,
      /**  System date at time that record was created.  */  
   "FirstArtSysDate":string,
      /**  Employee ID.  */  
   "EmpID":string,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  */  
   "VendorID":string,
      /**  Receipt date.  */  
   "ReceiptDate":string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   "RMANum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  A unique number for the transaction.  Auto increment.  */  
   "NonConfTranID":number,
      /**  RowID of related NonConf record  */  
   "NonConfRowIdent":string,
      /**  RowId of related First Art record  */  
   "FirstArtRowIdent":string,
      /**  RowId of related RcvDtl record  */  
   "RcvDtlRowIdent":string,
      /**  RowId of related RMARecpt record  */  
   "RMARecptRowIdent":string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   "SeqNum":number,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
   "RMAReceipt":number,
      /**  Unique ID field to establish relationship between InspProcList and child tables InspFirstArt, InspNonConf, InspRcpt  */  
   "xID":string,
      /**  Description of the source of the item to be inspected: Operations,First Articles,Inventory,Material,PO Receipts,RMAs  */  
   "TrnTypDescription":string,
   "EmpIDFirstName":string,
   "EmpIDLastName":string,
   "EmpIDName":string,
   "InspectorIDName":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "UOM":string,
   "InspDataEntered":boolean,
   "InspDataRequired":boolean,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   "AQMNCMNum":string,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "PCID":string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   "TrackInventoryByRevision":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspRcptRow{
      /**  Company Indentifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Supplier master file.  */  
   "VendorNum":number,
      /**  The Supplier purchase point ID.  */  
   "PurPoint":string,
      /**  Supplier Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   "AttributeValueSeq":number,
      /**  Dynamic Attribute Value Set ID for this receipt detail.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Receipt quantity in our unit of measure for this attribute set.  */  
   "OurQty":number,
      /**  Indicates whether the Attribute Value was auto-generated by the system.  */  
   "AutoGenerated":boolean,
      /**  Supplier selling Unit of Measure.  */  
   "PUM":string,
      /**  Quantity received against a purchase order in the Supplier unit of measure.  */  
   "VendorQty":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Unit of measure for the NumberOfPieces.  */  
   "NumberOfPiecesUOM":string,
      /**  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   "InspectionPending":boolean,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   "InspectionReq":boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  Date when item was inspected.  */  
   "InspectedDate":string,
      /**  Time of day when inspection transaction was recorded.  */  
   "InspectedTime":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  Unique ID field to establish relationship with InspProcList  */  
   "xID":string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   "AcceptUM":string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   "AQMNCMNum":string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   "AssemblySeq":number,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "BinNum":string,
      /**  Indicator of user's request to create a Corrective Action.  */  
   "CreateCorAct":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  = FailedQty * DimConvFactor  */  
   "DimFailedQty":number,
      /**  = OurQty * DimConvFactor  */  
   "DimOurQty":number,
      /**  = PassedQty * DimConvFactor  */  
   "DimPassedQty":number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  It is used to print Inventory Movement after processing.  */  
   "Done":boolean,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   "DUM":string,
      /**  Flag to indicate whether serial numbers will be required during inspection processing.  */  
   "EnforceSerialNumCount":boolean,
      /**  Location to which failed items are to be moved.  */  
   "FailedBin":string,
   "FailedBinDescription":string,
      /**  Failed Legal Number  */  
   "FailedLegalNumber":string,
      /**  Failed Legal Number ID  */  
   "FailedLegalNumberID":string,
      /**  Failed Legal Number Message  */  
   "FailedLegalNumberMsg":string,
      /**  Indicator of user's request to create a MtlQueue for failed items.  */  
   "FailedMove":boolean,
      /**  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  */  
   "FailedReasonCode":string,
   "FailedReasonDescription":string,
      /**  Failed Transaction Document Type  */  
   "FailedTranDocTypeID":string,
      /**  Location to which failed items are to be moved.  */  
   "FailedWarehouseCode":string,
   "FailedWarehouseDescription":string,
      /**  Comments on the items failing inspection.  */  
   "FldCommentText":string,
   "InspDataEntered":boolean,
   "InspDataRequired":boolean,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   "Invoiced":boolean,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   "InvoiceLine":number,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   "InvoiceNum":string,
      /**  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this material requirement?"  */  
   "IsOkToCloseJobMtl":boolean,
      /**  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this subcontract operation?"  */  
   "IsOkToCloseSubContract":boolean,
      /**  Holds user's response to the question: "The Job Material requirement is Closed...  do you really want it reopened?"  */  
   "IsOkToReopenJobMtl":boolean,
      /**  Holds user's response to the question: "The Subcontract operation is complete...  do you really want it reopened?"  */  
   "IsOkToReopenSubContract":boolean,
      /**  Holds user's response to the question: "Serial numbers assigned to Job Subcontracts are not tracked.  The Serial Numbers that have been assigned to this receipt will be deselected.  Are you sure this receipt is to a Job Subcontract?"  */  
   "IsOkToUnassignSerNums":boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "IssuedComplete":boolean,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   "JobNum":string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   "JobSeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   "JobSeqType":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  Lot Number  */  
   "LotNum":string,
      /**  The material burden rate for this part.  */  
   "MtlBurRate":number,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   "NonConformnce":boolean,
      /**  Number of labels  */  
   "NumLabels":number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   "OurMtlBurUnitCost":number,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "OurUnitCost":number,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   "PartNum":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
      /**  Location to which passed items are to be moved.  */  
   "PassedBin":string,
   "PassedBinDescription":string,
      /**  Issue To specifies where the quantity that passed should be issued.  For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  */  
   "PassedIssueTo":string,
   "PassedJobIUM":string,
      /**  Description of Job Assembly passed part is to be issued to.  */  
   "PassedJobPartDesc":string,
      /**  PartNum of Job Assembly passed part is to be issued to.  */  
   "PassedJobPartNum":string,
      /**  This is how many of the assemblies are required to produce the END ITEM.  */  
   "PassedJobQty":number,
      /**  Passed Legal Number  */  
   "PassedLegalNumber":string,
      /**  Passed Legal Number ID  */  
   "PassedLegalNumberID":string,
      /**  Passed Legal Number Message  */  
   "PassedLegalNumberMsg":string,
      /**  Indicator of user's request to create a MtlQueue for passed items.  */  
   "PassedMove":boolean,
      /**  Passed Transaction Document Type  */  
   "PassedTranDocTypeID":string,
      /**  Location to which passed items are to be moved  */  
   "PassedWarehouseCode":string,
   "PassedWarehouseDescription":string,
      /**  Plant  */  
   "Plant":string,
      /**  Contains comments about over all  purchase order. These will be printed on the purchase order.  */  
   "POHeaderComment":string,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  Comments on items passing inspection.  */  
   "PsdCommentText":string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   "ReasonCode":string,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers. - This description was for when InspRcpt was tied to RcvDtl  */  
   "ReceiptDate":string,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   "ReceiptType":string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "ReceivedComplete":boolean,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   "ReceivedTo":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
   "RefDisplayAccount":string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   "RevisionNum":string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   "TotCostVariance":number,
      /**  The Quantity field converted to the UOM defined in the job material  */  
   "TranQty":number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   "TranReference":string,
      /**  The UOM defined in the job material  */  
   "TranUOM":string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   "VendorUnitCost":number,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   "VenPartNum":string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   "WareHouseCode":string,
      /**  Weight  */  
   "Weight":number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Was a link column on RcvDtl.  */  
   "BinNumDescription":string,
      /**  Was a link column on RcvDtl.  */  
   "DimCodeDimCodeDescription":string,
      /**  Was a link column on RcvDtl.  */  
   "JobNumPartDescription":string,
      /**  Was a link column on RcvDtl.  */  
   "PartNumAttrClassID":string,
      /**  Was a link column on RcvDtl.  */  
   "PartNumIUM":string,
      /**  Was a link column on RcvDtl.  */  
   "PartNumPartDescription":string,
      /**  Was a link column on RcvDtl.  */  
   "PartNumPricePerCode":string,
      /**  Was a link column on RcvDtl.  */  
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
      /**  Was a link column on RcvDtl.  */  
   "PartNumTrackDimension":boolean,
      /**  Was a link column on RcvDtl.  */  
   "POLineLineDesc":string,
      /**  Was a link column on RcvDtl.  */  
   "POLinePartNum":string,
      /**  Was a link column on RcvDtl.  */  
   "POLineVenPartNum":string,
      /**  Was a link column on RcvDtl.  */  
   "WarehouseCodeDescription":string,
   "PCID":string,
   "FailedPCID":string,
   "PassedPCID":string,
   "BitFlag":number,
   "InspectorIDName":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress3":string,
   "VendorNumState":string,
   "VendorNumAddress2":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumDefaultFOB":string,
   "VendorNumVendorID":string,
   "VendorNumCity":string,
   "VendorNumName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Number of digits in the serial number  */  
   "NumberOfDigits":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
   "SNFormat1":string,
      /**  Whether or not to have leading zeroes  */  
   "LeadingZeroes":boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
   "HasSerialNumbers":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PartPricePerCode":string,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartPartDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskMask":string,
   "SerialMaskExample":string,
   "SerialMaskDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   "Company":string,
      /**  SerialNumber  */  
   "SerialNumber":string,
      /**  Scrapped flag  */  
   "Scrapped":boolean,
      /**  Scrapped reason code  */  
   "ScrappedReasonCode":string,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Reference field  */  
   "Reference":string,
      /**  Reason code type = s  */  
   "ReasonCodeType":string,
      /**  Reason code description  */  
   "ReasonCodeDesc":string,
      /**  PartNumber  */  
   "PartNum":string,
      /**  Serial number prefix  */  
   "SNPrefix":string,
      /**  Base number used to create the serial number  */  
   "SNBaseNumber":string,
      /**  RowID of the source record for this serial number  */  
   "SourceRowID":string,
      /**  TransType of the record that created this serial number  */  
   "TransType":string,
      /**  True if this serial numbered part passed inspection  */  
   "PassedInspection":boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   "Deselected":boolean,
   "KitWhseList":string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   "KBLbrAction":number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   "KBLbrActionDesc":string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   "PreventDeselect":boolean,
      /**  Used only by SN Assignment  */  
   "XRefPartNum":string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   "XRefPartType":string,
   "PreDeselected":boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   "poLinkValues":string,
      /**  The mask the was used to generate the serial number  */  
   "SNMask":string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   "NotSavedToDB":boolean,
   "RowSelected":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SupplierXRefRow{
   "Company":string,
   "MfgID":string,
   "MfgName":string,
   "MfgNum":number,
   "MfgPartNum":string,
   "PartNum":string,
   "POReference":boolean,
   "Receipt":boolean,
   "VendNum":number,
   "VendPartNum":string,
   "Invoice":boolean,
      /**  RcvXRefNum  */  
   "RcvXRefNum":number,
   "Inspected":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param pcInspectorID
      @param ds
   */  
export interface AssignInspectorFar_input{
      /**  (optional) The Inspector ID typed in by the user.  */  
   pcInspectorID:string,
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface AssignInspectorFar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param pcInspectorID
      @param ds
   */  
export interface AssignInspectorNonConf_input{
      /**  (optional) The Inspector ID typed in by the user.  */  
   pcInspectorID:string,
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface AssignInspectorNonConf_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   infoMsg:string,
}
}

   /** Required : 
      @param pcInspectorID
      @param ds
   */  
export interface AssignInspectorReceipt_input{
      /**  (optional) The Inspector ID typed in by the user.  */  
   pcInspectorID:string,
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface AssignInspectorReceipt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   infoMsg:string,
}
}

   /** Required : 
      @param ds
      @param pcSource
   */  
export interface CheckPlanningContractBin_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcSource:string,
}

export interface CheckPlanningContractBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcPCBinAction:string,
   pcPCBinMessage:string,
}
}

   /** Required : 
      @param ds
      @param pcSource
   */  
export interface CheckSerialNumCount_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf" or "Receipt"  */  
   pcSource:string,
}

export interface CheckSerialNumCount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcMsg:string,
}
}

   /** Required : 
      @param pcPartNum
      @param piQuantity
      @param piPassedQty
      @param piFailedQty
      @param pcAcceptUM
   */  
export interface ConvQtysToBase_input{
      /**  AcceptUM.  */  
   pcPartNum:string,
      /**  dimQuantity.  */  
   piQuantity:number,
      /**  dimPassedQty.  */  
   piPassedQty:number,
      /**  dimFailedQty.  */  
   piFailedQty:number,
      /**  AcceptUM.  */  
   pcAcceptUM:string,
}

export interface ConvQtysToBase_output{
parameters : {
      /**  output parameters  */  
   piBaseQty:number,
   piBasePassQty:number,
   piBaseFailQty:number,
}
}

   /** Required : 
      @param PartTranType
      @param JobNum
      @param AsmSeq
      @param JobSeq
   */  
export interface DisplayWarnMsg_input{
   PartTranType:string,
   JobNum:string,
   AsmSeq:number,
   JobSeq:number,
}

export interface DisplayWarnMsg_output{
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

export interface Erp_Tablesets_InspFirstArtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job number to which this first article transaction applies.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the first article transaction applies to.  */  
   AssemblySeq:number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   ResourceID:string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   SeqNum:number,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   ExpectedQuantity:number,
      /**  An ID of the person who did the first article inspection.  */  
   InspectorID:string,
      /**  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  */  
   EmployeeNum:string,
      /**  This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  */  
   FAStatus:string,
      /**  System date at time inspection time.  */  
   ActionDate:string,
      /**  System Time (hr-min-sec) at time of inspection.  */  
   ActionTime:number,
      /**  Contains comments about the inspection.  */  
   CommentText:string,
      /**  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  */  
   InspectedQuantity:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  User defined code which uniquely identifies the UOM within the UOMClass.  */  
   UOMCode:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   JobAsmPartNum:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   JobAsmRevisionNum:string,
      /**  Unique ID field to establish relationship with InspProcList  */  
   xID:string,
   InspDataRequired:boolean,
   InspDataEntered:boolean,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BitFlag:number,
   EmployeeNumFirstName:string,
   EmployeeNumLastName:string,
   EmployeeNumName:string,
   InspectorIDName:string,
   JobAsmDescription:string,
   JobNumPartDescription:string,
   ResourceIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspNonConfRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quantity of the material to be scrapped.  */  
   Quantity:number,
      /**  Scrap reason code.  */  
   ReasonCode:string,
      /**  Job Number of the JobAsmbl record.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  */  
   MtlSeq:number,
      /**  The field that identifies the Part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Scrap Labor Cost.  */  
   ScrapLaborCost:number,
      /**  Scrap Burden Cost.  */  
   ScrapBurdenCost:number,
      /**  Scrap Material Cost.  */  
   ScrapMaterialCost:number,
      /**  Scrap Material Bur Cost.  */  
   ScrapMaterialBurCost:number,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   TrnTyp:string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   DimCode:string,
      /**  The operation sequence of the Job/Assembly.  */  
   OprSeq:number,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  */  
   ResourceID:string,
      /**  Describes the Part.  */  
   Description:string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   EntryPerson:string,
      /**  Employee ID.  */  
   EmpID:string,
      /**  To indicate if the record has been inspected (Open/Closed).  */  
   InspectionPending:boolean,
      /**  Defines the Unit of Measure used when part is scrapped.  */  
   ScrapUM:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The conversion factor used to convert the material.  */  
   DimConvFactor:number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   LaborHedSeq:number,
      /**  Used as a foreign key for LaborDtl record.  */  
   LaborDtlSeq:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  Contains comments about the transaction.  */  
   PsdCommentText:string,
      /**  Contains comments about the transaction.  */  
   FldCommentText:string,
      /**  Supplier Purchase Point  */  
   PurPoint:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Non conformance warehosue code  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Scrap Labor Cost.  */  
   ScrapSubCost:number,
      /**  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  */  
   QtyFrm:string,
      /**  A unique number for the transaction.  Auto increment.  */  
   TranID:number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  */  
   Plant:string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  Receipt Number of related RMARcpt record.  */  
   RMAReceipt:number,
      /**  Disposition Number of related RMADisp record.  */  
   RMADisp:number,
      /**  Contains comments about the Non-Conformance transaction.  */  
   CommentText:string,
      /**  Mtl Mtl unit cost to date.  */  
   MaterialMtlCost:number,
      /**  Mtl Lab unit cost to date  */  
   MaterialLabCost:number,
      /**  Mtl Sub Unit cost to date  */  
   MaterialSubCost:number,
      /**  Material  Burd unit component cost to date  */  
   MaterialBurCost:number,
      /**  Operation Master Code  */  
   OpCode:string,
      /**  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  */  
   ToWarehouseCode:string,
      /**  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  */  
   ToBinNum:string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   AQMNCMNum:string,
      /**   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  */  
   MoveCostsToDMR:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  */  
   MtlSourceTrnType:string,
      /**  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  Long description of the Work Center.  */  
   WrkCntrDesc:string,
      /**  Indicator of user's request to create a MtlQueue for passed items.  */  
   PassedMove:boolean,
      /**  Location to which passed items are to be moved.  */  
   PassedWarehouseCode:string,
      /**  Location to which passed items are to be moved.  */  
   PassedBin:string,
      /**  Indicator of user's request to create a MtlQueue for failed items.  */  
   FailedMove:boolean,
      /**  Location to which failed items are to be moved.  */  
   FailedWarehouseCode:string,
      /**  Location to which failed items are to be moved.  */  
   FailedBin:string,
      /**  Indicator of user's request to create a Corrective Action.  */  
   CreateCorAct:boolean,
      /**  Issue To specifies where the quantity that passed should be issued. For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  */  
   PassedIssueTo:string,
      /**  Indicates whether or not the part is complete when it is issued back to the job. If the part is complete (not taken apart) when it is returned to the job, this is YES This field is available if PassedIssueTo is Job Assembly (ASM) or Job Material (MTL).  */  
   PassedIssuedComplete:boolean,
      /**  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  */  
   FailedReasonCode:string,
      /**  Flag to indicate whether serial numbers will be required during inspection processing.  */  
   EnforceSerialNumCount:boolean,
      /**  PartNum of Job Assembly passed part is to be issued to.  */  
   PassedJobPartNum:string,
      /**  Description of Job Assembly passed part is to be issued to.  */  
   PassedJobPartDesc:string,
      /**  This is how many of the assemblies are required to produce the END ITEM.  */  
   PassedJobQty:number,
      /**  Unique ID field to establish relationship with InspProcList  */  
   xID:string,
   FailedBinDescription:string,
   FailedReasonDescription:string,
   FailedWarehouseDescription:string,
   PassedBinDescription:string,
   PassedWarehouseDescription:string,
      /**  Quantity of the material to be scrapped.  */  
   DimQuantity:number,
      /**  = PassedQty * DimConvFactor  */  
   DimPassedQty:number,
      /**  = FailedQty * DimConvFactor  */  
   DimFailedQty:number,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   AcceptUM:string,
      /**  The Quantity field converted to the UOM defined in the job material  */  
   TranQty:number,
      /**  The UOM defined in the job material  */  
   TranUOM:string,
   RequiredQtyUOM:string,
      /**  To enable/disable Serial Tracking options in UI screens.  */  
   EnableSerialTracking:boolean,
   InspDataRequired:boolean,
   InspDataEntered:boolean,
      /**  It is used to print Inventory Movement after processing.  */  
   Done:boolean,
      /**  Failed Legal Number  */  
   FailedLegalNumber:string,
   FailedLegalNumberID:string,
      /**  Failed Legal Number Message  */  
   FailedLegalNumberMsg:string,
      /**  Failed Transaction Document Type  */  
   FailedTranDocTypeID:string,
      /**  Passed Transaction Document Type  */  
   PassedTranDocTypeID:string,
      /**  Passed Legal Number  */  
   PassedLegalNumber:string,
      /**  Passed Legal Number ID  */  
   PassedLegalNumberID:string,
      /**  Passed Legal Number Message  */  
   PassedLegalNumberMsg:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PassedPCID:string,
   FailedPCID:string,
   BitFlag:number,
   BinNumDescription:string,
   DMRNumPartDescription:string,
   InspectorIDName:string,
   JobNumPartDescription:string,
   OpCodeOpDesc:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumAttrClassID:string,
   ToBinNumDescription:string,
   VendorNumAddress1:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumVendorID:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumState:string,
   VendorNumCurrencyCode:string,
   VendorNumTermsCode:string,
   VendorNumName:string,
   VendorNumZIP:string,
   VendorNumCity:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspProcListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quantity of the material to be scrapped.  */  
   Quantity:number,
      /**  Scrap reason code.  */  
   ReasonCode:string,
      /**  Job Number of the JobAsmbl record.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  The field that identifies the Part.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  */  
   TrnTyp:string,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  */  
   EntryPerson:string,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The operation sequence of the Job/Assembly.  */  
   OprSeq:number,
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   DimCode:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  The ID of the machine that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  */  
   ResourceID:string,
      /**  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  */  
   ExpectedQuantity:number,
      /**  System date at time that record was created.  */  
   FirstArtSysDate:string,
      /**  Employee ID.  */  
   EmpID:string,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  */  
   VendorID:string,
      /**  Receipt date.  */  
   ReceiptDate:string,
      /**  Return Material Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  A unique number for the transaction.  Auto increment.  */  
   NonConfTranID:number,
      /**  RowID of related NonConf record  */  
   NonConfRowIdent:string,
      /**  RowId of related First Art record  */  
   FirstArtRowIdent:string,
      /**  RowId of related RcvDtl record  */  
   RcvDtlRowIdent:string,
      /**  RowId of related RMARecpt record  */  
   RMARecptRowIdent:string,
      /**  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  */  
   SeqNum:number,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
   RMAReceipt:number,
      /**  Unique ID field to establish relationship between InspProcList and child tables InspFirstArt, InspNonConf, InspRcpt  */  
   xID:string,
      /**  Description of the source of the item to be inspected: Operations,First Articles,Inventory,Material,PO Receipts,RMAs  */  
   TrnTypDescription:string,
   EmpIDFirstName:string,
   EmpIDLastName:string,
   EmpIDName:string,
   InspectorIDName:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   UOM:string,
   InspDataEntered:boolean,
   InspDataRequired:boolean,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   AQMNCMNum:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PCID:string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspProcessingTableset{
   InspProcList:Erp_Tablesets_InspProcListRow[],
   InspFirstArt:Erp_Tablesets_InspFirstArtRow[],
   InspNonConf:Erp_Tablesets_InspNonConfRow[],
   InspRcpt:Erp_Tablesets_InspRcptRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   SupplierXRef:Erp_Tablesets_SupplierXRefRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InspRcptRow{
      /**  Company Indentifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Supplier master file.  */  
   VendorNum:number,
      /**  The Supplier purchase point ID.  */  
   PurPoint:string,
      /**  Supplier Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   AttributeValueSeq:number,
      /**  Dynamic Attribute Value Set ID for this receipt detail.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Receipt quantity in our unit of measure for this attribute set.  */  
   OurQty:number,
      /**  Indicates whether the Attribute Value was auto-generated by the system.  */  
   AutoGenerated:boolean,
      /**  Supplier selling Unit of Measure.  */  
   PUM:string,
      /**  Quantity received against a purchase order in the Supplier unit of measure.  */  
   VendorQty:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   InspectionPending:boolean,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   InspectionReq:boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  Date when item was inspected.  */  
   InspectedDate:string,
      /**  Time of day when inspection transaction was recorded.  */  
   InspectedTime:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  Unique ID field to establish relationship with InspProcList  */  
   xID:string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   AcceptUM:string,
      /**  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  */  
   AQMNCMNum:string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   AssemblySeq:number,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BinNum:string,
      /**  Indicator of user's request to create a Corrective Action.  */  
   CreateCorAct:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  = FailedQty * DimConvFactor  */  
   DimFailedQty:number,
      /**  = OurQty * DimConvFactor  */  
   DimOurQty:number,
      /**  = PassedQty * DimConvFactor  */  
   DimPassedQty:number,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  It is used to print Inventory Movement after processing.  */  
   Done:boolean,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**  Flag to indicate whether serial numbers will be required during inspection processing.  */  
   EnforceSerialNumCount:boolean,
      /**  Location to which failed items are to be moved.  */  
   FailedBin:string,
   FailedBinDescription:string,
      /**  Failed Legal Number  */  
   FailedLegalNumber:string,
      /**  Failed Legal Number ID  */  
   FailedLegalNumberID:string,
      /**  Failed Legal Number Message  */  
   FailedLegalNumberMsg:string,
      /**  Indicator of user's request to create a MtlQueue for failed items.  */  
   FailedMove:boolean,
      /**  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  */  
   FailedReasonCode:string,
   FailedReasonDescription:string,
      /**  Failed Transaction Document Type  */  
   FailedTranDocTypeID:string,
      /**  Location to which failed items are to be moved.  */  
   FailedWarehouseCode:string,
   FailedWarehouseDescription:string,
      /**  Comments on the items failing inspection.  */  
   FldCommentText:string,
   InspDataEntered:boolean,
   InspDataRequired:boolean,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   Invoiced:boolean,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   InvoiceLine:number,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   InvoiceNum:string,
      /**  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this material requirement?"  */  
   IsOkToCloseJobMtl:boolean,
      /**  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this subcontract operation?"  */  
   IsOkToCloseSubContract:boolean,
      /**  Holds user's response to the question: "The Job Material requirement is Closed...  do you really want it reopened?"  */  
   IsOkToReopenJobMtl:boolean,
      /**  Holds user's response to the question: "The Subcontract operation is complete...  do you really want it reopened?"  */  
   IsOkToReopenSubContract:boolean,
      /**  Holds user's response to the question: "Serial numbers assigned to Job Subcontracts are not tracked.  The Serial Numbers that have been assigned to this receipt will be deselected.  Are you sure this receipt is to a Job Subcontract?"  */  
   IsOkToUnassignSerNums:boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   IssuedComplete:boolean,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   JobNum:string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   JobSeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   JobSeqType:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  Lot Number  */  
   LotNum:string,
      /**  The material burden rate for this part.  */  
   MtlBurRate:number,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   NonConformnce:boolean,
      /**  Number of labels  */  
   NumLabels:number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   OurMtlBurUnitCost:number,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   OurUnitCost:number,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   PartNum:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
      /**  Location to which passed items are to be moved.  */  
   PassedBin:string,
   PassedBinDescription:string,
      /**  Issue To specifies where the quantity that passed should be issued.  For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  */  
   PassedIssueTo:string,
   PassedJobIUM:string,
      /**  Description of Job Assembly passed part is to be issued to.  */  
   PassedJobPartDesc:string,
      /**  PartNum of Job Assembly passed part is to be issued to.  */  
   PassedJobPartNum:string,
      /**  This is how many of the assemblies are required to produce the END ITEM.  */  
   PassedJobQty:number,
      /**  Passed Legal Number  */  
   PassedLegalNumber:string,
      /**  Passed Legal Number ID  */  
   PassedLegalNumberID:string,
      /**  Passed Legal Number Message  */  
   PassedLegalNumberMsg:string,
      /**  Indicator of user's request to create a MtlQueue for passed items.  */  
   PassedMove:boolean,
      /**  Passed Transaction Document Type  */  
   PassedTranDocTypeID:string,
      /**  Location to which passed items are to be moved  */  
   PassedWarehouseCode:string,
   PassedWarehouseDescription:string,
      /**  Plant  */  
   Plant:string,
      /**  Contains comments about over all  purchase order. These will be printed on the purchase order.  */  
   POHeaderComment:string,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Comments on items passing inspection.  */  
   PsdCommentText:string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   ReasonCode:string,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers. - This description was for when InspRcpt was tied to RcvDtl  */  
   ReceiptDate:string,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   ReceiptType:string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   ReceivedComplete:boolean,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   ReceivedTo:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
   RefDisplayAccount:string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   TotCostVariance:number,
      /**  The Quantity field converted to the UOM defined in the job material  */  
   TranQty:number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   TranReference:string,
      /**  The UOM defined in the job material  */  
   TranUOM:string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   VendorUnitCost:number,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   VenPartNum:string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   WareHouseCode:string,
      /**  Weight  */  
   Weight:number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Was a link column on RcvDtl.  */  
   BinNumDescription:string,
      /**  Was a link column on RcvDtl.  */  
   DimCodeDimCodeDescription:string,
      /**  Was a link column on RcvDtl.  */  
   JobNumPartDescription:string,
      /**  Was a link column on RcvDtl.  */  
   PartNumAttrClassID:string,
      /**  Was a link column on RcvDtl.  */  
   PartNumIUM:string,
      /**  Was a link column on RcvDtl.  */  
   PartNumPartDescription:string,
      /**  Was a link column on RcvDtl.  */  
   PartNumPricePerCode:string,
      /**  Was a link column on RcvDtl.  */  
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
      /**  Was a link column on RcvDtl.  */  
   PartNumTrackDimension:boolean,
      /**  Was a link column on RcvDtl.  */  
   POLineLineDesc:string,
      /**  Was a link column on RcvDtl.  */  
   POLinePartNum:string,
      /**  Was a link column on RcvDtl.  */  
   POLineVenPartNum:string,
      /**  Was a link column on RcvDtl.  */  
   WarehouseCodeDescription:string,
   PCID:string,
   FailedPCID:string,
   PassedPCID:string,
   BitFlag:number,
   InspectorIDName:string,
   VendorNumTermsCode:string,
   VendorNumAddress3:string,
   VendorNumState:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   VendorNumVendorID:string,
   VendorNumCity:string,
   VendorNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SupplierXRefRow{
   Company:string,
   MfgID:string,
   MfgName:string,
   MfgNum:number,
   MfgPartNum:string,
   PartNum:string,
   POReference:boolean,
   Receipt:boolean,
   VendNum:number,
   VendPartNum:string,
   Invoice:boolean,
      /**  RcvXRefNum  */  
   RcvXRefNum:number,
   Inspected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param pcTranID
   */  
export interface GetByID_input{
      /**  The TranID of the NonConformance.  */  
   pcTranID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_InspProcessingTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param pText
   */  
export interface GetDateUser_input{
   pText:string,
}

export interface GetDateUser_output{
parameters : {
      /**  output parameters  */  
   pText:string,
}
}

   /** Required : 
      @param ds
      @param inspectionType
   */  
export interface GetFailedLegalNumGenOpts_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  The type of inspection: Inventory, Material, Operation, Receipt  */  
   inspectionType:string,
}

export interface GetFailedLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param pcJobNum
      @param piAssemblySeq
      @param piOprSeq
      @param pcResourceID
      @param piSeqNum
   */  
export interface GetFirstArtByID_input{
      /**  The JobNum of the First Article.  */  
   pcJobNum:string,
      /**  The AssemblySeq of the First Article.  */  
   piAssemblySeq:number,
      /**  The OprSeq of the First Article.  */  
   piOprSeq:number,
      /**  The ResourceID of the First Article.  */  
   pcResourceID:string,
      /**  The SeqNum of the First Article.  */  
   piSeqNum:number,
}

export interface GetFirstArtByID_output{
   returnObj:Erp_Tablesets_InspProcessingTableset[],
}

   /** Required : 
      @param pcInspRcptRowIdent
      @param ds
   */  
export interface GetInspRcptSelectedSerialNumbers_input{
      /**  Input RowIdent field  of InspRcpt datatable  */  
   pcInspRcptRowIdent:string,
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface GetInspRcptSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
      @param ipSource
   */  
export interface GetInspResultsPassFail_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf", "Receipt", "FirstArt"  */  
   ipSource:string,
}

export interface GetInspResultsPassFail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   totPassed:number,
   totFailed:number,
   inspDataEntered:boolean,
}
}

   /** Required : 
      @param inspectionType
      @param company
      @param nonConfTranID
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param tranType
   */  
export interface GetMtlQueueSeqValue_input{
   inspectionType:string,
   company:string,
   nonConfTranID:number,
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   tranType:string,
}

export interface GetMtlQueueSeqValue_output{
   returnObj:number,
}

   /** Required : 
      @param ipNonConfID
      @param ipDMRNum
      @param ipPassedIssueTo
   */  
export interface GetNonConfPartTranPKs_input{
      /**  ipNonConfID  */  
   ipNonConfID:number,
      /**  DMR number  */  
   ipDMRNum:number,
      /**  PassedIssueTo  */  
   ipPassedIssueTo:string,
}

export interface GetNonConfPartTranPKs_output{
parameters : {
      /**  output parameters  */  
   partTranPKs:string,
}
}

   /** Required : 
      @param ds
      @param inspectionType
   */  
export interface GetPassedLegalNumGenOpts_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  The type of inspection: Inventory, Material, Operation, Receipt  */  
   inspectionType:string,
}

export interface GetPassedLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param piVendorNum
      @param pcPurPoint
      @param pcPackSlip
      @param piPackLine
   */  
export interface GetReceiptByID_input{
      /**  The VendorNum of the Receipt.  */  
   piVendorNum:number,
      /**  The PurPoint of the Receipt.  */  
   pcPurPoint:string,
      /**  The PackSlip of the Receipt.  */  
   pcPackSlip:string,
      /**  The PackLine of the Receipt.  */  
   piPackLine:number,
}

export interface GetReceiptByID_output{
   returnObj:Erp_Tablesets_InspProcessingTableset[],
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipPackLine
      @param ipDMRNum
      @param ipPassedIssueTo
   */  
export interface GetReceiptPartTranPKs_input{
      /**  Vendor number  */  
   ipVendorNum:number,
      /**  PurPoint  */  
   ipPurPoint:string,
      /**  PackSlip  */  
   ipPackSlip:string,
      /**  PackLine  */  
   ipPackLine:number,
      /**  DMR number  */  
   ipDMRNum:number,
      /**  PassedIssueTo  */  
   ipPassedIssueTo:string,
}

export interface GetReceiptPartTranPKs_output{
parameters : {
      /**  output parameters  */  
   partTranPKs:string,
}
}

   /** Required : 
      @param tranType
      @param whereClauseInspProcList
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsLP_input{
      /**  Indicates the Transaction Type of the items to be retrieved. Valid values: ALL = All items, OPR = Job Operation, MTL = Job Material, INV = Inventory, FAR = First Article, POR = PO Receipt, and RMA = RMA  */  
   tranType:string,
      /**  Includes the additional Where conditions to be applied to the result set, especially the PartNum condition.  */  
   whereClauseInspProcList:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsLP_output{
   returnObj:Erp_Tablesets_InspProcessingTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param plOperation
      @param plMaterial
      @param plInventory
      @param plFirstArt
      @param plReceipt
      @param plRMA
      @param pcInspectorID
      @param pcCutOffDate
      @param whereClauseNonConf
      @param whereClauseFirstArt
      @param whereClauseRcvDtl
      @param whereClauseRMA
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param whereClauseInspProcList
      @param sortBy
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  If TRUE, include items that were sent to Inspection from a Job Operation.  */  
   plOperation:boolean,
      /**  If TRUE, include items that were sent to Inspection from a Job Material.  */  
   plMaterial:boolean,
      /**  If TRUE, include items that were sent to Inspection from Inventory.  */  
   plInventory:boolean,
      /**  If TRUE, include items that were sent to Inspection from a First Article.  */  
   plFirstArt:boolean,
      /**  If TRUE, include items that were sent to Inspection from a PO or SubContract receipt.  */  
   plReceipt:boolean,
      /**  If TRUE, include items that were sent to Inspection from an RMA.  */  
   plRMA:boolean,
      /**  (optional) The Inspector ID typed in by the user.  */  
   pcInspectorID:string,
      /**  (optional) Cut Off Date .  */  
   pcCutOffDate:string,
      /**  (optional)Additional Where conditions for NonConf table.  */  
   whereClauseNonConf:string,
      /**  (optional)Additional Where conditions for FirstArt table.  */  
   whereClauseFirstArt:string,
      /**  (optional)Additional Where conditions for RcvDtl table.  */  
   whereClauseRcvDtl:string,
      /**  (optional)Additional Where conditions for RMAHead table.  */  
   whereClauseRMA:string,
      /**  (optional)Additional Where conditions for SelectedSerialNumbers table.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  (optional)Additional Where conditions for SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  (optional)Additional Where conditions to be applied to result set.  */  
   whereClauseInspProcList:string,
      /**  Sort By selected in search  */  
   sortBy:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_InspProcessingTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param pcInspNonConfRowIdent
      @param ds
   */  
export interface GetSelectedSerialNumbers_input{
      /**  Input RowIdent field  of InspNonConf datatable  */  
   pcInspNonConfRowIdent:string,
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface GetSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
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
export interface InspectFirstArt_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectFirstArt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectInventory2_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectInventory2_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   message:string,
   iDMRNum:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectInventory_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectInventory_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   iDMRNum:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectMaterial2_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectMaterial2_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   message:string,
   iDMRNum:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectMaterial_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectMaterial_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   iDMRNum:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectOperation2_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectOperation2_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   message:string,
   iDMRNum:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectOperation_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectOperation_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   iDMRNum:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectReceipt2_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectReceipt2_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   message:string,
   iDMRNum:number,
   iNonConfID:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface InspectReceipt_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface InspectReceipt_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   iDMRNum:number,
   iNonConfID:number,
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
      @param pcSource
      @param piProposedAssemblySeq
   */  
export interface OnChangeAssemblySeq_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf" or "Receipt"  */  
   pcSource:string,
      /**  The new proposed Assembly Seq value  */  
   piProposedAssemblySeq:number,
}

export interface OnChangeAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
      @param pdInspectedQuantity
   */  
export interface OnChangeFAInspectedQty_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  The new proposed Inspected Quantity value  */  
   pdInspectedQuantity:number,
}

export interface OnChangeFAInspectedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcWarningMsg:string,
}
}

   /** Required : 
      @param ds
      @param pcSource
      @param pdProposedFailedQty
   */  
export interface OnChangeFailedQty_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf" or "Receipt"  */  
   pcSource:string,
      /**  The new proposed Failed Quantity value  */  
   pdProposedFailedQty:number,
}

export interface OnChangeFailedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   infoMsg:string,
}
}

   /** Required : 
      @param ds
      @param pcSource
      @param plProposedIssuedComplete
   */  
export interface OnChangeIssueComplete_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf" or "Receipt"  */  
   pcSource:string,
      /**  The new proposed Issued Complete value  */  
   plProposedIssuedComplete:boolean,
}

export interface OnChangeIssueComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcWarningMsg:string,
   pcResponseField:string,
}
}

   /** Required : 
      @param ds
      @param pcSource
      @param pcProposedJobNum
   */  
export interface OnChangeJobNum_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf" or "Receipt"  */  
   pcSource:string,
      /**  The new proposed Job Number value  */  
   pcProposedJobNum:string,
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcWarningMsg:string,
}
}

   /** Required : 
      @param ds
      @param piProposedJobSeq
   */  
export interface OnChangeJobSeq_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  The new proposed Job Sequence Number value  */  
   piProposedJobSeq:number,
}

export interface OnChangeJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcWarningMsg:string,
}
}

   /** Required : 
      @param ds
      @param piProposedMtlSeq
   */  
export interface OnChangeMtlSeq_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  The new proposed Material Sequence Number value  */  
   piProposedMtlSeq:number,
}

export interface OnChangeMtlSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcWarningMsg:string,
}
}

   /** Required : 
      @param pcid
      @param pCallProcess
      @param ds
   */  
export interface OnChangePCID_input{
   pcid:string,
   pCallProcess:string,
   ds:Erp_Tablesets_InspProcessingTableset[],
}

export interface OnChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
      @param pcSource
      @param pcProposedIssueTo
   */  
export interface OnChangePassedIssueTo_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf" or "Receipt"  */  
   pcSource:string,
      /**  The new proposed PassedIssueTo value  */  
   pcProposedIssueTo:string,
}

export interface OnChangePassedIssueTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ds
      @param pcSource
      @param pdProposedPassedQty
   */  
export interface OnChangePassedQty_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
      /**  "NonConf" or "Receipt"  */  
   pcSource:string,
      /**  The new proposed Passed Quantity value  */  
   pdProposedPassedQty:number,
}

export interface OnChangePassedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
   infoMsg:string,
}
}

   /** Required : 
      @param ds
      @param pcSource
      @param pcWhseType
      @param pdProposedWhse
   */  
export interface OnChangePassedWhse_input{
   ds:Erp_Tablesets_InspProcessingTableset[],
   pcSource:string,
   pcWhseType:string,
   pdProposedWhse:string,
}

export interface OnChangePassedWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspProcessingTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ipSerialNo
      @param ipVendorNum
      @param ipJobNum
      @param ipAsmSeq
      @param ipSubOprSeq
      @param ipPackSlip
      @param ipPackLine
      @param ipReceivedTo
      @param ipJobSeqType
      @param isRcpt
   */  
export interface ValidateSN_input{
      /**  Part Number  */  
   ipPartNum:string,
      /**  Serial Number  */  
   ipSerialNo:string,
      /**  Vendor Number  */  
   ipVendorNum:number,
      /**  Job Number  */  
   ipJobNum:string,
      /**  Vendor Number  */  
   ipAsmSeq:number,
      /**  Job Operation Number  */  
   ipSubOprSeq:number,
      /**  Pack Slip  */  
   ipPackSlip:string,
      /**  Pack Slip Line  */  
   ipPackLine:number,
      /**  Received To  */  
   ipReceivedTo:string,
      /**  Job Sequence type  */  
   ipJobSeqType:string,
      /**  Indicates whether the Serial Numbers are being entered for inspection from Receipt  */  
   isRcpt:boolean,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
}
}

   /** Required : 
      @param ipTranDocTypeID
   */  
export interface ValidateTranDocType_input{
      /**  Transaction Document Type ID to be validated  */  
   ipTranDocTypeID:string,
}

export interface ValidateTranDocType_output{
}

