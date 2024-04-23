import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DataCheckSvc
# Description: Data Health check server
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DataChecks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataChecks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataChecks
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks",headers=creds) as resp:
           return await resp.json()

async def post_DataChecks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataCheck item
   Description: Calls GetByID to retrieve the DataCheck item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheck
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataCheck for the service
   Description: Calls UpdateExt to update DataCheck. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheck
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataCheck item
   Description: Call UpdateExt to delete DataCheck item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheck
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckDDefs(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataCheckDDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataCheckDDefs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckDDefs",headers=creds) as resp:
           return await resp.json()

async def get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataCheckDDef item
   Description: Calls GetByID to retrieve the DataCheckDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckDDef1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckParams(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataCheckParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataCheckParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckParams",headers=creds) as resp:
           return await resp.json()

async def get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataCheckParam item
   Description: Calls GetByID to retrieve the DataCheckParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckRpts(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataCheckRpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataCheckRpts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckRpts",headers=creds) as resp:
           return await resp.json()

async def get_DataChecks_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataCheckRpt item
   Description: Calls GetByID to retrieve the DataCheckRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckRpt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataChecks(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataCheckDDefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataCheckDDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataCheckDDefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs",headers=creds) as resp:
           return await resp.json()

async def post_DataCheckDDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataCheckDDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataCheckDDef item
   Description: Calls GetByID to retrieve the DataCheckDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckDDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataCheckDDef for the service
   Description: Calls UpdateExt to update DataCheckDDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheckDDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckDDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataCheckDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataCheckDDef item
   Description: Call UpdateExt to delete DataCheckDDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheckDDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataCheckParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataCheckParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataCheckParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams",headers=creds) as resp:
           return await resp.json()

async def post_DataCheckParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataCheckParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataCheckParam item
   Description: Calls GetByID to retrieve the DataCheckParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataCheckParam for the service
   Description: Calls UpdateExt to update DataCheckParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheckParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataCheckParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataCheckParam item
   Description: Call UpdateExt to delete DataCheckParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheckParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataCheckRpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataCheckRpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataCheckRpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataCheckRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts",headers=creds) as resp:
           return await resp.json()

async def post_DataCheckRpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataCheckRpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataCheckRpt item
   Description: Calls GetByID to retrieve the DataCheckRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataCheckRpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataCheckRpt for the service
   Description: Calls UpdateExt to update DataCheckRpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataCheckRpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataCheckRptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataCheckRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataCheckRpt item
   Description: Call UpdateExt to delete DataCheckRpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataCheckRpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/DataCheckRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataChecklistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDataCheck, whereClauseDataCheckDDef, whereClauseDataCheckParam, whereClauseDataCheckRpt, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataCheck=" + whereClauseDataCheck
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataCheckDDef=" + whereClauseDataCheckDDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataCheckParam=" + whereClauseDataCheckParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataCheckRpt=" + whereClauseDataCheckRpt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, localName, key1, key2, key3, key4, key5, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "localName=" + localName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key4=" + key4
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key5=" + key5

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Retrieve DataCheck rows from Local001 table and populate temp tables
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDCustom
   Description: Get DataCheck data for given DataCheckId
   OperationID: GetByIDCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartCheck
   Description: Start Check
   OperationID: StartCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCheck
   Description: Update Check
   OperationID: UpdateCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelCheck
   Description: Cancel Check
   OperationID: CancelCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentInstallation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentInstallation
   Description: Get the current tenant and installation ids
   OperationID: GetCurrentInstallation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentInstallation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentInstallation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTenants(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTenants
   Description: Get all the tenants and installation ids
   OperationID: GetTenants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTenants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTenants_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectAll
   Description: Select all the current report records
   OperationID: SelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnSelectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnSelectAll
   Description: UnSelect all the current report records
   OperationID: UnSelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnSelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnSelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateParameterComponents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateParameterComponents
   Description: Generate the necessary components to fill parameters from ds.
   OperationID: GenerateParameterComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateParameterComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateParameterComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompanies(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanies
   Description: Get the companies available.
   OperationID: GetCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataCheck
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckDDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataCheckDDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataCheckParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataCheckRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataCheckRptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataCheckRptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataChecklistRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataChecklistRow] = obj["value"]
      pass

class Erp_Tablesets_DataCheckDDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.seqnum:int = obj["seqnum"]
      self.DataCheckddefid:str = obj["DataCheckddefid"]
      self.tblname:str = obj["tblname"]
      self.colname:str = obj["colname"]
      self.width:int = obj["width"]
      self.datatype:str = obj["datatype"]
      self.tabseq:int = obj["tabseq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataCheckParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.Label01:str = obj["Label01"]
      self.Value01:str = obj["Value01"]
      self.BlankOK01:bool = obj["BlankOK01"]
      self.DataType01:str = obj["DataType01"]
      self.ViewType01:str = obj["ViewType01"]
      self.Label02:str = obj["Label02"]
      self.Value02:str = obj["Value02"]
      self.BlankOK02:bool = obj["BlankOK02"]
      self.DataType02:str = obj["DataType02"]
      self.ViewType02:str = obj["ViewType02"]
      self.Label03:str = obj["Label03"]
      self.Value03:str = obj["Value03"]
      self.BlankOK03:bool = obj["BlankOK03"]
      self.DataType03:str = obj["DataType03"]
      self.ViewType03:str = obj["ViewType03"]
      self.Label04:str = obj["Label04"]
      self.Value04:str = obj["Value04"]
      self.BlankOK04:bool = obj["BlankOK04"]
      self.DataType04:str = obj["DataType04"]
      self.ViewType04:str = obj["ViewType04"]
      self.Label05:str = obj["Label05"]
      self.Value05:str = obj["Value05"]
      self.BlankOK05:bool = obj["BlankOK05"]
      self.DataType05:str = obj["DataType05"]
      self.ViewType05:str = obj["ViewType05"]
      self.Label06:str = obj["Label06"]
      self.Value06:str = obj["Value06"]
      self.BlankOK06:bool = obj["BlankOK06"]
      self.DataType06:str = obj["DataType06"]
      self.ViewType06:str = obj["ViewType06"]
      self.Label07:str = obj["Label07"]
      self.Value07:str = obj["Value07"]
      self.BlankOK07:bool = obj["BlankOK07"]
      self.DataType07:str = obj["DataType07"]
      self.ViewType07:str = obj["ViewType07"]
      self.Label08:str = obj["Label08"]
      self.Value08:str = obj["Value08"]
      self.BlankOK08:bool = obj["BlankOK08"]
      self.DataType08:str = obj["DataType08"]
      self.ViewType08:str = obj["ViewType08"]
      self.Label09:str = obj["Label09"]
      self.Value09:str = obj["Value09"]
      self.BlankOK09:bool = obj["BlankOK09"]
      self.DataType09:str = obj["DataType09"]
      self.ViewType09:str = obj["ViewType09"]
      self.Label10:str = obj["Label10"]
      self.Value10:str = obj["Value10"]
      self.BlankOK10:bool = obj["BlankOK10"]
      self.DataType10:str = obj["DataType10"]
      self.ViewType10:str = obj["ViewType10"]
      self.Label11:str = obj["Label11"]
      self.Value11:str = obj["Value11"]
      self.BlankOK11:bool = obj["BlankOK11"]
      self.DataType11:str = obj["DataType11"]
      self.ViewType11:str = obj["ViewType11"]
      self.Label12:str = obj["Label12"]
      self.Value12:str = obj["Value12"]
      self.BlankOK12:bool = obj["BlankOK12"]
      self.DataType12:str = obj["DataType12"]
      self.ViewType12:str = obj["ViewType12"]
      self.Label13:str = obj["Label13"]
      self.Value13:str = obj["Value13"]
      self.BlankOK13:bool = obj["BlankOK13"]
      self.DataType13:str = obj["DataType13"]
      self.ViewType13:str = obj["ViewType13"]
      self.Label14:str = obj["Label14"]
      self.Value14:str = obj["Value14"]
      self.BlankOK14:bool = obj["BlankOK14"]
      self.DataType14:str = obj["DataType14"]
      self.ViewType14:str = obj["ViewType14"]
      self.Label15:str = obj["Label15"]
      self.Value15:str = obj["Value15"]
      self.BlankOK15:bool = obj["BlankOK15"]
      self.DataType15:str = obj["DataType15"]
      self.ViewType15:str = obj["ViewType15"]
      self.Label16:str = obj["Label16"]
      self.Value16:str = obj["Value16"]
      self.BlankOK16:bool = obj["BlankOK16"]
      self.DataType16:str = obj["DataType16"]
      self.ViewType16:str = obj["ViewType16"]
      self.Label17:str = obj["Label17"]
      self.Value17:str = obj["Value17"]
      self.BlankOK17:bool = obj["BlankOK17"]
      self.DataType17:str = obj["DataType17"]
      self.ViewType17:str = obj["ViewType17"]
      self.Label18:str = obj["Label18"]
      self.Value18:str = obj["Value18"]
      self.BlankOK18:bool = obj["BlankOK18"]
      self.DataType18:str = obj["DataType18"]
      self.ViewType18:str = obj["ViewType18"]
      self.Label19:str = obj["Label19"]
      self.Value19:str = obj["Value19"]
      self.BlankOK19:bool = obj["BlankOK19"]
      self.DataType19:str = obj["DataType19"]
      self.ViewType19:str = obj["ViewType19"]
      self.Label20:str = obj["Label20"]
      self.Value20:str = obj["Value20"]
      self.BlankOK20:bool = obj["BlankOK20"]
      self.DataType20:str = obj["DataType20"]
      self.ViewType20:str = obj["ViewType20"]
      self.BlankCompOK:bool = obj["BlankCompOK"]
      self.LabelComp:str = obj["LabelComp"]
      self.ViewTypeComp:str = obj["ViewTypeComp"]
      self.ValueComp:str = obj["ValueComp"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataCheckRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Available:bool = obj["Available"]
      self.AvailDesc:str = obj["AvailDesc"]
      self.ExpiresInd:bool = obj["ExpiresInd"]
      self.Generic:bool = obj["Generic"]
      self.NotGeneric:bool = obj["NotGeneric"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataCheckRptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.UpdInd:bool = obj["UpdInd"]
      self.UpdTable:str = obj["UpdTable"]
      self.value01:str = obj["value01"]
      self.value02:str = obj["value02"]
      self.value03:str = obj["value03"]
      self.value04:str = obj["value04"]
      self.value05:str = obj["value05"]
      self.value06:str = obj["value06"]
      self.value07:str = obj["value07"]
      self.value08:str = obj["value08"]
      self.value09:str = obj["value09"]
      self.value10:str = obj["value10"]
      self.value11:str = obj["value11"]
      self.value12:str = obj["value12"]
      self.value13:str = obj["value13"]
      self.value14:str = obj["value14"]
      self.value15:str = obj["value15"]
      self.value16:str = obj["value16"]
      self.value17:str = obj["value17"]
      self.value18:str = obj["value18"]
      self.value19:str = obj["value19"]
      self.value20:str = obj["value20"]
      self.value21:str = obj["value21"]
      self.value22:str = obj["value22"]
      self.value23:str = obj["value23"]
      self.value24:str = obj["value24"]
      self.value25:str = obj["value25"]
      self.value26:str = obj["value26"]
      self.value27:str = obj["value27"]
      self.value28:str = obj["value28"]
      self.value29:str = obj["value29"]
      self.value30:str = obj["value30"]
      self.value31:str = obj["value31"]
      self.value32:str = obj["value32"]
      self.value33:str = obj["value33"]
      self.value34:str = obj["value34"]
      self.value35:str = obj["value35"]
      self.value36:str = obj["value36"]
      self.value37:str = obj["value37"]
      self.value38:str = obj["value38"]
      self.value39:str = obj["value39"]
      self.value40:str = obj["value40"]
      self.value41:str = obj["value41"]
      self.value42:str = obj["value42"]
      self.value43:str = obj["value43"]
      self.value44:str = obj["value44"]
      self.value45:str = obj["value45"]
      self.value46:str = obj["value46"]
      self.value47:str = obj["value47"]
      self.value48:str = obj["value48"]
      self.value49:str = obj["value49"]
      self.value50:str = obj["value50"]
      self.value51:str = obj["value51"]
      self.value52:str = obj["value52"]
      self.value53:str = obj["value53"]
      self.value54:str = obj["value54"]
      self.value55:str = obj["value55"]
      self.value56:str = obj["value56"]
      self.value57:str = obj["value57"]
      self.value58:str = obj["value58"]
      self.value59:str = obj["value59"]
      self.value60:str = obj["value60"]
      self.value61:str = obj["value61"]
      self.value62:str = obj["value62"]
      self.value63:str = obj["value63"]
      self.value64:str = obj["value64"]
      self.value65:str = obj["value65"]
      self.value66:str = obj["value66"]
      self.value67:str = obj["value67"]
      self.value68:str = obj["value68"]
      self.value69:str = obj["value69"]
      self.value70:str = obj["value70"]
      self.value71:str = obj["value71"]
      self.value72:str = obj["value72"]
      self.value73:str = obj["value73"]
      self.value74:str = obj["value74"]
      self.value75:str = obj["value75"]
      self.value76:str = obj["value76"]
      self.value77:str = obj["value77"]
      self.value78:str = obj["value78"]
      self.value79:str = obj["value79"]
      self.value80:str = obj["value80"]
      self.value81:str = obj["value81"]
      self.value82:str = obj["value82"]
      self.value83:str = obj["value83"]
      self.value84:str = obj["value84"]
      self.value85:str = obj["value85"]
      self.value86:str = obj["value86"]
      self.value87:str = obj["value87"]
      self.value88:str = obj["value88"]
      self.value89:str = obj["value89"]
      self.value90:str = obj["value90"]
      self.value91:str = obj["value91"]
      self.value92:str = obj["value92"]
      self.value93:str = obj["value93"]
      self.value94:str = obj["value94"]
      self.value95:str = obj["value95"]
      self.value96:str = obj["value96"]
      self.value97:str = obj["value97"]
      self.value98:str = obj["value98"]
      self.value99:str = obj["value99"]
      self.seqId:int = obj["seqId"]
      self.tblname:str = obj["tblname"]
      """  name of tab control record is displayed on  """  
      self.UpdXml:str = obj["UpdXml"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataChecklistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CancelCheck_input:
   """ Required : 
   SysRowId
   DataCheckId
   DataCheckSPName
   PageSize
   ds
   """  
   def __init__(self, obj):
      self.SysRowId:str = obj["SysRowId"]
      """  SysRowId of Data Fix record  """  
      self.DataCheckId:str = obj["DataCheckId"]
      """  Data Check ID  """  
      self.DataCheckSPName:str = obj["DataCheckSPName"]
      """  Data Check Stored Procedure  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of report records to return  """  
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

class CancelCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   company
   localName
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DataCheckDDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.seqnum:int = obj["seqnum"]
      self.DataCheckddefid:str = obj["DataCheckddefid"]
      self.tblname:str = obj["tblname"]
      self.colname:str = obj["colname"]
      self.width:int = obj["width"]
      self.datatype:str = obj["datatype"]
      self.tabseq:int = obj["tabseq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataCheckListTableset:
   def __init__(self, obj):
      self.DataChecklist:list[Erp_Tablesets_DataChecklistRow] = obj["DataChecklist"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DataCheckParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.Label01:str = obj["Label01"]
      self.Value01:str = obj["Value01"]
      self.BlankOK01:bool = obj["BlankOK01"]
      self.DataType01:str = obj["DataType01"]
      self.ViewType01:str = obj["ViewType01"]
      self.Label02:str = obj["Label02"]
      self.Value02:str = obj["Value02"]
      self.BlankOK02:bool = obj["BlankOK02"]
      self.DataType02:str = obj["DataType02"]
      self.ViewType02:str = obj["ViewType02"]
      self.Label03:str = obj["Label03"]
      self.Value03:str = obj["Value03"]
      self.BlankOK03:bool = obj["BlankOK03"]
      self.DataType03:str = obj["DataType03"]
      self.ViewType03:str = obj["ViewType03"]
      self.Label04:str = obj["Label04"]
      self.Value04:str = obj["Value04"]
      self.BlankOK04:bool = obj["BlankOK04"]
      self.DataType04:str = obj["DataType04"]
      self.ViewType04:str = obj["ViewType04"]
      self.Label05:str = obj["Label05"]
      self.Value05:str = obj["Value05"]
      self.BlankOK05:bool = obj["BlankOK05"]
      self.DataType05:str = obj["DataType05"]
      self.ViewType05:str = obj["ViewType05"]
      self.Label06:str = obj["Label06"]
      self.Value06:str = obj["Value06"]
      self.BlankOK06:bool = obj["BlankOK06"]
      self.DataType06:str = obj["DataType06"]
      self.ViewType06:str = obj["ViewType06"]
      self.Label07:str = obj["Label07"]
      self.Value07:str = obj["Value07"]
      self.BlankOK07:bool = obj["BlankOK07"]
      self.DataType07:str = obj["DataType07"]
      self.ViewType07:str = obj["ViewType07"]
      self.Label08:str = obj["Label08"]
      self.Value08:str = obj["Value08"]
      self.BlankOK08:bool = obj["BlankOK08"]
      self.DataType08:str = obj["DataType08"]
      self.ViewType08:str = obj["ViewType08"]
      self.Label09:str = obj["Label09"]
      self.Value09:str = obj["Value09"]
      self.BlankOK09:bool = obj["BlankOK09"]
      self.DataType09:str = obj["DataType09"]
      self.ViewType09:str = obj["ViewType09"]
      self.Label10:str = obj["Label10"]
      self.Value10:str = obj["Value10"]
      self.BlankOK10:bool = obj["BlankOK10"]
      self.DataType10:str = obj["DataType10"]
      self.ViewType10:str = obj["ViewType10"]
      self.Label11:str = obj["Label11"]
      self.Value11:str = obj["Value11"]
      self.BlankOK11:bool = obj["BlankOK11"]
      self.DataType11:str = obj["DataType11"]
      self.ViewType11:str = obj["ViewType11"]
      self.Label12:str = obj["Label12"]
      self.Value12:str = obj["Value12"]
      self.BlankOK12:bool = obj["BlankOK12"]
      self.DataType12:str = obj["DataType12"]
      self.ViewType12:str = obj["ViewType12"]
      self.Label13:str = obj["Label13"]
      self.Value13:str = obj["Value13"]
      self.BlankOK13:bool = obj["BlankOK13"]
      self.DataType13:str = obj["DataType13"]
      self.ViewType13:str = obj["ViewType13"]
      self.Label14:str = obj["Label14"]
      self.Value14:str = obj["Value14"]
      self.BlankOK14:bool = obj["BlankOK14"]
      self.DataType14:str = obj["DataType14"]
      self.ViewType14:str = obj["ViewType14"]
      self.Label15:str = obj["Label15"]
      self.Value15:str = obj["Value15"]
      self.BlankOK15:bool = obj["BlankOK15"]
      self.DataType15:str = obj["DataType15"]
      self.ViewType15:str = obj["ViewType15"]
      self.Label16:str = obj["Label16"]
      self.Value16:str = obj["Value16"]
      self.BlankOK16:bool = obj["BlankOK16"]
      self.DataType16:str = obj["DataType16"]
      self.ViewType16:str = obj["ViewType16"]
      self.Label17:str = obj["Label17"]
      self.Value17:str = obj["Value17"]
      self.BlankOK17:bool = obj["BlankOK17"]
      self.DataType17:str = obj["DataType17"]
      self.ViewType17:str = obj["ViewType17"]
      self.Label18:str = obj["Label18"]
      self.Value18:str = obj["Value18"]
      self.BlankOK18:bool = obj["BlankOK18"]
      self.DataType18:str = obj["DataType18"]
      self.ViewType18:str = obj["ViewType18"]
      self.Label19:str = obj["Label19"]
      self.Value19:str = obj["Value19"]
      self.BlankOK19:bool = obj["BlankOK19"]
      self.DataType19:str = obj["DataType19"]
      self.ViewType19:str = obj["ViewType19"]
      self.Label20:str = obj["Label20"]
      self.Value20:str = obj["Value20"]
      self.BlankOK20:bool = obj["BlankOK20"]
      self.DataType20:str = obj["DataType20"]
      self.ViewType20:str = obj["ViewType20"]
      self.BlankCompOK:bool = obj["BlankCompOK"]
      self.LabelComp:str = obj["LabelComp"]
      self.ViewTypeComp:str = obj["ViewTypeComp"]
      self.ValueComp:str = obj["ValueComp"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataCheckRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Available:bool = obj["Available"]
      self.AvailDesc:str = obj["AvailDesc"]
      self.ExpiresInd:bool = obj["ExpiresInd"]
      self.Generic:bool = obj["Generic"]
      self.NotGeneric:bool = obj["NotGeneric"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataCheckRptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.UpdInd:bool = obj["UpdInd"]
      self.UpdTable:str = obj["UpdTable"]
      self.value01:str = obj["value01"]
      self.value02:str = obj["value02"]
      self.value03:str = obj["value03"]
      self.value04:str = obj["value04"]
      self.value05:str = obj["value05"]
      self.value06:str = obj["value06"]
      self.value07:str = obj["value07"]
      self.value08:str = obj["value08"]
      self.value09:str = obj["value09"]
      self.value10:str = obj["value10"]
      self.value11:str = obj["value11"]
      self.value12:str = obj["value12"]
      self.value13:str = obj["value13"]
      self.value14:str = obj["value14"]
      self.value15:str = obj["value15"]
      self.value16:str = obj["value16"]
      self.value17:str = obj["value17"]
      self.value18:str = obj["value18"]
      self.value19:str = obj["value19"]
      self.value20:str = obj["value20"]
      self.value21:str = obj["value21"]
      self.value22:str = obj["value22"]
      self.value23:str = obj["value23"]
      self.value24:str = obj["value24"]
      self.value25:str = obj["value25"]
      self.value26:str = obj["value26"]
      self.value27:str = obj["value27"]
      self.value28:str = obj["value28"]
      self.value29:str = obj["value29"]
      self.value30:str = obj["value30"]
      self.value31:str = obj["value31"]
      self.value32:str = obj["value32"]
      self.value33:str = obj["value33"]
      self.value34:str = obj["value34"]
      self.value35:str = obj["value35"]
      self.value36:str = obj["value36"]
      self.value37:str = obj["value37"]
      self.value38:str = obj["value38"]
      self.value39:str = obj["value39"]
      self.value40:str = obj["value40"]
      self.value41:str = obj["value41"]
      self.value42:str = obj["value42"]
      self.value43:str = obj["value43"]
      self.value44:str = obj["value44"]
      self.value45:str = obj["value45"]
      self.value46:str = obj["value46"]
      self.value47:str = obj["value47"]
      self.value48:str = obj["value48"]
      self.value49:str = obj["value49"]
      self.value50:str = obj["value50"]
      self.value51:str = obj["value51"]
      self.value52:str = obj["value52"]
      self.value53:str = obj["value53"]
      self.value54:str = obj["value54"]
      self.value55:str = obj["value55"]
      self.value56:str = obj["value56"]
      self.value57:str = obj["value57"]
      self.value58:str = obj["value58"]
      self.value59:str = obj["value59"]
      self.value60:str = obj["value60"]
      self.value61:str = obj["value61"]
      self.value62:str = obj["value62"]
      self.value63:str = obj["value63"]
      self.value64:str = obj["value64"]
      self.value65:str = obj["value65"]
      self.value66:str = obj["value66"]
      self.value67:str = obj["value67"]
      self.value68:str = obj["value68"]
      self.value69:str = obj["value69"]
      self.value70:str = obj["value70"]
      self.value71:str = obj["value71"]
      self.value72:str = obj["value72"]
      self.value73:str = obj["value73"]
      self.value74:str = obj["value74"]
      self.value75:str = obj["value75"]
      self.value76:str = obj["value76"]
      self.value77:str = obj["value77"]
      self.value78:str = obj["value78"]
      self.value79:str = obj["value79"]
      self.value80:str = obj["value80"]
      self.value81:str = obj["value81"]
      self.value82:str = obj["value82"]
      self.value83:str = obj["value83"]
      self.value84:str = obj["value84"]
      self.value85:str = obj["value85"]
      self.value86:str = obj["value86"]
      self.value87:str = obj["value87"]
      self.value88:str = obj["value88"]
      self.value89:str = obj["value89"]
      self.value90:str = obj["value90"]
      self.value91:str = obj["value91"]
      self.value92:str = obj["value92"]
      self.value93:str = obj["value93"]
      self.value94:str = obj["value94"]
      self.value95:str = obj["value95"]
      self.value96:str = obj["value96"]
      self.value97:str = obj["value97"]
      self.value98:str = obj["value98"]
      self.value99:str = obj["value99"]
      self.seqId:int = obj["seqId"]
      self.tblname:str = obj["tblname"]
      """  name of tab control record is displayed on  """  
      self.UpdXml:str = obj["UpdXml"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataCheckTableset:
   def __init__(self, obj):
      self.DataCheck:list[Erp_Tablesets_DataCheckRow] = obj["DataCheck"]
      self.DataCheckDDef:list[Erp_Tablesets_DataCheckDDefRow] = obj["DataCheckDDef"]
      self.DataCheckParam:list[Erp_Tablesets_DataCheckParamRow] = obj["DataCheckParam"]
      self.DataCheckRpt:list[Erp_Tablesets_DataCheckRptRow] = obj["DataCheckRpt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DataChecklistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDataCheckTableset:
   def __init__(self, obj):
      self.DataCheck:list[Erp_Tablesets_DataCheckRow] = obj["DataCheck"]
      self.DataCheckDDef:list[Erp_Tablesets_DataCheckDDefRow] = obj["DataCheckDDef"]
      self.DataCheckParam:list[Erp_Tablesets_DataCheckParamRow] = obj["DataCheckParam"]
      self.DataCheckRpt:list[Erp_Tablesets_DataCheckRptRow] = obj["DataCheckRpt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateParameterComponents_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

class GenerateParameterComponents_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetByIDCustom_input:
   """ Required : 
   DataCheckId
   PageSize
   """  
   def __init__(self, obj):
      self.DataCheckId:str = obj["DataCheckId"]
      """  The Data Fix Id  """  
      self.PageSize:int = obj["PageSize"]
      """  number of report records to return  """  
      pass

class GetByIDCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataCheckTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   company
   localName
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataCheckTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DataCheckTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DataCheckTableset] = obj["returnObj"]
      pass

class GetCompanies_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.companies:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCurrentInstallation_input:
   """ Required : 
   TenantID
   InstallationID
   """  
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  Tenant Id  """  
      self.InstallationID:str = obj["InstallationID"]
      """  Installation ID  """  
      pass

class GetCurrentInstallation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.TenantID:str = obj["parameters"]
      self.InstallationID:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_DataCheckListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDataCheck_input:
   """ Required : 
   ds
   company
   localName
   key1
   key2
   key3
   key4
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      pass

class GetNewDataCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   dataCheckWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.dataCheckWhereClause:str = obj["dataCheckWhereClause"]
      """  where clause for data fixes  """  
      self.pageSize:int = obj["pageSize"]
      """  pagesize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page size  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataCheckTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDataCheck
   whereClauseDataCheckDDef
   whereClauseDataCheckParam
   whereClauseDataCheckRpt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDataCheck:str = obj["whereClauseDataCheck"]
      self.whereClauseDataCheckDDef:str = obj["whereClauseDataCheckDDef"]
      self.whereClauseDataCheckParam:str = obj["whereClauseDataCheckParam"]
      self.whereClauseDataCheckRpt:str = obj["whereClauseDataCheckRpt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataCheckTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTenants_input:
   """ Required : 
   Tenants
   InstallationIDs
   """  
   def __init__(self, obj):
      self.Tenants:str = obj["Tenants"]
      """  Tenants  """  
      self.InstallationIDs:str = obj["InstallationIDs"]
      """  Installation IDs  """  
      pass

class GetTenants_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.Tenants:str = obj["parameters"]
      self.InstallationIDs:str = obj["parameters"]
      pass

      """  output parameters  """  

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

class SelectAll_input:
   """ Required : 
   DataCheckId
   ds
   """  
   def __init__(self, obj):
      self.DataCheckId:str = obj["DataCheckId"]
      """  Data Fix Id  """  
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

class SelectAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartCheck_input:
   """ Required : 
   SysRowId
   DataCheckId
   DataCheckSPName
   InstallationID
   PageSize
   agentID
   ds
   """  
   def __init__(self, obj):
      self.SysRowId:str = obj["SysRowId"]
      """  SysRowId of Data Fix record  """  
      self.DataCheckId:str = obj["DataCheckId"]
      """  Data Check ID  """  
      self.DataCheckSPName:str = obj["DataCheckSPName"]
      """  Data Check Stored Procedure  """  
      self.InstallationID:str = obj["InstallationID"]
      """  Installation ID of tenant  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of Records to return  """  
      self.agentID:str = obj["agentID"]
      """  Task Agent  """  
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

class StartCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnSelectAll_input:
   """ Required : 
   DataCheckId
   ds
   """  
   def __init__(self, obj):
      self.DataCheckId:str = obj["DataCheckId"]
      """  Data Fix Id  """  
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

class UnSelectAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateCheck_input:
   """ Required : 
   SysRowId
   DataCheckId
   DataCheckSPName
   PageSize
   ds
   """  
   def __init__(self, obj):
      self.SysRowId:str = obj["SysRowId"]
      """  SysRowId of Data Fix record  """  
      self.DataCheckId:str = obj["DataCheckId"]
      """  Data Check ID  """  
      self.DataCheckSPName:str = obj["DataCheckSPName"]
      """  Data Check Stored Procedure  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of Records to return  """  
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

class UpdateCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDataCheckTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDataCheckTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

