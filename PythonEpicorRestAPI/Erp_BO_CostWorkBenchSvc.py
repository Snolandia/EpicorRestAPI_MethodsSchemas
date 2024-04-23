import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CostWorkBenchSvc
# Description: Costing work bench
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CostWorkBenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostWorkBenches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches",headers=creds) as resp:
           return await resp.json()

async def post_CostWorkBenches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostWorkBenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CostGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostWorkBench item
   Description: Calls GetByID to retrieve the CostWorkBench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CostWorkBenches_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CostWorkBench for the service
   Description: Calls UpdateExt to update CostWorkBench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CostWorkBenches_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CostWorkBench item
   Description: Call UpdateExt to delete CostWorkBench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches_Company_GroupID_CostBurdens(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CostBurdens items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CostBurdens1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostBurdenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostBurdens",headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches_Company_GroupID_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostBurden item
   Description: Calls GetByID to retrieve the CostBurden item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostBurden1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostBurdenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches_Company_GroupID_CostLabors(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CostLabors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CostLabors1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostLaborRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostLabors",headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches_Company_GroupID_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostLabor item
   Description: Calls GetByID to retrieve the CostLabor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostLabor1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostLaborRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches_Company_GroupID_CostParts(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CostParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CostParts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostParts",headers=creds) as resp:
           return await resp.json()

async def get_CostWorkBenches_Company_GroupID_CostParts_Company_GroupID_TypeCode_PartNum(Company, GroupID, TypeCode, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostPart item
   Description: Calls GetByID to retrieve the CostPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostPart1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CostBurdens(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CostBurdens items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostBurdens
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostBurdenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens",headers=creds) as resp:
           return await resp.json()

async def post_CostBurdens(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostBurdens
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostBurdenRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CostBurdenRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostBurden item
   Description: Calls GetByID to retrieve the CostBurden item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostBurden
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostBurdenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CostBurden for the service
   Description: Calls UpdateExt to update CostBurden. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostBurden
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostBurdenRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CostBurden item
   Description: Call UpdateExt to delete CostBurden item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostBurden
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CostLabors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CostLabors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostLabors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostLaborRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors",headers=creds) as resp:
           return await resp.json()

async def post_CostLabors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostLabors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostLaborRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CostLaborRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostLabor item
   Description: Calls GetByID to retrieve the CostLabor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostLabor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostLaborRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CostLabor for the service
   Description: Calls UpdateExt to update CostLabor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostLabor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostLaborRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company, GroupID, RateSourceTableName, SourceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CostLabor item
   Description: Call UpdateExt to delete CostLabor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostLabor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param RateSourceTableName: Desc: RateSourceTableName   Required: True   Allow empty value : True
      :param SourceID: Desc: SourceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CostParts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CostParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostParts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts",headers=creds) as resp:
           return await resp.json()

async def post_CostParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CostPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CostParts_Company_GroupID_TypeCode_PartNum(Company, GroupID, TypeCode, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostPart item
   Description: Calls GetByID to retrieve the CostPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CostParts_Company_GroupID_TypeCode_PartNum(Company, GroupID, TypeCode, PartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CostPart for the service
   Description: Calls UpdateExt to update CostPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CostParts_Company_GroupID_TypeCode_PartNum(Company, GroupID, TypeCode, PartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CostPart item
   Description: Call UpdateExt to delete CostPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCostGrp, whereClauseCostBurden, whereClauseCostLabor, whereClauseCostPart, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCostGrp=" + whereClauseCostGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCostBurden=" + whereClauseCostBurden
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCostLabor=" + whereClauseCostLabor
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCostPart=" + whereClauseCostPart
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Descripotion List
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCopyFromGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCopyFromGroupID
   Description: Method to call when changing the copy from group id on the cost group.  Validates the
group id and updates CostGrp with default values based on the new group id.
   OperationID: ChangeCopyFromGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCopyFromGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCopyFromGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCopyFromPlantCostID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCopyFromPlantCostID
   Description: Method to call when changing the copy from plant cost id on the cost group.  Validates the
plant cost id and updates CostGrp with default values based on the new plant cost id.
   OperationID: ChangeCopyFromPlantCostID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCopyFromPlantCostID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCopyFromPlantCostID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCWBPostPostToPlantCostID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCWBPostPostToPlantCostID
   Description: Method to call when changing the post to cost id on the post cost table (CostWorkBenchPost).
Validates the plant cost id recreates CostWorkBenchPostPlants records for
the new cost id.
Prior to calling this method all CostWorkBenchPostPlants records must have the
RowMod value set to U because they will be deleted.
   OperationID: ChangeCWBPostPostToPlantCostID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCWBPostPostToPlantCostID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCWBPostPostToPlantCostID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePrimaryPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePrimaryPlant
   Description: Method to call when changing the primary plant on the cost group.  Validates the plant id
and updates CostGrp with default values based on the new plant.
   OperationID: ChangePrimaryPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePrimaryPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrimaryPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CostPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CostPost
   Description: Post costs for the group.
   OperationID: CostPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CostPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CostPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CostRollUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CostRollUp
   Description: Roll up costs for the group.
   OperationID: CostRollUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CostRollUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CostRollUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DEGetImportRatesLockStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DEGetImportRatesLockStatus
   Description: Parameters:  none
   OperationID: DEGetImportRatesLockStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DEGetImportRatesLockStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DEGetImportRatesLockStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostSet
   Description: This method creates/refreshes the costs for the Cost Group.
   OperationID: GetCostSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostWBInternalPrices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostWBInternalPrices
   Description: This method will create an empty CostWBInternalPrices record to use in
populating the parameters required to update the internal prices
The WorkstationID, DateFormat and NumericFormat fields are not user updatable
The Action field is one of 3 values 'All' = 'Calculate, Print, Update', 'Print' = 'Calculate, Print', 'Update' = 'Calculate, Update'
   OperationID: GetCostWBInternalPrices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostWBInternalPrices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWBInternalPrices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostWorkBenchCostSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostWorkBenchCostSet
   Description: This method will create a CostWorkbenchCostSet record which is used to store
user options for the getting the CostPart, CostLabor, and CostBurden records.
   OperationID: GetCostWorkBenchCostSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchCostSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchCostSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostWorkBenchPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostWorkBenchPost
   Description: This method will create a CostWorkbenchPost record which is used to store
user options for the Post option.
   OperationID: GetCostWorkBenchPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostWorkBenchRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostWorkBenchRefresh
   Description: This method will create a CostWorkbenchRefresh record which is used to store
user options for refreshing costs in the CostPart, CostLabor, and CostBurden records.
   OperationID: GetCostWorkBenchRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostWorkBenchRollUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostWorkBenchRollUp
   Description: This method will create a CostWorkbenchRollUp record which is used to store
user options for the rollup option.
   OperationID: GetCostWorkBenchRollUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchRollUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchRollUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ListCostingEdits(epicorHeaders = None):
   """  
   Summary: Invoke method ListCostingEdits
   Description: Returns the list for Costing Edits.  The list is in
code1`desc1~code2`desc2 format.
   OperationID: ListCostingEdits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListCostingEdits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ListFilters(epicorHeaders = None):
   """  
   Summary: Invoke method ListFilters
   Description: Returns the list for filter options for parts.  The list is in code1`desc1~code2`desc2 format.
   OperationID: ListFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListFilters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ListOprAndResourceSortBy(epicorHeaders = None):
   """  
   Summary: Invoke method ListOprAndResourceSortBy
   Description: Returns the list for sort by options for Operations and Resource Groups.
The list is in code1`desc1~code2`desc2 format.
   OperationID: ListOprAndResourceSortBy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOprAndResourceSortBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ListPartCostingMethod(epicorHeaders = None):
   """  
   Summary: Invoke method ListPartCostingMethod
   Description: Returns the list of available costing methods for a part.  The list is in
code1`desc1~code2`desc2 format.
   OperationID: ListPartCostingMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListPartCostingMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ListPartSortBy(epicorHeaders = None):
   """  
   Summary: Invoke method ListPartSortBy
   Description: Returns the list for sort by options for parts.  The list is in code1`desc1~code2`desc2 format.
   OperationID: ListPartSortBy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListPartSortBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ListRates(epicorHeaders = None):
   """  
   Summary: Invoke method ListRates
   Description: Returns the list of available rates for Resource Groups and Operations.  The list is in
code1`desc1~code2`desc2 format.
   OperationID: ListRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_PreCostRollUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCostRollUp
   Description: Pre-processing before the rolling up of costs for the group.
Check if there are unapproved revisions that are in the rollup criteria.  If
there are, return a message to the UI to ask the user if it is ok to proceed.  If
pcQuestion is blank, a question does not need to be asked.
   OperationID: PreCostRollUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCostRollUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCostRollUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshCosts
   Description: This method refreshes the costs for the Cost Group.
   OperationID: RefreshCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ViewCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ViewCosts
   Description: This method will return the data need to display Part Rev costs.
   OperationID: ViewCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ViewCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ViewCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCostGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCostGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCostGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCostBurden(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCostBurden
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostBurden
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCostBurden_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostBurden_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCostLabor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCostLabor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostLabor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCostLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCostPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCostPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCostPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostBurdenRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CostBurdenRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CostGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CostGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostLaborRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CostLaborRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CostPartRow] = obj["value"]
      pass

class Erp_Tablesets_CostBurdenRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.RateSourceTableName:str = obj["RateSourceTableName"]
      """  Indicates the source table name of the labor rates.  """  
      self.SourceID:str = obj["SourceID"]
      """  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  """  
      self.Description:str = obj["Description"]
      """  The description of SourceID.  Will be the description from Resource or ResourceGroup.  """  
      self.BurdenType:str = obj["BurdenType"]
      """  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispTableName:str = obj["DispTableName"]
      self.BurdenDesc:str = obj["BurdenDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BOMRollupDate:str = obj["BOMRollupDate"]
      """  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this cost group.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  """  
      self.Comment:str = obj["Comment"]
      """   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  """  
      self.LastPartRefresh:str = obj["LastPartRefresh"]
      """  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.LastWCRefresh:str = obj["LastWCRefresh"]
      """  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.Burden:str = obj["Burden"]
      """  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicated the group has been posted.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that posted this cost group.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Group posted date.  """  
      self.Labor:str = obj["Labor"]
      """  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.LastOPRefresh:str = obj["LastOPRefresh"]
      """  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      """  The primary Site for the cost group.  """  
      self.LoadAltMethod:bool = obj["LoadAltMethod"]
      """  Load Alternate Method  """  
      self.LoadCostLot:bool = obj["LoadCostLot"]
      """  Load Costing Lot Sizes  """  
      self.CopyFromPlantCostID:str = obj["CopyFromPlantCostID"]
      """  The Site Cost ID to copy costs from  """  
      self.CopyFromGroupID:str = obj["CopyFromGroupID"]
      """  The Cost Group to copy costs from  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CopyFromGroupDesc:str = obj["CopyFromGroupDesc"]
      self.EnableCostMethod:bool = obj["EnableCostMethod"]
      self.InternalPricePctChange:int = obj["InternalPricePctChange"]
      self.CopyFromPlantCostDescription:str = obj["CopyFromPlantCostDescription"]
      """  Description  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BOMRollupDate:str = obj["BOMRollupDate"]
      """  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this cost group.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  """  
      self.Comment:str = obj["Comment"]
      """   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  """  
      self.LastPartRefresh:str = obj["LastPartRefresh"]
      """  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.LastWCRefresh:str = obj["LastWCRefresh"]
      """  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.Burden:str = obj["Burden"]
      """  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicated the group has been posted.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that posted this cost group.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Group posted date.  """  
      self.Labor:str = obj["Labor"]
      """  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.LastOPRefresh:str = obj["LastOPRefresh"]
      """  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      """  The primary Site for the cost group.  """  
      self.LoadAltMethod:bool = obj["LoadAltMethod"]
      """  Load Alternate Method  """  
      self.LoadCostLot:bool = obj["LoadCostLot"]
      """  Load Costing Lot Sizes  """  
      self.CopyFromPlantCostID:str = obj["CopyFromPlantCostID"]
      """  The Site Cost ID to copy costs from  """  
      self.CopyFromGroupID:str = obj["CopyFromGroupID"]
      """  The Cost Group to copy costs from  """  
      self.DEImportRateStatus:bool = obj["DEImportRateStatus"]
      """  Flag used to indicate the status of the Import Rates process, if it finished succesfully for the Costing WorkBench Group or did not  """  
      self.DEImpRtsLockStatus:bool = obj["DEImpRtsLockStatus"]
      """  Flag used to indicate that the Import Rates process is active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CopyFromGroupDesc:str = obj["CopyFromGroupDesc"]
      self.DERatesImported:bool = obj["DERatesImported"]
      """  DE Rates Imported flag  """  
      self.EnableCostMethod:bool = obj["EnableCostMethod"]
      self.InternalPricePctChange:int = obj["InternalPricePctChange"]
      self.BitFlag:int = obj["BitFlag"]
      self.CopyFromPlantCostDescription:str = obj["CopyFromPlantCostDescription"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostLaborRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.RateSourceTableName:str = obj["RateSourceTableName"]
      """  Indicates the source table name of the labor rates.  """  
      self.SourceID:str = obj["SourceID"]
      """  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  """  
      self.Description:str = obj["Description"]
      """  The description of SourceID.  Will be the description from Resource or ResourceGroup.  """  
      self.SetupLRate:int = obj["SetupLRate"]
      """  The labor rate used for setup time.  """  
      self.ProdLRate:int = obj["ProdLRate"]
      """  Labor rate used for production time on an operation.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispTableName:str = obj["DispTableName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """   Standard Burden Unit Cost.

( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """   Standard Material Unit cost.

( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimCostPart:str = obj["PrimCostPart"]
      """  PrimCostPart  """  
      self.PrimCostRev:str = obj["PrimCostRev"]
      """  PrimCostRev  """  
      self.PrimCostAltMethod:str = obj["PrimCostAltMethod"]
      """  PrimCostAltMethod  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  CoPartsReqQty  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  MtlCostPct  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  LaborCostPct  """  
      self.OrigStdMaterialCost:int = obj["OrigStdMaterialCost"]
      """  OrigStdMaterialCost  """  
      self.OrigStdLaborCost:int = obj["OrigStdLaborCost"]
      """  OrigStdLaborCost  """  
      self.OrigStdBurdenCost:int = obj["OrigStdBurdenCost"]
      """  OrigStdBurdenCost  """  
      self.OrigStdSubContCost:int = obj["OrigStdSubContCost"]
      """  OrigStdSubContCost  """  
      self.OrigStdMtlBurCost:int = obj["OrigStdMtlBurCost"]
      """  OrigStdMtlBurCost  """  
      self.IsTransferCostID:bool = obj["IsTransferCostID"]
      """  IsTransferCostID  """  
      self.ApprovedMethod:bool = obj["ApprovedMethod"]
      self.CurrentRevDescription:str = obj["CurrentRevDescription"]
      self.CurrentRevisionNum:str = obj["CurrentRevisionNum"]
      self.IsMethod:bool = obj["IsMethod"]
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCWBPostPostToPlantCostID_input:
   """ Required : 
   ProposedPlantCostID
   ds
   """  
   def __init__(self, obj):
      self.ProposedPlantCostID:str = obj["ProposedPlantCostID"]
      """  The proposed plant cost id  """  
      self.ds:list[Erp_Tablesets_CostWorkBenchPostTableset] = obj["ds"]
      pass

class ChangeCWBPostPostToPlantCostID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchPostTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCopyFromGroupID_input:
   """ Required : 
   ProposedGroupID
   ds
   """  
   def __init__(self, obj):
      self.ProposedGroupID:str = obj["ProposedGroupID"]
      """  The proposed plant cost id  """  
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

class ChangeCopyFromGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCopyFromPlantCostID_input:
   """ Required : 
   ProposedPlantCostID
   ds
   """  
   def __init__(self, obj):
      self.ProposedPlantCostID:str = obj["ProposedPlantCostID"]
      """  The proposed plant cost id  """  
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

class ChangeCopyFromPlantCostID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePrimaryPlant_input:
   """ Required : 
   ProposedPlant
   ds
   """  
   def __init__(self, obj):
      self.ProposedPlant:str = obj["ProposedPlant"]
      """  The proposed plant  """  
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

class ChangePrimaryPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CostPost_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchPostTableset] = obj["ds"]
      pass

class CostPost_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchPostTableset] = obj["ds"]
      self.pcCostsNotUpdatedMsg:str = obj["parameters"]
      self.pcLegalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CostRollUp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchRollUpTableset] = obj["ds"]
      pass

class CostRollUp_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchRollUpTableset] = obj["ds"]
      self.pcPartsNotUpdatedMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class DEGetImportRatesLockStatus_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DEGetImportRatesLockStatus_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CostBurdenRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.RateSourceTableName:str = obj["RateSourceTableName"]
      """  Indicates the source table name of the labor rates.  """  
      self.SourceID:str = obj["SourceID"]
      """  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  """  
      self.Description:str = obj["Description"]
      """  The description of SourceID.  Will be the description from Resource or ResourceGroup.  """  
      self.BurdenType:str = obj["BurdenType"]
      """  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispTableName:str = obj["DispTableName"]
      self.BurdenDesc:str = obj["BurdenDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BOMRollupDate:str = obj["BOMRollupDate"]
      """  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this cost group.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  """  
      self.Comment:str = obj["Comment"]
      """   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  """  
      self.LastPartRefresh:str = obj["LastPartRefresh"]
      """  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.LastWCRefresh:str = obj["LastWCRefresh"]
      """  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.Burden:str = obj["Burden"]
      """  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicated the group has been posted.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that posted this cost group.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Group posted date.  """  
      self.Labor:str = obj["Labor"]
      """  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.LastOPRefresh:str = obj["LastOPRefresh"]
      """  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      """  The primary Site for the cost group.  """  
      self.LoadAltMethod:bool = obj["LoadAltMethod"]
      """  Load Alternate Method  """  
      self.LoadCostLot:bool = obj["LoadCostLot"]
      """  Load Costing Lot Sizes  """  
      self.CopyFromPlantCostID:str = obj["CopyFromPlantCostID"]
      """  The Site Cost ID to copy costs from  """  
      self.CopyFromGroupID:str = obj["CopyFromGroupID"]
      """  The Cost Group to copy costs from  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CopyFromGroupDesc:str = obj["CopyFromGroupDesc"]
      self.EnableCostMethod:bool = obj["EnableCostMethod"]
      self.InternalPricePctChange:int = obj["InternalPricePctChange"]
      self.CopyFromPlantCostDescription:str = obj["CopyFromPlantCostDescription"]
      """  Description  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostGrpListTableset:
   def __init__(self, obj):
      self.CostGrpList:list[Erp_Tablesets_CostGrpListRow] = obj["CostGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BOMRollupDate:str = obj["BOMRollupDate"]
      """  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this cost group.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  """  
      self.Comment:str = obj["Comment"]
      """   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  """  
      self.LastPartRefresh:str = obj["LastPartRefresh"]
      """  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.LastWCRefresh:str = obj["LastWCRefresh"]
      """  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  """  
      self.Burden:str = obj["Burden"]
      """  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicated the group has been posted.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user ID that posted this cost group.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Group posted date.  """  
      self.Labor:str = obj["Labor"]
      """  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  """  
      self.LastOPRefresh:str = obj["LastOPRefresh"]
      """  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      """  The primary Site for the cost group.  """  
      self.LoadAltMethod:bool = obj["LoadAltMethod"]
      """  Load Alternate Method  """  
      self.LoadCostLot:bool = obj["LoadCostLot"]
      """  Load Costing Lot Sizes  """  
      self.CopyFromPlantCostID:str = obj["CopyFromPlantCostID"]
      """  The Site Cost ID to copy costs from  """  
      self.CopyFromGroupID:str = obj["CopyFromGroupID"]
      """  The Cost Group to copy costs from  """  
      self.DEImportRateStatus:bool = obj["DEImportRateStatus"]
      """  Flag used to indicate the status of the Import Rates process, if it finished succesfully for the Costing WorkBench Group or did not  """  
      self.DEImpRtsLockStatus:bool = obj["DEImpRtsLockStatus"]
      """  Flag used to indicate that the Import Rates process is active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CopyFromGroupDesc:str = obj["CopyFromGroupDesc"]
      self.DERatesImported:bool = obj["DERatesImported"]
      """  DE Rates Imported flag  """  
      self.EnableCostMethod:bool = obj["EnableCostMethod"]
      self.InternalPricePctChange:int = obj["InternalPricePctChange"]
      self.BitFlag:int = obj["BitFlag"]
      self.CopyFromPlantCostDescription:str = obj["CopyFromPlantCostDescription"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostLaborRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.RateSourceTableName:str = obj["RateSourceTableName"]
      """  Indicates the source table name of the labor rates.  """  
      self.SourceID:str = obj["SourceID"]
      """  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  """  
      self.Description:str = obj["Description"]
      """  The description of SourceID.  Will be the description from Resource or ResourceGroup.  """  
      self.SetupLRate:int = obj["SetupLRate"]
      """  The labor rate used for setup time.  """  
      self.ProdLRate:int = obj["ProdLRate"]
      """  Labor rate used for production time on an operation.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispTableName:str = obj["DispTableName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """   Standard Burden Unit Cost.

( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """   Standard Material Unit cost.

( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimCostPart:str = obj["PrimCostPart"]
      """  PrimCostPart  """  
      self.PrimCostRev:str = obj["PrimCostRev"]
      """  PrimCostRev  """  
      self.PrimCostAltMethod:str = obj["PrimCostAltMethod"]
      """  PrimCostAltMethod  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  CoPartsReqQty  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  MtlCostPct  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  LaborCostPct  """  
      self.OrigStdMaterialCost:int = obj["OrigStdMaterialCost"]
      """  OrigStdMaterialCost  """  
      self.OrigStdLaborCost:int = obj["OrigStdLaborCost"]
      """  OrigStdLaborCost  """  
      self.OrigStdBurdenCost:int = obj["OrigStdBurdenCost"]
      """  OrigStdBurdenCost  """  
      self.OrigStdSubContCost:int = obj["OrigStdSubContCost"]
      """  OrigStdSubContCost  """  
      self.OrigStdMtlBurCost:int = obj["OrigStdMtlBurCost"]
      """  OrigStdMtlBurCost  """  
      self.IsTransferCostID:bool = obj["IsTransferCostID"]
      """  IsTransferCostID  """  
      self.ApprovedMethod:bool = obj["ApprovedMethod"]
      self.CurrentRevDescription:str = obj["CurrentRevDescription"]
      self.CurrentRevisionNum:str = obj["CurrentRevisionNum"]
      self.IsMethod:bool = obj["IsMethod"]
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostWBInternalPricesPartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.PctChg:int = obj["PctChg"]
      self.WorkstationID:str = obj["WorkstationID"]
      self.DateFormat:str = obj["DateFormat"]
      self.NumericFormat:str = obj["NumericFormat"]
      self.Action:str = obj["Action"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostWBInternalPricesTableset:
   def __init__(self, obj):
      self.CostWBInternalPricesParts:list[Erp_Tablesets_CostWBInternalPricesPartsRow] = obj["CostWBInternalPricesParts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostWorkBenchCostSetRow:
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      self.EffectivityDate:str = obj["EffectivityDate"]
      self.LastPartRefreshDate:str = obj["LastPartRefreshDate"]
      self.GetManufacturingParts:bool = obj["GetManufacturingParts"]
      self.GetPurchasedParts:bool = obj["GetPurchasedParts"]
      self.GetOperations:bool = obj["GetOperations"]
      self.GetResourceGroups:bool = obj["GetResourceGroups"]
      self.RefreshAllCosts:bool = obj["RefreshAllCosts"]
      self.PartList:str = obj["PartList"]
      self.ProdGroupList:str = obj["ProdGroupList"]
      self.PartClassList:str = obj["PartClassList"]
      self.PartCostMethod:str = obj["PartCostMethod"]
      self.BurdenCostMethod:str = obj["BurdenCostMethod"]
      self.LaborCostMethod:str = obj["LaborCostMethod"]
      self.GetUnlinkedPurchasedParts:bool = obj["GetUnlinkedPurchasedParts"]
      self.GetUnlinkedRates:bool = obj["GetUnlinkedRates"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostWorkBenchCostSetTableset:
   def __init__(self, obj):
      self.CostWorkBenchCostSet:list[Erp_Tablesets_CostWorkBenchCostSetRow] = obj["CostWorkBenchCostSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostWorkBenchCostsTableset:
   def __init__(self, obj):
      self.PartRevCosts:list[Erp_Tablesets_PartRevCostsRow] = obj["PartRevCosts"]
      self.PartRevCostsDetail:list[Erp_Tablesets_PartRevCostsDetailRow] = obj["PartRevCostsDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostWorkBenchPostPlantsRow:
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      self.Plant:str = obj["Plant"]
      self.Name:str = obj["Name"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostWorkBenchPostRow:
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      self.PartList:str = obj["PartList"]
      """  Delimited list of Parts to run the post for  """  
      self.ProdGrupList:str = obj["ProdGrupList"]
      """  Delimited list of Prod Groups to run the rollup for  """  
      self.PartClassList:str = obj["PartClassList"]
      """  Delimited list of Part Classes to run the rollup for  """  
      self.ReasonCode:str = obj["ReasonCode"]
      self.EnableReasonCode:bool = obj["EnableReasonCode"]
      self.PostToPlantCostID:str = obj["PostToPlantCostID"]
      self.PostBurden:bool = obj["PostBurden"]
      self.PostLabor:bool = obj["PostLabor"]
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostWorkBenchPostTableset:
   def __init__(self, obj):
      self.CostWorkBenchPost:list[Erp_Tablesets_CostWorkBenchPostRow] = obj["CostWorkBenchPost"]
      self.CostWorkBenchPostPlants:list[Erp_Tablesets_CostWorkBenchPostPlantsRow] = obj["CostWorkBenchPostPlants"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostWorkBenchRefreshRow:
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      self.RefreshPurchasedParts:bool = obj["RefreshPurchasedParts"]
      self.PartCostMethod:str = obj["PartCostMethod"]
      self.RefreshLaborRates:bool = obj["RefreshLaborRates"]
      self.LaborCostMethod:str = obj["LaborCostMethod"]
      self.RefreshBurdenRates:bool = obj["RefreshBurdenRates"]
      self.BurdenCostMethod:str = obj["BurdenCostMethod"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostWorkBenchRefreshTableset:
   def __init__(self, obj):
      self.CostWorkBenchRefresh:list[Erp_Tablesets_CostWorkBenchRefreshRow] = obj["CostWorkBenchRefresh"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostWorkBenchRollUpRow:
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      self.EffectivityDate:str = obj["EffectivityDate"]
      self.PartList:str = obj["PartList"]
      """  Delimited list of Parts to run the rollup for  """  
      self.ProdGrupList:str = obj["ProdGrupList"]
      """  Delimited list of Product Groups to run the rollup for  """  
      self.PartClassList:str = obj["PartClassList"]
      """  Delimited list of Part Classes to run the rollup for  """  
      self.ConsiderPullAsAsmSettings:bool = obj["ConsiderPullAsAsmSettings"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostWorkBenchRollUpTableset:
   def __init__(self, obj):
      self.CostWorkBenchRollUp:list[Erp_Tablesets_CostWorkBenchRollUpRow] = obj["CostWorkBenchRollUp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostWorkBenchTableset:
   def __init__(self, obj):
      self.CostGrp:list[Erp_Tablesets_CostGrpRow] = obj["CostGrp"]
      self.CostBurden:list[Erp_Tablesets_CostBurdenRow] = obj["CostBurden"]
      self.CostLabor:list[Erp_Tablesets_CostLaborRow] = obj["CostLabor"]
      self.CostPart:list[Erp_Tablesets_CostPartRow] = obj["CostPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartRevCostsDetailRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity  """  
      self.Approved:bool = obj["Approved"]
      """  Is this approved?  """  
      self.BOMType:str = obj["BOMType"]
      """  The BOM type  """  
      self.BOMLevel:int = obj["BOMLevel"]
      """  The BOM Level  """  
      self.MtlRevision:str = obj["MtlRevision"]
      """  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.MaterialCost:int = obj["MaterialCost"]
      """  The material cost  """  
      self.LaborCost:int = obj["LaborCost"]
      """  The labor cost  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  The burden cost  """  
      self.SubcontractCost:int = obj["SubcontractCost"]
      """  The subcontract cost  """  
      self.MaterialBurdenCost:int = obj["MaterialBurdenCost"]
      """  The material burden cost  """  
      self.TotalCost:int = obj["TotalCost"]
      """  The total cost  """  
      self.MaterialUnitCost:int = obj["MaterialUnitCost"]
      """  The material unit cost  """  
      self.LaborUnitCost:int = obj["LaborUnitCost"]
      """  The labor unit cost  """  
      self.BurdenUnitCost:int = obj["BurdenUnitCost"]
      """  The burden unit cost  """  
      self.SubcontractUnitCost:int = obj["SubcontractUnitCost"]
      """  The subcontract unit cost  """  
      self.MaterialBurdenUnitCost:int = obj["MaterialBurdenUnitCost"]
      """  The material burden unit cost  """  
      self.TotalUnitCost:int = obj["TotalUnitCost"]
      """  The total unit cost  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The quantity per parent  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The effective date  """  
      self.BomSequence:int = obj["BomSequence"]
      """  The BOM Sequence  """  
      self.Company:str = obj["Company"]
      """  The company id.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  The Alternate Method  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevCostsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company id.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The effective date  """  
      self.MaxLevel:int = obj["MaxLevel"]
      """  The maximum level  """  
      self.AssembliesOnly:bool = obj["AssembliesOnly"]
      """  Assemblies Only flag  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity  """  
      self.MaterialTotalCost:int = obj["MaterialTotalCost"]
      """  The material total cost.  """  
      self.MaterialUnitCost:int = obj["MaterialUnitCost"]
      """  The material unit cost  """  
      self.MaterialPartCost:int = obj["MaterialPartCost"]
      """  The material part cost  """  
      self.LaborTotalCost:int = obj["LaborTotalCost"]
      """  The labor total cost  """  
      self.LaborUnitCost:int = obj["LaborUnitCost"]
      """  The unit cost of labor  """  
      self.LaborPartCost:int = obj["LaborPartCost"]
      """  The part cost of labor  """  
      self.BurdenTotalCost:int = obj["BurdenTotalCost"]
      """  The burden total cost  """  
      self.BurdenUnitCost:int = obj["BurdenUnitCost"]
      """  The burden unit cost  """  
      self.BurdenPartCost:int = obj["BurdenPartCost"]
      """  The burden part cost  """  
      self.SubcontractTotalCost:int = obj["SubcontractTotalCost"]
      """  The subcontract total cost  """  
      self.SubcontractUnitCost:int = obj["SubcontractUnitCost"]
      """  The subcontract unit cost  """  
      self.SubcontractPartCost:int = obj["SubcontractPartCost"]
      """  The subcontract part cost  """  
      self.MtlBurdenTotalCost:int = obj["MtlBurdenTotalCost"]
      """  The material burden total cost  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  The material burden unit cost  """  
      self.MtlBurdenPartCost:int = obj["MtlBurdenPartCost"]
      """  The material burden part cost  """  
      self.CostMethodLabel:str = obj["CostMethodLabel"]
      """  The cost method label  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  The alternate method  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCostWorkBenchTableset:
   def __init__(self, obj):
      self.CostGrp:list[Erp_Tablesets_CostGrpRow] = obj["CostGrp"]
      self.CostBurden:list[Erp_Tablesets_CostBurdenRow] = obj["CostBurden"]
      self.CostLabor:list[Erp_Tablesets_CostLaborRow] = obj["CostLabor"]
      self.CostPart:list[Erp_Tablesets_CostPartRow] = obj["CostPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCostSet_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchCostSetTableset] = obj["ds"]
      pass

class GetCostSet_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchCostSetTableset] = obj["ds"]
      self.cReturnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCostWBInternalPrices_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Group ID  """  
      pass

class GetCostWBInternalPrices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWBInternalPricesTableset] = obj["returnObj"]
      pass

class GetCostWorkBenchCostSet_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Group ID  """  
      pass

class GetCostWorkBenchCostSet_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchCostSetTableset] = obj["returnObj"]
      pass

class GetCostWorkBenchPost_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Group ID  """  
      pass

class GetCostWorkBenchPost_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchPostTableset] = obj["returnObj"]
      pass

class GetCostWorkBenchRefresh_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Group ID  """  
      pass

class GetCostWorkBenchRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchRefreshTableset] = obj["returnObj"]
      pass

class GetCostWorkBenchRollUp_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Group ID  """  
      pass

class GetCostWorkBenchRollUp_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchRollUpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CostGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCostBurden_input:
   """ Required : 
   ds
   groupID
   rateSourceTableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.rateSourceTableName:str = obj["rateSourceTableName"]
      pass

class GetNewCostBurden_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCostGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

class GetNewCostGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCostLabor_input:
   """ Required : 
   ds
   groupID
   rateSourceTableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.rateSourceTableName:str = obj["rateSourceTableName"]
      pass

class GetNewCostLabor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCostPart_input:
   """ Required : 
   ds
   groupID
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewCostPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCostGrp
   whereClauseCostBurden
   whereClauseCostLabor
   whereClauseCostPart
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCostGrp:str = obj["whereClauseCostGrp"]
      self.whereClauseCostBurden:str = obj["whereClauseCostBurden"]
      self.whereClauseCostLabor:str = obj["whereClauseCostLabor"]
      self.whereClauseCostPart:str = obj["whereClauseCostPart"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

class ListCostingEdits_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cCostingEditList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ListFilters_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cFilterList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ListOprAndResourceSortBy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOprResourceSortByList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ListPartCostingMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cPartCostingMethodList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ListPartSortBy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cPartSortByList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ListRates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cRatesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreCostRollUp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchRollUpTableset] = obj["ds"]
      pass

class PreCostRollUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchRollUpTableset] = obj["ds"]
      self.pcQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class RefreshCosts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchRefreshTableset] = obj["ds"]
      pass

class RefreshCosts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchRefreshTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCostWorkBenchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCostWorkBenchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ViewCosts_input:
   """ Required : 
   ipGroupID
   ipTypeCode
   ipPartNum
   ipQuantity
   ipMaxLevel
   ipAssembliesOnly
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Cost Group ID to return costs for.  """  
      self.ipTypeCode:str = obj["ipTypeCode"]
      """  The Type Code of the Part to return costs for (CostPart.TypeCode).  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return costs for.  """  
      self.ipQuantity:int = obj["ipQuantity"]
      """  The Quantity to return costs for.  """  
      self.ipMaxLevel:int = obj["ipMaxLevel"]
      """  The Max Level to return costs for.  """  
      self.ipAssembliesOnly:bool = obj["ipAssembliesOnly"]
      """  Assemblies only  """  
      pass

class ViewCosts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostWorkBenchCostsTableset] = obj["returnObj"]
      pass

