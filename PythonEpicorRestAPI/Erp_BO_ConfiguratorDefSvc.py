import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConfiguratorDefSvc
# Description: ConfiguratorDef Business Object
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorDefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConfiguratorDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfiguratorDefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs",headers=creds) as resp:
           return await resp.json()

async def post_ConfiguratorDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfiguratorDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorDefs_Company_ConfigID(Company, ConfigID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConfiguratorDef item
   Description: Calls GetByID to retrieve the ConfiguratorDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfiguratorDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConfiguratorDefs_Company_ConfigID(Company, ConfigID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConfiguratorDef for the service
   Description: Calls UpdateExt to update ConfiguratorDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfiguratorDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs(" + Company + "," + ConfigID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConfiguratorDefs_Company_ConfigID(Company, ConfigID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConfiguratorDef item
   Description: Call UpdateExt to delete ConfiguratorDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfiguratorDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcStatusAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcStatusAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcStatusAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches",headers=creds) as resp:
           return await resp.json()

async def post_PcStatusAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcStatusAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcStatusAttches_Company_ConfigID_DrawingSeq(Company, ConfigID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcStatusAttch item
   Description: Calls GetByID to retrieve the PcStatusAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStatusAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches(" + Company + "," + ConfigID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcStatusAttches_Company_ConfigID_DrawingSeq(Company, ConfigID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcStatusAttch for the service
   Description: Calls UpdateExt to update PcStatusAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcStatusAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches(" + Company + "," + ConfigID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcStatusAttches_Company_ConfigID_DrawingSeq(Company, ConfigID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcStatusAttch item
   Description: Call UpdateExt to delete PcStatusAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcStatusAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches(" + Company + "," + ConfigID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcAudits(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcAudits items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcAudits
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcAuditRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits",headers=creds) as resp:
           return await resp.json()

async def post_PcAudits(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcAudits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcAuditRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcAuditRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcAudits_Company_PartNum_RevisionNum_ChgDate_ChgTime(Company, PartNum, RevisionNum, ChgDate, ChgTime, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcAudit item
   Description: Calls GetByID to retrieve the PcAudit item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcAudit
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param ChgDate: Desc: ChgDate   Required: True   Allow empty value : True
      :param ChgTime: Desc: ChgTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcAuditRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits(" + Company + "," + PartNum + "," + RevisionNum + "," + ChgDate + "," + ChgTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcAudits_Company_PartNum_RevisionNum_ChgDate_ChgTime(Company, PartNum, RevisionNum, ChgDate, ChgTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcAudit for the service
   Description: Calls UpdateExt to update PcAudit. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcAudit
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param ChgDate: Desc: ChgDate   Required: True   Allow empty value : True
      :param ChgTime: Desc: ChgTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcAuditRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits(" + Company + "," + PartNum + "," + RevisionNum + "," + ChgDate + "," + ChgTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcAudits_Company_PartNum_RevisionNum_ChgDate_ChgTime(Company, PartNum, RevisionNum, ChgDate, ChgTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcAudit item
   Description: Call UpdateExt to delete PcAudit item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcAudit
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param ChgDate: Desc: ChgDate   Required: True   Allow empty value : True
      :param ChgTime: Desc: ChgTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits(" + Company + "," + PartNum + "," + RevisionNum + "," + ChgDate + "," + ChgTime + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDocRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcDocRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDocRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDocRulesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules",headers=creds) as resp:
           return await resp.json()

async def post_PcDocRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDocRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcDocRules_Company_ConfigID_RuleSeq(Company, ConfigID, RuleSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDocRule item
   Description: Calls GetByID to retrieve the PcDocRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDocRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules(" + Company + "," + ConfigID + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcDocRules_Company_ConfigID_RuleSeq(Company, ConfigID, RuleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcDocRule for the service
   Description: Calls UpdateExt to update PcDocRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDocRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules(" + Company + "," + ConfigID + "," + RuleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcDocRules_Company_ConfigID_RuleSeq(Company, ConfigID, RuleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcDocRule item
   Description: Call UpdateExt to delete PcDocRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDocRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules(" + Company + "," + ConfigID + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDocRulesExprs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcDocRulesExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDocRulesExprs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDocRulesExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs",headers=creds) as resp:
           return await resp.json()

async def post_PcDocRulesExprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDocRulesExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcDocRulesExprs_Company_ConfigID_RuleSeq_TypeCode_SeqNum(Company, ConfigID, RuleSeq, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDocRulesExpr item
   Description: Calls GetByID to retrieve the PcDocRulesExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDocRulesExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs(" + Company + "," + ConfigID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcDocRulesExprs_Company_ConfigID_RuleSeq_TypeCode_SeqNum(Company, ConfigID, RuleSeq, TypeCode, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcDocRulesExpr for the service
   Description: Calls UpdateExt to update PcDocRulesExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDocRulesExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs(" + Company + "," + ConfigID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcDocRulesExprs_Company_ConfigID_RuleSeq_TypeCode_SeqNum(Company, ConfigID, RuleSeq, TypeCode, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcDocRulesExpr item
   Description: Call UpdateExt to delete PcDocRulesExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDocRulesExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs(" + Company + "," + ConfigID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDocVars(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcDocVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDocVars
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDocVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars",headers=creds) as resp:
           return await resp.json()

async def post_PcDocVars(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDocVars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcDocVars_Company_ConfigID_VarNum(Company, ConfigID, VarNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDocVar item
   Description: Calls GetByID to retrieve the PcDocVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDocVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param VarNum: Desc: VarNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars(" + Company + "," + ConfigID + "," + VarNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcDocVars_Company_ConfigID_VarNum(Company, ConfigID, VarNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcDocVar for the service
   Description: Calls UpdateExt to update PcDocVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDocVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param VarNum: Desc: VarNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars(" + Company + "," + ConfigID + "," + VarNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcDocVars_Company_ConfigID_VarNum(Company, ConfigID, VarNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcDocVar item
   Description: Call UpdateExt to delete PcDocVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDocVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param VarNum: Desc: VarNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars(" + Company + "," + ConfigID + "," + VarNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs",headers=creds) as resp:
           return await resp.json()

async def post_PcInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName(Company, ConfigID, InputName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInput item
   Description: Calls GetByID to retrieve the PcInput item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInput
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputs_Company_ConfigID_InputName(Company, ConfigID, InputName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInput for the service
   Description: Calls UpdateExt to update PcInput. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInput
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputs_Company_ConfigID_InputName(Company, ConfigID, InputName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInput item
   Description: Call UpdateExt to delete PcInput item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInput
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcStrComps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcStrComps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcStrComps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStrCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps",headers=creds) as resp:
           return await resp.json()

async def post_PcStrComps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcStrComps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcStrComps_Company_ConfigID_PosOrder_CompName(Company, ConfigID, PosOrder, CompName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcStrComp item
   Description: Calls GetByID to retrieve the PcStrComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStrComp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PosOrder: Desc: PosOrder   Required: True
      :param CompName: Desc: CompName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps(" + Company + "," + ConfigID + "," + PosOrder + "," + CompName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcStrComps_Company_ConfigID_PosOrder_CompName(Company, ConfigID, PosOrder, CompName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcStrComp for the service
   Description: Calls UpdateExt to update PcStrComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcStrComp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PosOrder: Desc: PosOrder   Required: True
      :param CompName: Desc: CompName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps(" + Company + "," + ConfigID + "," + PosOrder + "," + CompName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcStrComps_Company_ConfigID_PosOrder_CompName(Company, ConfigID, PosOrder, CompName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcStrComp item
   Description: Call UpdateExt to delete PcStrComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcStrComp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PosOrder: Desc: PosOrder   Required: True
      :param CompName: Desc: CompName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps(" + Company + "," + ConfigID + "," + PosOrder + "," + CompName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcTargetEntities(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcTargetEntities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcTargetEntities
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcTargetEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities",headers=creds) as resp:
           return await resp.json()

async def post_PcTargetEntities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcTargetEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcTargetEntities_Company_ConfigID_TableName(Company, ConfigID, TableName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcTargetEntity item
   Description: Calls GetByID to retrieve the PcTargetEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcTargetEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities(" + Company + "," + ConfigID + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcTargetEntities_Company_ConfigID_TableName(Company, ConfigID, TableName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcTargetEntity for the service
   Description: Calls UpdateExt to update PcTargetEntity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcTargetEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities(" + Company + "," + ConfigID + "," + TableName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcTargetEntities_Company_ConfigID_TableName(Company, ConfigID, TableName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcTargetEntity item
   Description: Call UpdateExt to delete PcTargetEntity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcTargetEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities(" + Company + "," + ConfigID + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcStatus, whereClausePcStatusAttch, whereClausePcAudit, whereClausePcDocRules, whereClausePcDocRulesExpr, whereClausePcDocVar, whereClausePcInputs, whereClausePcStrComp, whereClausePcTargetEntity, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcStatus=" + whereClausePcStatus
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcStatusAttch=" + whereClausePcStatusAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcAudit=" + whereClausePcAudit
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcDocRules=" + whereClausePcDocRules
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcDocRulesExpr=" + whereClausePcDocRulesExpr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcDocVar=" + whereClausePcDocVar
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputs=" + whereClausePcInputs
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcStrComp=" + whereClausePcStrComp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcTargetEntity=" + whereClausePcTargetEntity
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(configID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "configID=" + configID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetFormatString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFormatString
   Description: Get the format string for a PcInput
   OperationID: GetFormatString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFormatString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormatString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInputPossibleValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInputPossibleValues
   Description: Get the values from Radio and DropDownList
   OperationID: GetInputPossibleValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInputPossibleValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInputPossibleValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailInputs
   Description: Get the available inputs that may be used to build smart string.
   OperationID: GetAvailInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildSampleSmartString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildSampleSmartString
   Description: Updates the PcStatus Sample Smart String when the smart string parameters are changed.
   OperationID: BuildSampleSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildSampleSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildSampleSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SalesKitConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SalesKitConfiguration
   Description: If a partplant record is available for the current plant then check the SourceType
If not partplant available then check the typecode on the part record.
   OperationID: SalesKitConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesKitConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesKitConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SmartStringMoveDown(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SmartStringMoveDown
   Description: Move a smart string input down in the available inputs list
   OperationID: SmartStringMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SmartStringMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SmartStringMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SmartStringMoveUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SmartStringMoveUp
   Description: Move a smart string input up in the selected inputs list
   OperationID: SmartStringMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SmartStringMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SmartStringMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SyncRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SyncRevision
   Description: This method synchronizes the part revision approval flag when the PcStatus.Approved
flag changes
   OperationID: SyncRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SyncRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyncRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePcStruct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePcStruct
   Description: Update PcStruct records with new display sequence
   OperationID: UpdatePcStruct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePcStruct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePcStruct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateConfigSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateConfigSequence
   Description: Called prior to testing input/rules to generate
           configuration sequence records
   OperationID: GenerateConfigSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateConfigSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateConfigSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteConfigSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteConfigSequence
   Description: Called after testing inputs/rules to delete configuration
           sequence records
   OperationID: DeleteConfigSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteConfigSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteConfigSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSpecRevs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSpecRevs
   Description: Get the valid specification revisions
   OperationID: GetSpecRevs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSpecRevs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSpecRevs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLinkedParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLinkedParts
   Description: Get a list of parts that are related to this configuration id
   OperationID: GetLinkedParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLinkedParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkedParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckValidRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckValidRevision
   Description: verify the selected revision is valid
   OperationID: CheckValidRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckValidRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConfigAndGetType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConfigAndGetType
   Description: Check if Configuration exists and return ConfigType in case exist
   OperationID: CheckConfigAndGetType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfigAndGetType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfigAndGetType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRevisions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevisions
   Description: Get a list of revisions that are related to the selected part number
   OperationID: GetRevisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEffectiveRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEffectiveRevision
   Description: Get the latest effective revision for the related part number and configuration id
   OperationID: GetEffectiveRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEffectiveRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEffectiveRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetConfigurationOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConfigurationOptions
   Description: Get the valid options that are used for populating configuration design options.  This will populate the ConfigPartCreateMethod, ConfigSmartStringStyle,
   OperationID: GetConfigurationOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConfigurationOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfigurationOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTargetTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTargetTables
   Description: Get the valid table options for config type
   OperationID: GetTargetTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PromptForPassword(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PromptForPassword
   Description: This method checks the BMSyst record to see if a password should prompted for and then
validated by the ValidatePassword method in UserFile BO.  Run this before SyncRevision method is called.
   OperationID: PromptForPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PromptForPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptForPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangingEntConf(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangingEntConf
   Description: This methods checks to see if any enterprise configurator specific settings
have been created.  If so then a message should be displayed prior to unchecking
the enterprise configurator checkbox
   OperationID: ChangingEntConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingEntConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingEntConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePcStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePcStatus
   Description: Create a new configuration for a Part Revision
   OperationID: CreatePcStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePcStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePcStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSequenceForTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSequenceForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
ALL ALTERNATES OF THE PARTREVISION WILL BE RETURNED if ipcomplete is true
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
   OperationID: GetSequenceForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSequenceForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSequenceForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshSubConf(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshSubConf
   Description: This method rebuilds the configurator sequence. It's
a compilation of all sub configured parts defined in the method of manufacture
for the parent configured part.
   OperationID: RefreshSubConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshSubConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshSubConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshConfiguratorSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshConfiguratorSequence
   Description: This method rebuilds the configurator sequence and updates the PcValueHead table to apply the new sequence to existing configurations.
   OperationID: RefreshConfiguratorSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshConfiguratorSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshConfiguratorSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshPcStatusBeforeDisapprove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshPcStatusBeforeDisapprove
   Description: Refresh PcStatus when RegenConfig is True before disapproving in case the record has been changed by the Regenerate Configurator process already.
   OperationID: RefreshPcStatusBeforeDisapprove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshPcStatusBeforeDisapprove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshPcStatusBeforeDisapprove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocRulesMoveDown(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocRulesMoveDown
   Description: Move a document rule down in the order of configuration rules.
   OperationID: DocRulesMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocRulesMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocRulesMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocRulesMoveUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocRulesMoveUp
   Description: Move a document rule up in the order of configuration rules.
   OperationID: DocRulesMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocRulesMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocRulesMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeConfigType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeConfigType
   Description: The default value for Product Configurator types is true for displaying the summary screen.  For all other types it is false because it is not allowed.
   OperationID: OnChangeConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttrClassID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttrClassID
   Description: Validate if exists the Part Attribute Class selected and if the Inputs have attributes assigned.
   OperationID: OnChangeAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedDocRuleCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedDocRuleCompany
   Description: Change Company when click check boxes for Multi-Company or Local company
Must clear the list of companies in case already selected in picker list
   OperationID: OnChangedDocRuleCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedDocRuleCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDocRuleCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcDocRulesExprExprType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcDocRulesExprExprType
   Description: This method is executed when changing the ExprType column of PcDocRulesExpr, it is used to clear all fields related with
action expression
   OperationID: OnChangedPcDocRulesExprExprType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocRulesExprExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocRulesExprExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcDocRulesRuleType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcDocRulesRuleType
   Description: This method is executed when changing the RuleType column of PcDocRules, it is used to clear all fields related with
condition expression
   OperationID: OnChangedPcDocRulesRuleType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocRulesRuleType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocRulesRuleType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePcDocRulesExprLValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePcDocRulesExprLValue
   Description: This method is executed when changing the LValue column of PcDocRulesExpr, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcDocRulesExprLValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcDocRulesExprLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcDocRulesExprLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePcDocRulesLValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePcDocRulesLValue
   Description: This method is executed when changing the LValue column of PcDocRules, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcDocRulesLValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcDocRulesLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcDocRulesLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcStatusRemoveLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcStatusRemoveLink
   Description: Only when Part Creation is enabled should add the part table to target entity list
   OperationID: OnChangedPcStatusRemoveLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcStatusRemoveLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcStatusRemoveLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcStatusCreatePart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcStatusCreatePart
   Description: Only when Part Creation is enabled should add the part table to target entity list
   OperationID: OnChangedPcStatusCreatePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcStatusCreatePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcStatusCreatePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePcStatusKBConfigID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePcStatusKBConfigID
   Description: On change of the CPQ Configurator ID
   OperationID: OnChangePcStatusKBConfigID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcStatusKBConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcStatusKBConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetKBConfigSearchList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetKBConfigSearchList
   Description: Get a list of CPQ Configurators
   OperationID: Get_GetKBConfigSearchList
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKBConfigSearchList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPcTargetEntityList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPcTargetEntityList
   Description: Gets a list of PcTargetEntity records based on a where clause.
   OperationID: GetPcTargetEntityList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPcTargetEntityList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPcTargetEntityList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPcTargetEntityListIncludeUD(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPcTargetEntityListIncludeUD
   Description: Gets a list of PcTargetEntity records based on a where clause.
   OperationID: GetPcTargetEntityListIncludeUD
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPcTargetEntityListIncludeUD_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPcTargetEntityListIncludeUD_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePcDocRulesDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePcDocRulesDelete
   Description: Validate if exist child record when try to delete
   OperationID: ValidatePcDocRulesDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcDocRulesDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcDocRulesDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EditorFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EditorFilter
   Description: Return filter for editor
   OperationID: EditorFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EditorFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EditorFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportConfiguration
   Description: Exports a configurator.
   OperationID: ExportConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeployToEWC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeployToEWC
   Description: Export the client side portions of the configurator for EWC to use when constructing their UI
   OperationID: DeployToEWC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeployToEWC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeployToEWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrievePcLayeredImagesForExport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrievePcLayeredImagesForExport
   Description: retrieve layered image inputs for export when advanced configurator
   OperationID: RetrievePcLayeredImagesForExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrievePcLayeredImagesForExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrievePcLayeredImagesForExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportConfiguration
   Description: Imports the Configuration records for kinetic and non kientic
   OperationID: ImportConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingPcDocVarDataType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingPcDocVarDataType
   Description: Validate variable is not being used.
   OperationID: OnChangingPcDocVarDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPcDocVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcDocVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcDocVarDataType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcDocVarDataType
   Description: Clean DataType when dataType is changed
   OperationID: OnChangedPcDocVarDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingPcDocVarVarName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingPcDocVarVarName
   Description: Validate Changing VarName
   OperationID: OnChangingPcDocVarVarName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPcDocVarVarName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcDocVarVarName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcDocVarExprType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcDocVarExprType
   Description: This method is executed when changing the ExprType column of PcDocVar, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcDocVarExprType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocVarExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocVarExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocVarMoveDown(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocVarMoveDown
   Description: Move a Variable down in the order of document variables.
   OperationID: DocVarMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocVarMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocVarMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocVarMoveUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocVarMoveUp
   Description: Move a Variable up in the order of document variables.
   OperationID: DocVarMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocVarMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocVarMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailDocVariables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailDocVariables
   Description: Get the available document variables that may be used in code editor.
   OperationID: GetAvailDocVariables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailDocVariables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailDocVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildCodeEditorInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildCodeEditorInputs
   Description: builds list of inputs used in this config that are needed by the code editor available selections panel
   OperationID: BuildCodeEditorInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCodeEditorInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCodeEditorInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeEditorOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeEditorOptions
   Description: this method populates the code editor options that are database dependent
   OperationID: GetCodeEditorOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeEditorOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeEditorOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTargetEntityColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTargetEntityColumns
   Description: retrieve TargetEntity Columns
   OperationID: GetTargetEntityColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetEntityColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetEntityColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedEntityColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedEntityColumn
   Description: validate if exists the selected entity column in the specify result set
   OperationID: OnChangedEntityColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedEntityColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedEntityColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateConfiguration
   Description: Duplicates configuration. It won't duplicate Method Rules, Method Variables, Lookup Tables (Definition), Sequence, Global Variables(Definition), Images(Definition), Memos, Change Log
   OperationID: DuplicateConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForEpicorWebClientSyncUpdates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForEpicorWebClientSyncUpdates
   Description: Call this method to determine whether or the configuration definition has changed since the last time the configurator was generated in EWC.
   OperationID: CheckForEpicorWebClientSyncUpdates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForEpicorWebClientSyncUpdates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForEpicorWebClientSyncUpdates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateEpicorWebDeployStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateEpicorWebDeployStatus
   Description: Call this method after the configuration has been successfully generated in EWC.
   OperationID: UpdateEpicorWebDeployStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateEpicorWebDeployStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateEpicorWebDeployStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestInputsPostDeployMessageToEWC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestInputsPostDeployMessageToEWC
   Description: Called when user is executed Test Inputs for an EWC configurator
   OperationID: TestInputsPostDeployMessageToEWC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestInputsPostDeployMessageToEWC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestInputsPostDeployMessageToEWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostDeployMessageToEWC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostDeployMessageToEWC
   Description: Method to call when EWC is to execute their logic to deploy a configurator to EWC and generate all of the necessary files.
   OperationID: PostDeployMessageToEWC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostDeployMessageToEWC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostDeployMessageToEWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcStatus
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcStatusAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcStatusAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatusAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatusAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatusAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcAudit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcAudit
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcAudit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcAudit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcAudit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcDocRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcDocRules
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDocRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDocRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDocRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcDocRulesExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcDocRulesExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDocRulesExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDocRulesExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDocRulesExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcDocVar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcDocVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDocVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDocVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDocVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcStrComp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcStrComp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStrComp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStrComp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStrComp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcTargetEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcTargetEntity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcTargetEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcTargetEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcTargetEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcAuditRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcAuditRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesExprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcDocRulesExprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcDocRulesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocVarRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcDocVarRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcStatusAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcStatusListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcStatusRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStrCompRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcStrCompRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcTargetEntityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcTargetEntityRow] = obj["value"]
      pass

class Erp_Tablesets_PcAuditRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ChgDate:str = obj["ChgDate"]
      """  System Date when this change was made.  """  
      self.ChgTime:int = obj["ChgTime"]
      """  System Time (seconds since midnight) of when the changes were made.  """  
      self.ChgBy:str = obj["ChgBy"]
      """  UserID who made the changes.  Not maintainable by the user.  """  
      self.ChgDescription:str = obj["ChgDescription"]
      """  Used to enter a description of the changes that were made.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.CvtChgTime:str = obj["CvtChgTime"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDocRulesExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Document Rule Sequence Number  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  Document Rule Expression  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ProcessOrder:int = obj["ProcessOrder"]
      """  ProcessOrder  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispActionString:str = obj["DispActionString"]
      self.dbTable:str = obj["dbTable"]
      self.dbField:str = obj["dbField"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDocRulesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company ID  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Document Rule Sequence Number  """  
      self.RuleString:str = obj["RuleString"]
      """  Document Rule String  """  
      self.RuleType:str = obj["RuleType"]
      """  Document Rule Type  """  
      self.CalcName:str = obj["CalcName"]
      """  Name for the calculated field  """  
      self.CalcDataType:str = obj["CalcDataType"]
      """  Calculated field data type  """  
      self.dbField:str = obj["dbField"]
      """  Database field  """  
      self.dbTable:str = obj["dbTable"]
      """  Database table  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.Comments:str = obj["Comments"]
      """  Comment  """  
      self.RuleExpr:str = obj["RuleExpr"]
      """  Document Rule Expression  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Process Sequence  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ExtCompanyList:str = obj["ExtCompanyList"]
      """  ExtCompanyList  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.dspRuleType:str = obj["dspRuleType"]
      self.EntprsConf:bool = obj["EntprsConf"]
      self.TypeCode:str = obj["TypeCode"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.CompanyName:str = obj["CompanyName"]
      self.dspdbField:str = obj["dspdbField"]
      self.dspdbTable:str = obj["dspdbTable"]
      self.MultiCompany:bool = obj["MultiCompany"]
      """  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  """  
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.DispLinkString:str = obj["DispLinkString"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDocVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.VarNum:int = obj["VarNum"]
      """  VarNum  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.VarSeq:int = obj["VarSeq"]
      """  VarSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Format:str = obj["Format"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.DispLinkString:str = obj["DispLinkString"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.ShowDistinct:bool = obj["ShowDistinct"]
      """  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  """  
      self.DesignControlType:str = obj["DesignControlType"]
      """  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoSizeList:bool = obj["AutoSizeList"]
      """  AutoSizeList  """  
      self.ListWidth:int = obj["ListWidth"]
      """  ListWidth  """  
      self.ImageSource:str = obj["ImageSource"]
      """  ImageSource  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.Content:str = obj["Content"]
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.FullInputName:str = obj["FullInputName"]
      """  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  """  
      self.ImageMapping:bool = obj["ImageMapping"]
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.InputRules:bool = obj["InputRules"]
      """  Indicates whether or not Input Rules have been defined.  """  
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.OnLaunch:str = obj["OnLaunch"]
      self.PageDisplaySeq:int = obj["PageDisplaySeq"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      """  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  """  
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ImageURL:str = obj["ImageURL"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.AllowReconPO:bool = obj["AllowReconPO"]
      """  AllowReconPO  """  
      self.CompPricingJobMethod:bool = obj["CompPricingJobMethod"]
      """  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  """  
      self.CreateRev:bool = obj["CreateRev"]
      """  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  """  
      self.DefaultECO:str = obj["DefaultECO"]
      """  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  """  
      self.GenerateMethod:bool = obj["GenerateMethod"]
      """  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.PromptForCheckout:bool = obj["PromptForCheckout"]
      """  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  """  
      self.RemoveLink:bool = obj["RemoveLink"]
      """  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.UseSavedLayout:bool = obj["UseSavedLayout"]
      """  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.CreateNewConfigID:bool = obj["CreateNewConfigID"]
      """  CreateNewConfigID  """  
      self.UseTemplatePartDefaults:bool = obj["UseTemplatePartDefaults"]
      """  UseTemplatePartDefaults  """  
      self.DefaultPartNum:str = obj["DefaultPartNum"]
      """  DefaultPartNum  """  
      self.DefaultRevisionNum:str = obj["DefaultRevisionNum"]
      """  DefaultRevisionNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  """  
      self.RecycleJobs:bool = obj["RecycleJobs"]
      """  RecycleJobs  """  
      self.ClientDeployedToEWCDate:str = obj["ClientDeployedToEWCDate"]
      """  ClientDeployedToEWCDate  """  
      self.EWCClientSyncRequired:bool = obj["EWCClientSyncRequired"]
      """  EWCClientSyncRequired  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.Kinetic:bool = obj["Kinetic"]
      """  Kinetic  """  
      self.KBConfigID:int = obj["KBConfigID"]
      """  KBConfigID  """  
      self.KBConfigDesc:str = obj["KBConfigDesc"]
      """  KBConfigDesc  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.HasInputs:bool = obj["HasInputs"]
      """  Indicates if the configurator has inputs in its design.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.ResetPCInputsAttributes:bool = obj["ResetPCInputsAttributes"]
      """  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.UpdateCreatePartTarget:bool = obj["UpdateCreatePartTarget"]
      """  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.EnableCPQPartCreation:bool = obj["EnableCPQPartCreation"]
      """  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStrCompRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.PosOrder:int = obj["PosOrder"]
      """  Position order  """  
      self.CompName:str = obj["CompName"]
      """  Name  """  
      self.CompType:str = obj["CompType"]
      """  Type  """  
      self.CompDataType:str = obj["CompDataType"]
      """  Data Type  """  
      self.DisplayFormat:str = obj["DisplayFormat"]
      """  Display Format  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.DateFormat:str = obj["DateFormat"]
      """  The coded format to use for a Date component  """  
      self.DateSeparator:str = obj["DateSeparator"]
      """  The separator to use for a date component  """  
      self.DateFourDigitYear:bool = obj["DateFourDigitYear"]
      """  If True a 4 digit year will be used for the date  """  
      self.DateThreeCharMonth:bool = obj["DateThreeCharMonth"]
      """  Use a 3 character month instead of a numeric month  """  
      self.LogicalFormat:str = obj["LogicalFormat"]
      """  A coded value indicating the format to use for a logical component  """  
      self.LogicalTrueValue:str = obj["LogicalTrueValue"]
      """  The value to use for a True logical value  """  
      self.LogicalFalseValue:str = obj["LogicalFalseValue"]
      """  The value to use for a False logical value  """  
      self.PossibleValues:str = obj["PossibleValues"]
      """  The possible values for a Radio-Set, Combo-Box, or validated Character Fill-In  """  
      self.CanFormat:bool = obj["CanFormat"]
      """  True if formatting can be applied to the component  """  
      self.SmartStringSeparator:str = obj["SmartStringSeparator"]
      self.NumberDecimals:int = obj["NumberDecimals"]
      """  Number of decimals  """  
      self.NumberDigits:int = obj["NumberDigits"]
      """  Number of digits.  """  
      self.NumberNegatives:str = obj["NumberNegatives"]
      """  Type of negatives.  """  
      self.NumberThousands:bool = obj["NumberThousands"]
      """  Thousands' separator.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcTargetEntityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.AllowRecordCreation:bool = obj["AllowRecordCreation"]
      """  AllowRecordCreation  """  
      self.AllowPricing:bool = obj["AllowPricing"]
      """  AllowPricing  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.IncomingSmartString:bool = obj["IncomingSmartString"]
      """  IncomingSmartString  """  
      self.AllowReconfig:bool = obj["AllowReconfig"]
      """  Specifies if a configuration that was originally configured in another entity can be reconfigured in the new entity.  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.TableDesc:str = obj["TableDesc"]
      """  Description visible of table name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildCodeEditorInputs_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class BuildCodeEditorInputs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.availInputs:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildSampleSmartString_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class BuildSampleSmartString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangingEntConf_input:
   """ Required : 
   ipConfigID
   """  
   def __init__(self, obj):
      self.ipConfigID:str = obj["ipConfigID"]
      """  Current Config ID  """  
      pass

class ChangingEntConf_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isSynched:bool = obj["isSynched"]
      self.settingsExist:bool = obj["settingsExist"]
      pass

      """  output parameters  """  

class CheckConfigAndGetType_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Selected configuration ID  """  
      pass

class CheckConfigAndGetType_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckForEpicorWebClientSyncUpdates_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  ConfigurationID to validate  """  
      pass

class CheckForEpicorWebClientSyncUpdates_output:
   def __init__(self, obj):
      pass

class CheckValidRevision_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  part number  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Revision number  """  
      pass

class CheckValidRevision_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CreatePcStatus_input:
   """ Required : 
   configID
   partNum
   revisionNum
   isInspPlan
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  The configuration ID  """  
      self.partNum:str = obj["partNum"]
      """  The configuration part number  """  
      self.revisionNum:str = obj["revisionNum"]
      """  The configuration revision number  """  
      self.isInspPlan:bool = obj["isInspPlan"]
      """  Is this an inspection plan configuration  """  
      pass

class CreatePcStatus_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteConfigSequence_input:
   """ Required : 
   configID
   configPartNum
   configRevisionNum
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  The configurator ID  """  
      self.configPartNum:str = obj["configPartNum"]
      """  The configurator part number  """  
      self.configRevisionNum:str = obj["configRevisionNum"]
      """  The configurator revision number  """  
      pass

class DeleteConfigSequence_output:
   def __init__(self, obj):
      pass

class DeployToEWC_input:
   """ Required : 
   configID
   isTest
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.isTest:bool = obj["isTest"]
      """  inidicates whether or not EWC is deploying for the purpose of TestInputs or TestRules  """  
      pass

class DeployToEWC_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigImportExportTableset] = obj["returnObj"]
      pass

class DocRulesMoveDown_input:
   """ Required : 
   PcDocRulesRowid
   ds
   """  
   def __init__(self, obj):
      self.PcDocRulesRowid:str = obj["PcDocRulesRowid"]
      """  The SysRowID of the rule to be moved down  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class DocRulesMoveDown_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DocRulesMoveUp_input:
   """ Required : 
   PcDocRulesRowid
   ds
   """  
   def __init__(self, obj):
      self.PcDocRulesRowid:str = obj["PcDocRulesRowid"]
      """  The SysRowID of the rule to be moved up  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class DocRulesMoveUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DocVarMoveDown_input:
   """ Required : 
   PcDocVarRowid
   ds
   """  
   def __init__(self, obj):
      self.PcDocVarRowid:str = obj["PcDocVarRowid"]
      """  The RowIdent of the rule to be moved down  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class DocVarMoveDown_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DocVarMoveUp_input:
   """ Required : 
   PcDocVarRowid
   ds
   """  
   def __init__(self, obj):
      self.PcDocVarRowid:str = obj["PcDocVarRowid"]
      """  The RowIdent of the rule to be moved up  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class DocVarMoveUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DuplicateConfiguration_input:
   """ Required : 
   configID
   newConfigID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  The configuration ID to be duplicated.  """  
      self.newConfigID:str = obj["newConfigID"]
      """  The new configuration ID.  """  
      pass

class DuplicateConfiguration_output:
   def __init__(self, obj):
      pass

class EditorFilter_input:
   """ Required : 
   type
   configID
   ruleSeq
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  Indicates if will be for session filter or for ColumnFilter  """  
      self.configID:str = obj["configID"]
      """  ConfigID  """  
      self.ruleSeq:int = obj["ruleSeq"]
      """  ConfigID  """  
      pass

class EditorFilter_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Erp_Tablesets_CodeEditorPCDatasetTableset:
   def __init__(self, obj):
      self.CodeEditorPCTargets:list[Erp_Tablesets_CodeEditorPCTargetsRow] = obj["CodeEditorPCTargets"]
      self.CodeEditorPCDocVars:list[Erp_Tablesets_CodeEditorPCDocVarsRow] = obj["CodeEditorPCDocVars"]
      self.CodeEditorPCInputs:list[Erp_Tablesets_CodeEditorPCInputsRow] = obj["CodeEditorPCInputs"]
      self.CodeEditorPCMethodVars:list[Erp_Tablesets_CodeEditorPCMethodVarsRow] = obj["CodeEditorPCMethodVars"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CodeEditorPCDocVarsRow:
   def __init__(self, obj):
      self.VarName:str = obj["VarName"]
      self.DataType:str = obj["DataType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCInputsRow:
   def __init__(self, obj):
      self.InputName:str = obj["InputName"]
      self.InputType:str = obj["InputType"]
      self.DataType:str = obj["DataType"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCMethodVarsRow:
   def __init__(self, obj):
      self.VarName:str = obj["VarName"]
      self.DataType:str = obj["DataType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCTargetsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TableName:str = obj["TableName"]
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnFormat:str = obj["ColumnFormat"]
      """  Reserved for future development  """  
      self.ColumnSyntax:str = obj["ColumnSyntax"]
      self.UDColumn:bool = obj["UDColumn"]
      """  Indicates if the column is from the UD table  """  
      self.DataType:str = obj["DataType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfigImportExportLayeredImageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.InputName:str = obj["InputName"]
      self.ControlType:str = obj["ControlType"]
      self.ImageLayerID:str = obj["ImageLayerID"]
      self.ImageURL:str = obj["ImageURL"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfigImportExportLayeredImageTableset:
   def __init__(self, obj):
      self.ConfigImportExportLayeredImage:list[Erp_Tablesets_ConfigImportExportLayeredImageRow] = obj["ConfigImportExportLayeredImage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfigImportExportTableset:
   def __init__(self, obj):
      self.PcStatus:list[Erp_Tablesets_PcStatusRow] = obj["PcStatus"]
      self.FileStore:list[Erp_Tablesets_FileStoreRow] = obj["FileStore"]
      self.PcAssembly:list[Erp_Tablesets_PcAssemblyRow] = obj["PcAssembly"]
      self.PcAssemblyUsing:list[Erp_Tablesets_PcAssemblyUsingRow] = obj["PcAssemblyUsing"]
      self.PcDocRules:list[Erp_Tablesets_PcDocRulesRow] = obj["PcDocRules"]
      self.PcDocRulesExpr:list[Erp_Tablesets_PcDocRulesExprRow] = obj["PcDocRulesExpr"]
      self.PcDocVar:list[Erp_Tablesets_PcDocVarRow] = obj["PcDocVar"]
      self.PcDynLst:list[Erp_Tablesets_PcDynLstRow] = obj["PcDynLst"]
      self.PcDynLstCriteria:list[Erp_Tablesets_PcDynLstCriteriaRow] = obj["PcDynLstCriteria"]
      self.PcDynLstParams:list[Erp_Tablesets_PcDynLstParamsRow] = obj["PcDynLstParams"]
      self.PcExpVar:list[Erp_Tablesets_PcExpVarRow] = obj["PcExpVar"]
      self.PcFunctionDef:list[Erp_Tablesets_PcFunctionDefRow] = obj["PcFunctionDef"]
      self.PcFunctionParam:list[Erp_Tablesets_PcFunctionParamRow] = obj["PcFunctionParam"]
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.PcInputsExpr:list[Erp_Tablesets_PcInputsExprRow] = obj["PcInputsExpr"]
      self.PcInputsLayerDetail:list[Erp_Tablesets_PcInputsLayerDetailRow] = obj["PcInputsLayerDetail"]
      self.PcInputsLayerHeader:list[Erp_Tablesets_PcInputsLayerHeaderRow] = obj["PcInputsLayerHeader"]
      self.PcInputsRule:list[Erp_Tablesets_PcInputsRuleRow] = obj["PcInputsRule"]
      self.PcInputsRuleDef:list[Erp_Tablesets_PcInputsRuleDefRow] = obj["PcInputsRuleDef"]
      self.PcInputVar:list[Erp_Tablesets_PcInputVarRow] = obj["PcInputVar"]
      self.PcMethodVar:list[Erp_Tablesets_PcMethodVarRow] = obj["PcMethodVar"]
      self.PcPage:list[Erp_Tablesets_PcPageRow] = obj["PcPage"]
      self.PcPageExpr:list[Erp_Tablesets_PcPageExprRow] = obj["PcPageExpr"]
      self.PcRules:list[Erp_Tablesets_PcRulesRow] = obj["PcRules"]
      self.PcRuleSet:list[Erp_Tablesets_PcRuleSetRow] = obj["PcRuleSet"]
      self.PcRulesExpr:list[Erp_Tablesets_PcRulesExprRow] = obj["PcRulesExpr"]
      self.PcStatusExpr:list[Erp_Tablesets_PcStatusExprRow] = obj["PcStatusExpr"]
      self.PcStrComp:list[Erp_Tablesets_PcStrCompRow] = obj["PcStrComp"]
      self.PcStruct:list[Erp_Tablesets_PcStructRow] = obj["PcStruct"]
      self.PcTargetEntity:list[Erp_Tablesets_PcTargetEntityRow] = obj["PcTargetEntity"]
      self.QBuildMapping:list[Erp_Tablesets_QBuildMappingRow] = obj["QBuildMapping"]
      self.QBuildObj:list[Erp_Tablesets_QBuildObjRow] = obj["QBuildObj"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfigurationSequenceTableset:
   def __init__(self, obj):
      self.PcStruct:list[Erp_Tablesets_PcStructRow] = obj["PcStruct"]
      self.PcConfigSmartString:list[Erp_Tablesets_PcConfigSmartStringRow] = obj["PcConfigSmartString"]
      self.PcStrComp:list[Erp_Tablesets_PcStrCompRow] = obj["PcStrComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfiguratorDefTableset:
   def __init__(self, obj):
      self.PcStatus:list[Erp_Tablesets_PcStatusRow] = obj["PcStatus"]
      self.PcStatusAttch:list[Erp_Tablesets_PcStatusAttchRow] = obj["PcStatusAttch"]
      self.PcAudit:list[Erp_Tablesets_PcAuditRow] = obj["PcAudit"]
      self.PcDocRules:list[Erp_Tablesets_PcDocRulesRow] = obj["PcDocRules"]
      self.PcDocRulesExpr:list[Erp_Tablesets_PcDocRulesExprRow] = obj["PcDocRulesExpr"]
      self.PcDocVar:list[Erp_Tablesets_PcDocVarRow] = obj["PcDocVar"]
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.PcStrComp:list[Erp_Tablesets_PcStrCompRow] = obj["PcStrComp"]
      self.PcTargetEntity:list[Erp_Tablesets_PcTargetEntityRow] = obj["PcTargetEntity"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfiguratorDefValueListTableset:
   def __init__(self, obj):
      self.PcAvailInputsList:list[Erp_Tablesets_PcAvailInputsListRow] = obj["PcAvailInputsList"]
      self.PcPossibleValuesList:list[Erp_Tablesets_PcPossibleValuesListRow] = obj["PcPossibleValuesList"]
      self.PcTargetTablesList:list[Erp_Tablesets_PcTargetTablesListRow] = obj["PcTargetTablesList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FileStoreRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTable:str = obj["RelatedToTable"]
      """  RelatedToTable  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  ModifiedBy  """  
      self.ModifiedOn:str = obj["ModifiedOn"]
      """  ModifiedOn  """  
      self.Content:str = obj["Content"]
      """  Content  """  
      self.FileName:str = obj["FileName"]
      """  FileName  """  
      self.Category:str = obj["Category"]
      """  Category  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_KBConfigSearchListRow:
   def __init__(self, obj):
      self.KBConfigID:int = obj["KBConfigID"]
      self.KBConfigDesc:str = obj["KBConfigDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_KBConfigSearchListTableset:
   def __init__(self, obj):
      self.KBConfigSearchList:list[Erp_Tablesets_KBConfigSearchListRow] = obj["KBConfigSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcAssemblyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.Path:str = obj["Path"]
      """  Path  """  
      self.IncludeIn:int = obj["IncludeIn"]
      """  IncludeIn  """  
      self.ExternalAssembly:bool = obj["ExternalAssembly"]
      """  ExternalAssembly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CreateUsingClauses:bool = obj["CreateUsingClauses"]
      """  Used to determine if the using clauses are to be automatically created when a a new assembly is specified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PcStatusApproved:bool = obj["PcStatusApproved"]
      self.PcStatusDescription:str = obj["PcStatusDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAssemblyUsingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.UsingSeq:int = obj["UsingSeq"]
      """  UsingSeq  """  
      self.UsingClause:str = obj["UsingClause"]
      """  UsingClause  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAuditRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ChgDate:str = obj["ChgDate"]
      """  System Date when this change was made.  """  
      self.ChgTime:int = obj["ChgTime"]
      """  System Time (seconds since midnight) of when the changes were made.  """  
      self.ChgBy:str = obj["ChgBy"]
      """  UserID who made the changes.  Not maintainable by the user.  """  
      self.ChgDescription:str = obj["ChgDescription"]
      """  Used to enter a description of the changes that were made.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.CvtChgTime:str = obj["CvtChgTime"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAvailInputsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.ChoiceDisplay:str = obj["ChoiceDisplay"]
      self.ChoiceValue:str = obj["ChoiceValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcConfigSmartStringRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.StringStyle:str = obj["StringStyle"]
      self.PrefacePart:bool = obj["PrefacePart"]
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Reserved for future development  """  
      self.Separator:str = obj["Separator"]
      self.NumberFormat:str = obj["NumberFormat"]
      """  Reserved for future development  """  
      self.StartNumber:int = obj["StartNumber"]
      self.TargetEntityForSmartString:str = obj["TargetEntityForSmartString"]
      """  Reserved for future development  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDocRulesExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Document Rule Sequence Number  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  Document Rule Expression  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ProcessOrder:int = obj["ProcessOrder"]
      """  ProcessOrder  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispActionString:str = obj["DispActionString"]
      self.dbTable:str = obj["dbTable"]
      self.dbField:str = obj["dbField"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDocRulesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company ID  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Document Rule Sequence Number  """  
      self.RuleString:str = obj["RuleString"]
      """  Document Rule String  """  
      self.RuleType:str = obj["RuleType"]
      """  Document Rule Type  """  
      self.CalcName:str = obj["CalcName"]
      """  Name for the calculated field  """  
      self.CalcDataType:str = obj["CalcDataType"]
      """  Calculated field data type  """  
      self.dbField:str = obj["dbField"]
      """  Database field  """  
      self.dbTable:str = obj["dbTable"]
      """  Database table  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.Comments:str = obj["Comments"]
      """  Comment  """  
      self.RuleExpr:str = obj["RuleExpr"]
      """  Document Rule Expression  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Process Sequence  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ExtCompanyList:str = obj["ExtCompanyList"]
      """  ExtCompanyList  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.dspRuleType:str = obj["dspRuleType"]
      self.EntprsConf:bool = obj["EntprsConf"]
      self.TypeCode:str = obj["TypeCode"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.CompanyName:str = obj["CompanyName"]
      self.dspdbField:str = obj["dspdbField"]
      self.dspdbTable:str = obj["dspdbTable"]
      self.MultiCompany:bool = obj["MultiCompany"]
      """  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  """  
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.DispLinkString:str = obj["DispLinkString"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDocVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.VarNum:int = obj["VarNum"]
      """  VarNum  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.VarSeq:int = obj["VarSeq"]
      """  VarSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Format:str = obj["Format"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.DispLinkString:str = obj["DispLinkString"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstCriteriaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.CriteriaSeq:int = obj["CriteriaSeq"]
      """  Criteria sequence number to make this record unique.  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Column name to use for BAQ query criteria  """  
      self.Condition:str = obj["Condition"]
      """  Condition to use for BAQ query criteria. Options include: =, < >, >, <, >=, <=, BEGINS, MATCHES  """  
      self.ValueFrom:str = obj["ValueFrom"]
      """  This field will indicate where the ColumnValue will be taken from. Current options are BAQ, CONST and INPUT.  """  
      self.ColumnValue:str = obj["ColumnValue"]
      """  This field holds either a constant, a baq column name or a input name from which it will take the value to be used in the BAQ criteria.  """  
      self.Operator:str = obj["Operator"]
      """  Operator to be applied between each criteria. Values are restricted to AND/OR and if none is defined then AND will be used as a default.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.UseEmptyValue:bool = obj["UseEmptyValue"]
      """  UseEmptyValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ColumnType:str = obj["ColumnType"]
      """  Column data type used to identify what type of value should it be compared to, this value should come from the QueryField table.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  Page Sequence where the parent input exists  """  
      self.ValueFromDisplay:str = obj["ValueFromDisplay"]
      """  External field used to temporarily store a display value from which the real value is determined to then be stored in ValueFrom.  """  
      self.BAQProgramName:str = obj["BAQProgramName"]
      """  BAQ Program Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ListSeq:int = obj["ListSeq"]
      """  ListSeq  """  
      self.ParamName:str = obj["ParamName"]
      """  ParamName  """  
      self.ParamConst:bool = obj["ParamConst"]
      """  ParamConst  """  
      self.ParamValue:str = obj["ParamValue"]
      """  ParamValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PageSeq:int = obj["PageSeq"]
      """  Page Sequence where the parent input exists  """  
      self.ParamType:str = obj["ParamType"]
      """  This is the type of Parameter.  """  
      self.ParamInput:str = obj["ParamInput"]
      self.ParamModifier:str = obj["ParamModifier"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.Condition:str = obj["Condition"]
      """  Contains the logical expression as to when the list is used.  """  
      self.ListItems:str = obj["ListItems"]
      """  Contains the combo-box list items that are used when the condition is true.  """  
      self.InitVal:str = obj["InitVal"]
      """  The Initial value for the list.  """  
      self.BAQRunProgram:bool = obj["BAQRunProgram"]
      """  If TRUE then the dynamic list will be built by running a BAQ program  """  
      self.BAQProgramName:str = obj["BAQProgramName"]
      """  The BAQ program name used for building the dynamic list  """  
      self.BAQDispValue:str = obj["BAQDispValue"]
      """  Value that will be displayed from the BAQ  """  
      self.BAQInputVal:str = obj["BAQInputVal"]
      """  The input value for the BAQ  """  
      self.ListDataSource:str = obj["ListDataSource"]
      """  Defines the type of dynamic list from Static, BAQ, Program, etc.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RunTblLookup:bool = obj["RunTblLookup"]
      """  RunTblLookup  """  
      self.TblLookupID:str = obj["TblLookupID"]
      """  TblLookupID  """  
      self.TblLookupFunc:str = obj["TblLookupFunc"]
      """  TblLookupFunc  """  
      self.RunUserDefined:str = obj["RunUserDefined"]
      """  RunUserDefined  """  
      self.UserDefinedName:str = obj["UserDefinedName"]
      """  UserDefinedName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SortOrder:str = obj["SortOrder"]
      """  SortOrder  """  
      self.SubReturnColumn:str = obj["SubReturnColumn"]
      """  SubReturnColumn  """  
      self.ScriptCondition:str = obj["ScriptCondition"]
      """  ScriptCondition  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Reserved for Future Development  """  
      self.EnableScript:bool = obj["EnableScript"]
      """  Identifies if Script expressions are valid for Dynamic List Conditions  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      self.PageSeq:int = obj["PageSeq"]
      self.UserDefinedFunctionType:str = obj["UserDefinedFunctionType"]
      """  Either Client or Server where the UD Method is executed.  """  
      self.UserDefinedReturnType:str = obj["UserDefinedReturnType"]
      """  Storing the Return Type for the selected User Defined Method.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then details on this record can be updated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcExpVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TokenizedText:str = obj["TokenizedText"]
      """  Tokenized Text used by the expression builder.  """  
      self.CodeEditorText:str = obj["CodeEditorText"]
      self.AlternateText:str = obj["AlternateText"]
      self.Approved:bool = obj["Approved"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcFunctionDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.FunctionType:str = obj["FunctionType"]
      """  FunctionType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ReturnType:str = obj["ReturnType"]
      """  ReturnType  """  
      self.OldFunctionName:str = obj["OldFunctionName"]
      """  OldFunctionName  """  
      self.IsSync:bool = obj["IsSync"]
      """  IsSync  """  
      self.GlobalFunc:bool = obj["GlobalFunc"]
      """  GlobalFunc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BagID:str = obj["BagID"]
      """  BagID  """  
      self.NoInputs:bool = obj["NoInputs"]
      """  NoInputs  """  
      self.ScriptExpression:str = obj["ScriptExpression"]
      """  ScriptExpression  """  
      self.DispFunctionName:str = obj["DispFunctionName"]
      self.DispFunctionType:str = obj["DispFunctionType"]
      self.DispReturnType:str = obj["DispReturnType"]
      self.BtnEditScript:bool = obj["BtnEditScript"]
      """  Script expressions are only permitted for PCEMF configurator client expressions.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PcStatusApproved:bool = obj["PcStatusApproved"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcFunctionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.ParameterName:str = obj["ParameterName"]
      """  ParameterName  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.Modifier:str = obj["Modifier"]
      """  Modifier  """  
      self.ParamType:str = obj["ParamType"]
      """  ParamType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ParamSeq:int = obj["ParamSeq"]
      """  ParamSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.InitValue:str = obj["InitValue"]
      """  InitValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.InitString:str = obj["InitString"]
      self.InitDecimal:int = obj["InitDecimal"]
      self.InitLogical:bool = obj["InitLogical"]
      self.InitDate:str = obj["InitDate"]
      self.InUse:bool = obj["InUse"]
      """  Determines if the variable is being used by an input.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  LayerSeq  """  
      self.LayerName:str = obj["LayerName"]
      """  LayerName  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  LayerDesc  """  
      self.ZIndex:int = obj["ZIndex"]
      """  Order in which layers are placed on the base image.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.FileType:str = obj["FileType"]
      """  Png type is supported.  """  
      self.Category:str = obj["Category"]
      """  Free form text enabling users to categorize layers  """  
      self.Width:int = obj["Width"]
      """  Width of image  """  
      self.Height:int = obj["Height"]
      """  Height of image  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for Future Development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for Future Development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input name this header is assigned.  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID.  """  
      self.ImageID:str = obj["ImageID"]
      """  File name of the image to be retrieved from the Image URL.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ImageURL:str = obj["ImageURL"]
      """  The URL location of the image.  """  
      self.FileType:str = obj["FileType"]
      """  File types png and jpg are supported.  """  
      self.Width:int = obj["Width"]
      """  Image Width  """  
      self.Height:int = obj["Height"]
      """  Image height  """  
      self.Version:int = obj["Version"]
      """  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.ShowDistinct:bool = obj["ShowDistinct"]
      """  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  """  
      self.DesignControlType:str = obj["DesignControlType"]
      """  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoSizeList:bool = obj["AutoSizeList"]
      """  AutoSizeList  """  
      self.ListWidth:int = obj["ListWidth"]
      """  ListWidth  """  
      self.ImageSource:str = obj["ImageSource"]
      """  ImageSource  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.Content:str = obj["Content"]
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.FullInputName:str = obj["FullInputName"]
      """  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  """  
      self.ImageMapping:bool = obj["ImageMapping"]
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.InputRules:bool = obj["InputRules"]
      """  Indicates whether or not Input Rules have been defined.  """  
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.OnLaunch:str = obj["OnLaunch"]
      self.PageDisplaySeq:int = obj["PageDisplaySeq"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      """  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  """  
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ImageURL:str = obj["ImageURL"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRuleDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.TargetInputName:str = obj["TargetInputName"]
      """  The Input that is updated based upon the rule definition.  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Internal column used to keep the rows unique and permit the rule to be resequenced.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The order in which these definitions are interrogated.  """  
      self.SourceInputName:str = obj["SourceInputName"]
      """  Input whose value is used in determining if this rule is executed.  """  
      self.SourceInputProperty:str = obj["SourceInputProperty"]
      """  Reserved for future development.  Defaults to Value.  """  
      self.SourceCharacterValue:str = obj["SourceCharacterValue"]
      """  SourceCharacterValue  """  
      self.SourceIntegerValue:int = obj["SourceIntegerValue"]
      """  SourceIntegerValue  """  
      self.SourceDecimalValue:int = obj["SourceDecimalValue"]
      """  SourceDecimalValue  """  
      self.SourceDateValue:str = obj["SourceDateValue"]
      """  SourceDateValue  """  
      self.SourceLogicalValue:bool = obj["SourceLogicalValue"]
      """  SourceLogicalValue  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  """  
      self.LeftP:str = obj["LeftP"]
      """  Reserved for future development.  """  
      self.RightP:str = obj["RightP"]
      """  Reserved for future development.  """  
      self.AndOr:str = obj["AndOr"]
      """  Defaults to And and permits users to use more than one input in the rule.  """  
      self.CompOp:str = obj["CompOp"]
      """  Comparison operator used when evaluating the rule. Valid value at this time is equals.  """  
      self.Neg:bool = obj["Neg"]
      """  Reserved for future development.  Defaults to false.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ListValues:str = obj["ListValues"]
      self.SourceValue:str = obj["SourceValue"]
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, ComboBox  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourcePcInputsDesignControlType:str = obj["SourcePcInputsDesignControlType"]
      self.SourcePcInputsFormatString:str = obj["SourcePcInputsFormatString"]
      self.SourcePcInputsListItems:str = obj["SourcePcInputsListItems"]
      self.SourcePcInputsDataType:str = obj["SourcePcInputsDataType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.TargetInputName:str = obj["TargetInputName"]
      """  The Input that is updated based upon the rule definition.  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Internal column used to keep the rows unique and permit the rule to be resequenced.  """  
      self.RuleDesc:str = obj["RuleDesc"]
      """  Enter text that describes what the rule does.  """  
      self.TargetInputProperty:str = obj["TargetInputProperty"]
      """  Reserved for future development.  Defaults to Value.  """  
      self.TargetInputValue:str = obj["TargetInputValue"]
      """  The new value of the input when this rule executes.  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DefinitionDesc:str = obj["DefinitionDesc"]
      """  Associated Rule Defintion descriptions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcMethodVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.VarNum:int = obj["VarNum"]
      """  VarNum  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.VarSeq:int = obj["VarSeq"]
      """  VarSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DispLinkString:str = obj["DispLinkString"]
      """  Temporal column to show link phrase  """  
      self.Format:str = obj["Format"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcPageExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  The configuration page sequence.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcPageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  The configuration page sequence.  """  
      self.PageTitle:str = obj["PageTitle"]
      """  The title of the configuration page.  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the page.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the page  """  
      self.SkipOnLeaveOPL:bool = obj["SkipOnLeaveOPL"]
      """  If this is set to true then 'On Leave' expressions will not be processed when the input page loads during the configuration process.  Also, if this is set to true then it won't process the 'On Leave' expression for the current input unless the value changes.  If the value changes and the  OnLeave expression for the current input changes the value of another input then it will process the 'On Leave' expression for the other input.  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add OnLeave expressions to the page  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.ProcessDynLstFirst:bool = obj["ProcessDynLstFirst"]
      """  Process dynamic lists before on leave expressions for this page  """  
      self.DynLstHigher:bool = obj["DynLstHigher"]
      """  Only process dynamic lists with higher tab sequences  """  
      self.SkipPageProcessOL:bool = obj["SkipPageProcessOL"]
      """  Skip processing page on leave on load  """  
      self.SkipPageNoInputs:bool = obj["SkipPageNoInputs"]
      """  Do not process on leave expressions when page loads  """  
      self.SkipOnLeaveOPE:bool = obj["SkipOnLeaveOPE"]
      """  Do not process on leave expressions when leaving pages  """  
      self.pWidth:int = obj["pWidth"]
      """  Width of panel  """  
      self.pHeight:int = obj["pHeight"]
      """  Height of panel  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  Order sequence in which the page will be displayed to the user. This value has been separated from PageSeq.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.FirstPage:bool = obj["FirstPage"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcPossibleValuesListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.DisplayValue:str = obj["DisplayValue"]
      self.PossibleValue:str = obj["PossibleValue"]
      self.SeqNum:int = obj["SeqNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRuleSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      """  BOMElementSysRowID  """  
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      """  BOMElementTableName  """  
      self.BOMElementType:str = obj["BOMElementType"]
      """  BOMElementType  """  
      self.RuleTag:str = obj["RuleTag"]
      """  RuleTag  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  MtlSeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  OpDtlSeq  """  
      self.UseKeepWhen:bool = obj["UseKeepWhen"]
      """  UseKeepWhen  """  
      self.KeepWhenExpr:str = obj["KeepWhenExpr"]
      """  KeepWhenExpr  """  
      self.KeepWhenLValue:str = obj["KeepWhenLValue"]
      """  KeepWhenLValue  """  
      self.KeepWhenCompareOpr:str = obj["KeepWhenCompareOpr"]
      """  KeepWhenCompareOpr  """  
      self.KeepWhenRValue:str = obj["KeepWhenRValue"]
      """  KeepWhenRValue  """  
      self.KeepWhenRValueType:str = obj["KeepWhenRValueType"]
      """  KeepWhenRValueType  """  
      self.KeepWhenType:str = obj["KeepWhenType"]
      """  KeepWhenType  """  
      self.ExtCompanyList:str = obj["ExtCompanyList"]
      """  ExtCompanyList  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  Indicates if is allowed Enterprise Configuration  """  
      self.KeepWhenField:str = obj["KeepWhenField"]
      self.KeepWhenTable:str = obj["KeepWhenTable"]
      self.MultiCompany:bool = obj["MultiCompany"]
      """  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.CompanyName:str = obj["CompanyName"]
      """  If is Enterprise configuration allowed it will update if is Local Company or MultiCompany  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  The sequence the rule is going to be applied.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Operation Sequence Number  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number  """  
      self.ParPartNum:str = obj["ParPartNum"]
      """  Stores the parent part number within the multi-level BOM for which the rule is related.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this rule.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  Method Rule Expression  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ProcessOrder:int = obj["ProcessOrder"]
      """  ProcessOrder  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.ExprXMLItem:str = obj["ExprXMLItem"]
      """  ExprXMLItem  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispActionString:str = obj["DispActionString"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      self.RuleTag:str = obj["RuleTag"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.dbField:str = obj["dbField"]
      self.dbTable:str = obj["dbTable"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  The sequence the rule is going to be applied.  """  
      self.RuleString:str = obj["RuleString"]
      """  Method Rule String  """  
      self.RuleType:str = obj["RuleType"]
      """  Method Rule Type  """  
      self.RuleExpr:str = obj["RuleExpr"]
      """  Method Rule Expression  """  
      self.CalcName:str = obj["CalcName"]
      """  Name for the calculated field  """  
      self.CalcDataType:str = obj["CalcDataType"]
      """  Calculated field data type  """  
      self.dbField:str = obj["dbField"]
      """  Database Field  """  
      self.dbTable:str = obj["dbTable"]
      """  Database Table  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Operation Sequence Number  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number  """  
      self.ParPartNum:str = obj["ParPartNum"]
      """  Stores the parent part number within the multi-level BOM for which the rule is related.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.ElementType:str = obj["ElementType"]
      """  Defines what the rule is related to.  Valid values include Par, Opr, Mtl, Asm.  This is used in Gencode.p when creating the compiled code.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this rule.  """  
      self.RuleID:int = obj["RuleID"]
      """  A unique identifier for the rule.  This will be generated in the database trigger.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Process Sequence  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.CurrentNode:str = obj["CurrentNode"]
      """  The node that is currently selected in the tree.  """  
      self.CurrentRuleLineage:str = obj["CurrentRuleLineage"]
      self.ParentNode:str = obj["ParentNode"]
      """  The parent node of the current node that is selected in the tree  """  
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.DispLinkString:str = obj["DispLinkString"]
      """  Temporal column to show link phrase  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TypeCode:str = obj["TypeCode"]
      """  TypeCode  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusListTableset:
   def __init__(self, obj):
      self.PcStatusList:list[Erp_Tablesets_PcStatusListRow] = obj["PcStatusList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.AllowReconPO:bool = obj["AllowReconPO"]
      """  AllowReconPO  """  
      self.CompPricingJobMethod:bool = obj["CompPricingJobMethod"]
      """  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  """  
      self.CreateRev:bool = obj["CreateRev"]
      """  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  """  
      self.DefaultECO:str = obj["DefaultECO"]
      """  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  """  
      self.GenerateMethod:bool = obj["GenerateMethod"]
      """  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.PromptForCheckout:bool = obj["PromptForCheckout"]
      """  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  """  
      self.RemoveLink:bool = obj["RemoveLink"]
      """  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.UseSavedLayout:bool = obj["UseSavedLayout"]
      """  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.CreateNewConfigID:bool = obj["CreateNewConfigID"]
      """  CreateNewConfigID  """  
      self.UseTemplatePartDefaults:bool = obj["UseTemplatePartDefaults"]
      """  UseTemplatePartDefaults  """  
      self.DefaultPartNum:str = obj["DefaultPartNum"]
      """  DefaultPartNum  """  
      self.DefaultRevisionNum:str = obj["DefaultRevisionNum"]
      """  DefaultRevisionNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  """  
      self.RecycleJobs:bool = obj["RecycleJobs"]
      """  RecycleJobs  """  
      self.ClientDeployedToEWCDate:str = obj["ClientDeployedToEWCDate"]
      """  ClientDeployedToEWCDate  """  
      self.EWCClientSyncRequired:bool = obj["EWCClientSyncRequired"]
      """  EWCClientSyncRequired  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.Kinetic:bool = obj["Kinetic"]
      """  Kinetic  """  
      self.KBConfigID:int = obj["KBConfigID"]
      """  KBConfigID  """  
      self.KBConfigDesc:str = obj["KBConfigDesc"]
      """  KBConfigDesc  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.HasInputs:bool = obj["HasInputs"]
      """  Indicates if the configurator has inputs in its design.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.ResetPCInputsAttributes:bool = obj["ResetPCInputsAttributes"]
      """  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.UpdateCreatePartTarget:bool = obj["UpdateCreatePartTarget"]
      """  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.EnableCPQPartCreation:bool = obj["EnableCPQPartCreation"]
      """  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStrCompRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.PosOrder:int = obj["PosOrder"]
      """  Position order  """  
      self.CompName:str = obj["CompName"]
      """  Name  """  
      self.CompType:str = obj["CompType"]
      """  Type  """  
      self.CompDataType:str = obj["CompDataType"]
      """  Data Type  """  
      self.DisplayFormat:str = obj["DisplayFormat"]
      """  Display Format  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.DateFormat:str = obj["DateFormat"]
      """  The coded format to use for a Date component  """  
      self.DateSeparator:str = obj["DateSeparator"]
      """  The separator to use for a date component  """  
      self.DateFourDigitYear:bool = obj["DateFourDigitYear"]
      """  If True a 4 digit year will be used for the date  """  
      self.DateThreeCharMonth:bool = obj["DateThreeCharMonth"]
      """  Use a 3 character month instead of a numeric month  """  
      self.LogicalFormat:str = obj["LogicalFormat"]
      """  A coded value indicating the format to use for a logical component  """  
      self.LogicalTrueValue:str = obj["LogicalTrueValue"]
      """  The value to use for a True logical value  """  
      self.LogicalFalseValue:str = obj["LogicalFalseValue"]
      """  The value to use for a False logical value  """  
      self.PossibleValues:str = obj["PossibleValues"]
      """  The possible values for a Radio-Set, Combo-Box, or validated Character Fill-In  """  
      self.CanFormat:bool = obj["CanFormat"]
      """  True if formatting can be applied to the component  """  
      self.SmartStringSeparator:str = obj["SmartStringSeparator"]
      self.NumberDecimals:int = obj["NumberDecimals"]
      """  Number of decimals  """  
      self.NumberDigits:int = obj["NumberDigits"]
      """  Number of digits.  """  
      self.NumberNegatives:str = obj["NumberNegatives"]
      """  Type of negatives.  """  
      self.NumberThousands:bool = obj["NumberThousands"]
      """  Thousands' separator.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStructRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the parent configured part number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the parent configured part number  """  
      self.ConfLabel:str = obj["ConfLabel"]
      """  An optional label to identify the purpose of the sub configurator rule.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Sub assembly configured part number that can be run from this configurator based on the condition of this rule  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  The revision number of the configurator that can be run from this configurator based on the condition of this rule  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Optional field.  The sales companies do not have the manufacturing information available but the manufacturing company must put the result of the sub configurator somewhere in the method.  The field has 3 options, E (Equal), G (Greater Than), L (Less Than).  The result of this rule will be inserted in the BOM in the location specified in this field.  If no value is entered, the result will be appended at the end of the BOM structure.  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the structure rule  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Default operation sequence  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.StructID:int = obj["StructID"]
      """  StructID  """  
      self.RelatedTo:str = obj["RelatedTo"]
      """  RelatedTo  """  
      self.RelatedToID:str = obj["RelatedToID"]
      """  RelatedToID  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  DisplaySeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.E9PcInValueRuleTag:str = obj["E9PcInValueRuleTag"]
      """  E9PcInValueRuleTag  """  
      self.BasePartNum:str = obj["BasePartNum"]
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.ConfigSysRowID:str = obj["ConfigSysRowID"]
      self.ConfigType:str = obj["ConfigType"]
      self.ConfigVersion:int = obj["ConfigVersion"]
      self.CreatePart:bool = obj["CreatePart"]
      self.DefaultECO:str = obj["DefaultECO"]
      self.DisplayTag:str = obj["DisplayTag"]
      self.KeepIt:bool = obj["KeepIt"]
      self.NewPartNum:str = obj["NewPartNum"]
      self.OverwriteSIValues:bool = obj["OverwriteSIValues"]
      self.ParentNewAsm:str = obj["ParentNewAsm"]
      self.PromptForAutoCreate:bool = obj["PromptForAutoCreate"]
      self.PromptForCheckout:bool = obj["PromptForCheckout"]
      self.PromptForPart:bool = obj["PromptForPart"]
      self.PromptForSIValues:bool = obj["PromptForSIValues"]
      self.ResponseAutoCreatePart:bool = obj["ResponseAutoCreatePart"]
      self.RevExists:bool = obj["RevExists"]
      self.RevolvingSeq:int = obj["RevolvingSeq"]
      """  Revolving Sequence  """  
      self.SavedGroupSeq:int = obj["SavedGroupSeq"]
      self.SaveHeadNum:int = obj["SaveHeadNum"]
      self.SIGroupSeq:int = obj["SIGroupSeq"]
      self.SIHeadNum:int = obj["SIHeadNum"]
      self.SmartString:str = obj["SmartString"]
      self.SourceSysRowID:str = obj["SourceSysRowID"]
      """  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRe the PartRev.SysRowID and SourceTableName will have "PartRev", otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  """  
      self.SourceTableName:str = obj["SourceTableName"]
      """  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRev" and SourceSysRowID will contain the PartRev.SysRowID, otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  """  
      self.StructTag:str = obj["StructTag"]
      self.SubBasePartNum:str = obj["SubBasePartNum"]
      self.SubBaseRevisionNum:str = obj["SubBaseRevisionNum"]
      self.SubConfigID:str = obj["SubConfigID"]
      self.UseKeepWhen:bool = obj["UseKeepWhen"]
      self.ParentStructID:int = obj["ParentStructID"]
      self.GenerateMethod:bool = obj["GenerateMethod"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartIUM:str = obj["PartIUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcTargetEntityListTableset:
   def __init__(self, obj):
      self.PcTargetEntity:list[Erp_Tablesets_PcTargetEntityRow] = obj["PcTargetEntity"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcTargetEntityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.AllowRecordCreation:bool = obj["AllowRecordCreation"]
      """  AllowRecordCreation  """  
      self.AllowPricing:bool = obj["AllowPricing"]
      """  AllowPricing  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.IncomingSmartString:bool = obj["IncomingSmartString"]
      """  IncomingSmartString  """  
      self.AllowReconfig:bool = obj["AllowReconfig"]
      """  Specifies if a configuration that was originally configured in another entity can be reconfigured in the new entity.  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.TableDesc:str = obj["TableDesc"]
      """  Description visible of table name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcTargetTablesListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.Code:str = obj["Code"]
      self.Description:str = obj["Description"]
      self.Hide:bool = obj["Hide"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the object name.  """  
      self.ObjParameter:str = obj["ObjParameter"]
      """  This is the name of the object parameter.  """  
      self.MappedInputName:str = obj["MappedInputName"]
      """  Name of the input mapped to this object parameter.  """  
      self.ObjParameterDataType:str = obj["ObjParameterDataType"]
      """  This is the data type of the object parameter.  """  
      self.ObjParameterInitValue:str = obj["ObjParameterInitValue"]
      """  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataType:str = obj["DataType"]
      self.PageSeq:int = obj["PageSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.QBuildObjObjType:str = obj["QBuildObjObjType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildObjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the name of the object.  """  
      self.ObjType:str = obj["ObjType"]
      """  This is the object type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PageSeq:int = obj["PageSeq"]
      self.DataType:str = obj["DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtConfiguratorDefTableset:
   def __init__(self, obj):
      self.PcStatus:list[Erp_Tablesets_PcStatusRow] = obj["PcStatus"]
      self.PcStatusAttch:list[Erp_Tablesets_PcStatusAttchRow] = obj["PcStatusAttch"]
      self.PcAudit:list[Erp_Tablesets_PcAuditRow] = obj["PcAudit"]
      self.PcDocRules:list[Erp_Tablesets_PcDocRulesRow] = obj["PcDocRules"]
      self.PcDocRulesExpr:list[Erp_Tablesets_PcDocRulesExprRow] = obj["PcDocRulesExpr"]
      self.PcDocVar:list[Erp_Tablesets_PcDocVarRow] = obj["PcDocVar"]
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.PcStrComp:list[Erp_Tablesets_PcStrCompRow] = obj["PcStrComp"]
      self.PcTargetEntity:list[Erp_Tablesets_PcTargetEntityRow] = obj["PcTargetEntity"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportConfiguration_input:
   """ Required : 
   configID
   path
   fileName
   doInputs
   doComments
   doSequence
   doPartCreation
   doSmartString
   doDocRules
   doPcRules
   doGlbVar
   configImportExportLayeredImageTS
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.path:str = obj["path"]
      self.fileName:str = obj["fileName"]
      self.doInputs:bool = obj["doInputs"]
      self.doComments:bool = obj["doComments"]
      self.doSequence:bool = obj["doSequence"]
      self.doPartCreation:bool = obj["doPartCreation"]
      self.doSmartString:bool = obj["doSmartString"]
      self.doDocRules:bool = obj["doDocRules"]
      self.doPcRules:bool = obj["doPcRules"]
      self.doGlbVar:bool = obj["doGlbVar"]
      self.configImportExportLayeredImageTS:list[Erp_Tablesets_ConfigImportExportLayeredImageTableset] = obj["configImportExportLayeredImageTS"]
      pass

class ExportConfiguration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.configImportExportLayeredImageTS:list[Erp_Tablesets_ConfigImportExportLayeredImageTableset] = obj["configImportExportLayeredImageTS"]
      pass

      """  output parameters  """  

class GenerateConfigSequence_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  The configurator id  """  
      pass

class GenerateConfigSequence_output:
   def __init__(self, obj):
      pass

class GetAvailDocVariables_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  The configuration ID  """  
      pass

class GetAvailDocVariables_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.availDocVars:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAvailInputs_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class GetAvailInputs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefValueListTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCodeEditorOptions_input:
   """ Required : 
   configID
   udTargetTables
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.udTargetTables:str = obj["udTargetTables"]
      pass

class GetCodeEditorOptions_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CodeEditorPCDatasetTableset] = obj["returnObj"]
      pass

class GetConfigurationOptions_input:
   """ Required : 
   optionType
   """  
   def __init__(self, obj):
      self.optionType:str = obj["optionType"]
      """  The type of option to get.
            Valid values are: PartCreateMethods, SmartStringStyles, SeparatorChars, NumberFormats, PriceMultipliers,
            SmartStringDateFormats, SmartStringDateSeparators, SmartStringLogicalFormats, NumFormatSignOptions, HTMLProducts  """  
      pass

class GetConfigurationOptions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.optionList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetEffectiveRevision_input:
   """ Required : 
   ipConfigID
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipConfigID:str = obj["ipConfigID"]
      """  Configuration ID  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Configuration ID  """  
      pass

class GetEffectiveRevision_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFormatString_input:
   """ Required : 
   company
   configID
   compName
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The company ID  """  
      self.configID:str = obj["configID"]
      """  The configuration ID  """  
      self.compName:str = obj["compName"]
      """  The input's name  """  
      pass

class GetFormatString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.formatString:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInputPossibleValues_input:
   """ Required : 
   configID
   inputName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configurator ID  """  
      self.inputName:str = obj["inputName"]
      """  Input name  """  
      pass

class GetInputPossibleValues_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefValueListTableset] = obj["returnObj"]
      pass

class GetKBConfigSearchList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetKBConfigSearchList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_KBConfigSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLinkedParts_input:
   """ Required : 
   ipConfigID
   """  
   def __init__(self, obj):
      self.ipConfigID:str = obj["ipConfigID"]
      """  Configuration ID  """  
      pass

class GetLinkedParts_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcStatusListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPcAudit_input:
   """ Required : 
   ds
   partNum
   revisionNum
   chgDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.chgDate:str = obj["chgDate"]
      pass

class GetNewPcAudit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcDocRulesExpr_input:
   """ Required : 
   ds
   configID
   ruleSeq
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.ruleSeq:int = obj["ruleSeq"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewPcDocRulesExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcDocRules_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcDocRules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcDocVar_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcDocVar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputs_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcInputs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcStatusAttch_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcStatusAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcStatus_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class GetNewPcStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcStrComp_input:
   """ Required : 
   ds
   configID
   posOrder
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.posOrder:int = obj["posOrder"]
      pass

class GetNewPcStrComp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcTargetEntity_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcTargetEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPcTargetEntityListIncludeUD_input:
   """ Required : 
   whereClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Search clause  """  
      pass

class GetPcTargetEntityListIncludeUD_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcTargetEntityListTableset] = obj["returnObj"]
      pass

class GetPcTargetEntityList_input:
   """ Required : 
   whereClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Search clause  """  
      pass

class GetPcTargetEntityList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcTargetEntityListTableset] = obj["returnObj"]
      pass

class GetRevisions_input:
   """ Required : 
   ipPartNum
   ipConfigID
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Selected part number  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  Current configuration ID  """  
      pass

class GetRevisions_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePcStatus
   whereClausePcStatusAttch
   whereClausePcAudit
   whereClausePcDocRules
   whereClausePcDocRulesExpr
   whereClausePcDocVar
   whereClausePcInputs
   whereClausePcStrComp
   whereClausePcTargetEntity
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcStatus:str = obj["whereClausePcStatus"]
      self.whereClausePcStatusAttch:str = obj["whereClausePcStatusAttch"]
      self.whereClausePcAudit:str = obj["whereClausePcAudit"]
      self.whereClausePcDocRules:str = obj["whereClausePcDocRules"]
      self.whereClausePcDocRulesExpr:str = obj["whereClausePcDocRulesExpr"]
      self.whereClausePcDocVar:str = obj["whereClausePcDocVar"]
      self.whereClausePcInputs:str = obj["whereClausePcInputs"]
      self.whereClausePcStrComp:str = obj["whereClausePcStrComp"]
      self.whereClausePcTargetEntity:str = obj["whereClausePcTargetEntity"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSequenceForTree_input:
   """ Required : 
   ipCompanyID
   ipConfigID
   ipPartNum
   ipRevisionNum
   """  
   def __init__(self, obj):
      self.ipCompanyID:str = obj["ipCompanyID"]
      """  The company ID to return data for.  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  The configuration ID to return data for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      pass

class GetSequenceForTree_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["returnObj"]
      pass

class GetSpecRevs_input:
   """ Required : 
   ipSpecID
   """  
   def __init__(self, obj):
      self.ipSpecID:str = obj["ipSpecID"]
      """  Specification ID  """  
      pass

class GetSpecRevs_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTargetEntityColumns_input:
   """ Required : 
   whereClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      pass

class GetTargetEntityColumns_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CodeEditorPCDatasetTableset] = obj["returnObj"]
      pass

class GetTargetTables_input:
   """ Required : 
   configType
   """  
   def __init__(self, obj):
      self.configType:str = obj["configType"]
      """  The config type  """  
      pass

class GetTargetTables_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorDefValueListTableset] = obj["returnObj"]
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class ImportConfiguration_input:
   """ Required : 
   configID
   fileToImport
   replComp
   aprvConfig
   doInputs
   doPartCreation
   doSmartString
   doComments
   doSequence
   doDocRules
   doPcRules
   doGlbVar
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.fileToImport:str = obj["fileToImport"]
      """  File To Import  """  
      self.replComp:bool = obj["replComp"]
      """  Replicate Company  """  
      self.aprvConfig:bool = obj["aprvConfig"]
      """  Approve Configuration on import  """  
      self.doInputs:str = obj["doInputs"]
      """  Include Inputs  """  
      self.doPartCreation:bool = obj["doPartCreation"]
      """  Include Part Creation  """  
      self.doSmartString:bool = obj["doSmartString"]
      """  Include Smart Strings  """  
      self.doComments:bool = obj["doComments"]
      """  Include Comments  """  
      self.doSequence:str = obj["doSequence"]
      """  Include Sequence  """  
      self.doDocRules:str = obj["doDocRules"]
      """  Include Document Rules  """  
      self.doPcRules:str = obj["doPcRules"]
      """  Include Method Rules  """  
      self.doGlbVar:str = obj["doGlbVar"]
      """  Include Input Variables  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      pass

class ImportConfiguration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.infoMessages:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeAttrClassID_input:
   """ Required : 
   ipConfigID
   schemaName
   tableName
   ipAttrClassID
   """  
   def __init__(self, obj):
      self.ipConfigID:str = obj["ipConfigID"]
      """  Configuration ID  """  
      self.schemaName:str = obj["schemaName"]
      """  Part Attribute Class Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Part Attribute Class Table Name  """  
      self.ipAttrClassID:str = obj["ipAttrClassID"]
      """  Part Attribute Class ID  """  
      pass

class OnChangeAttrClassID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opExistAttributes:bool = obj["opExistAttributes"]
      self.opDynAttributeConfigWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeConfigType_input:
   """ Required : 
   proposedConfigType
   ds
   """  
   def __init__(self, obj):
      self.proposedConfigType:str = obj["proposedConfigType"]
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangeConfigType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePcDocRulesExprLValue_input:
   """ Required : 
   newValue
   ds
   """  
   def __init__(self, obj):
      self.newValue:str = obj["newValue"]
      """  New value for LValue column  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangePcDocRulesExprLValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePcDocRulesLValue_input:
   """ Required : 
   newValue
   ds
   """  
   def __init__(self, obj):
      self.newValue:str = obj["newValue"]
      """  New value for LValue column  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangePcDocRulesLValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePcStatusKBConfigID_input:
   """ Required : 
   kbConfigID
   ds
   """  
   def __init__(self, obj):
      self.kbConfigID:int = obj["kbConfigID"]
      """  CPQ Configurator ID  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangePcStatusKBConfigID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedDocRuleCompany_input:
   """ Required : 
   multiCompany
   ds
   """  
   def __init__(self, obj):
      self.multiCompany:bool = obj["multiCompany"]
      """  Indicate if is multi company  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangedDocRuleCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedEntityColumn_input:
   """ Required : 
   columnName
   whereClause
   """  
   def __init__(self, obj):
      self.columnName:str = obj["columnName"]
      self.whereClause:str = obj["whereClause"]
      pass

class OnChangedEntityColumn_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangedPcDocRulesExprExprType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangedPcDocRulesExprExprType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcDocRulesRuleType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangedPcDocRulesRuleType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcDocVarDataType_input:
   """ Required : 
   newDataType
   ds
   """  
   def __init__(self, obj):
      self.newDataType:str = obj["newDataType"]
      """  New DataType  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangedPcDocVarDataType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcDocVarExprType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangedPcDocVarExprType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcStatusCreatePart_input:
   """ Required : 
   createPart
   ds
   """  
   def __init__(self, obj):
      self.createPart:bool = obj["createPart"]
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangedPcStatusCreatePart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcStatusRemoveLink_input:
   """ Required : 
   NonConfigurable
   ds
   """  
   def __init__(self, obj):
      self.NonConfigurable:bool = obj["NonConfigurable"]
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangedPcStatusRemoveLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingPcDocVarDataType_input:
   """ Required : 
   newDataType
   ds
   """  
   def __init__(self, obj):
      self.newDataType:str = obj["newDataType"]
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangingPcDocVarDataType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingPcDocVarVarName_input:
   """ Required : 
   newVarName
   ds
   """  
   def __init__(self, obj):
      self.newVarName:str = obj["newVarName"]
      """  New DataType  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class OnChangingPcDocVarVarName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostDeployMessageToEWC_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID EWC needs to deploy  """  
      pass

class PostDeployMessageToEWC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.resultMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PromptForPassword_input:
   """ Required : 
   ipTestPlan
   ipConfigID
   """  
   def __init__(self, obj):
      self.ipTestPlan:bool = obj["ipTestPlan"]
      """  Is this a test plan.  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  Configuration ID of the revisions being synched.  """  
      pass

class PromptForPassword_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPromptForPassword:bool = obj["opPromptForPassword"]
      self.opRevisionStatus:bool = obj["opRevisionStatus"]
      self.opRevisionFound:bool = obj["opRevisionFound"]
      pass

      """  output parameters  """  

class RefreshConfiguratorSequence_input:
   """ Required : 
   ipCompanyID
   ipConfigID
   ipPartNum
   ipRevisionNum
   ipManualRefresh
   refreshPcValueHead
   """  
   def __init__(self, obj):
      self.ipCompanyID:str = obj["ipCompanyID"]
      """  The Configuration ID to return data for.  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  The Configuration ID to return data for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part number ID to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The revision number to return data for.  """  
      self.ipManualRefresh:bool = obj["ipManualRefresh"]
      """  True if manually called from within the designer.  """  
      self.refreshPcValueHead:bool = obj["refreshPcValueHead"]
      """  True if the sequence of PcValueHead should be updated.  """  
      pass

class RefreshConfiguratorSequence_output:
   def __init__(self, obj):
      pass

class RefreshPcStatusBeforeDisapprove_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class RefreshPcStatusBeforeDisapprove_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshSubConf_input:
   """ Required : 
   ipCompanyID
   ipConfigID
   ipPartNum
   ipRevisionNum
   ipManualRefresh
   """  
   def __init__(self, obj):
      self.ipCompanyID:str = obj["ipCompanyID"]
      """  The Configuration ID to return data for.  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  The Configuration ID to return data for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part number ID to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The revision number to return data for.  """  
      self.ipManualRefresh:bool = obj["ipManualRefresh"]
      """  True if manually called from within the designer.  """  
      pass

class RefreshSubConf_output:
   def __init__(self, obj):
      pass

class RetrievePcLayeredImagesForExport_input:
   """ Required : 
   configID
   configImportExportLayeredImageTableset
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  configuration ID  """  
      self.configImportExportLayeredImageTableset:list[Erp_Tablesets_ConfigImportExportLayeredImageTableset] = obj["configImportExportLayeredImageTableset"]
      pass

class RetrievePcLayeredImagesForExport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.configImportExportLayeredImageTableset:list[Erp_Tablesets_ConfigImportExportLayeredImageTableset] = obj["configImportExportLayeredImageTableset"]
      pass

      """  output parameters  """  

class SalesKitConfiguration_input:
   """ Required : 
   PcPartNum
   """  
   def __init__(self, obj):
      self.PcPartNum:str = obj["PcPartNum"]
      """  The current part number  """  
      pass

class SalesKitConfiguration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.SalesKit:bool = obj["SalesKit"]
      pass

      """  output parameters  """  

class SmartStringMoveDown_input:
   """ Required : 
   PcStrCompRowid
   ds
   """  
   def __init__(self, obj):
      self.PcStrCompRowid:str = obj["PcStrCompRowid"]
      """  The RowIdent of the input to be moved down  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class SmartStringMoveDown_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SmartStringMoveUp_input:
   """ Required : 
   PcStrCompRowid
   ds
   """  
   def __init__(self, obj):
      self.PcStrCompRowid:str = obj["PcStrCompRowid"]
      """  The RowIdent of the PcStrComp to be moved up  """  
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class SmartStringMoveUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SyncRevision_input:
   """ Required : 
   ipTestPlan
   ipApproved
   ipValidPassword
   ipConfigID
   ipAuditDesc
   """  
   def __init__(self, obj):
      self.ipTestPlan:bool = obj["ipTestPlan"]
      """  Is this a test plan configuration  """  
      self.ipApproved:bool = obj["ipApproved"]
      """  The proposed approval flag  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method
            in the UserFile BO.  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  The configurator ID of the revisions to synchronize  """  
      self.ipAuditDesc:str = obj["ipAuditDesc"]
      """  The audit description entered for the configuration approval  """  
      pass

class SyncRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.revSynched:bool = obj["revSynched"]
      pass

      """  output parameters  """  

class TestInputsPostDeployMessageToEWC_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class TestInputsPostDeployMessageToEWC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.resultMessage:str = obj["parameters"]
      self.configRuntimeURL:str = obj["parameters"]
      self.testFileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateEpicorWebDeployStatus_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration to update the DeployedToEWCDate with the current date time.  """  
      pass

class UpdateEpicorWebDeployStatus_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorDefTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorDefTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePcStruct_input:
   """ Required : 
   PcStructRowID
   newDisplaySeq
   """  
   def __init__(self, obj):
      self.PcStructRowID:str = obj["PcStructRowID"]
      """  The RowIdent of the sequence to be moved down  """  
      self.newDisplaySeq:int = obj["newDisplaySeq"]
      """  The new display sequence to assign to the field  """  
      pass

class UpdatePcStruct_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePcDocRulesDelete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

class ValidatePcDocRulesDelete_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

