import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InspProcessingSvc
# Description: This object supports the following activities:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspProcessings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspProcessings
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspProcListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings_xID(xID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspProcessing item
   Description: Calls GetByID to retrieve the InspProcessing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspProcessing
      :param xID: Desc: xID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspProcListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings_xID_InspFirstArts(xID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspFirstArts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspFirstArts1
      :param xID: Desc: xID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspFirstArtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspFirstArts",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings_xID_InspFirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(xID, Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspFirstArt item
   Description: Calls GetByID to retrieve the InspFirstArt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspFirstArt1
      :param xID: Desc: xID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspFirstArtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspFirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings_xID_InspNonConfs(xID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspNonConfs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspNonConfs1
      :param xID: Desc: xID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspNonConfRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspNonConfs",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings_xID_InspNonConfs_Company_TranID(xID, Company, TranID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspNonConf item
   Description: Calls GetByID to retrieve the InspNonConf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspNonConf1
      :param xID: Desc: xID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspNonConfRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspNonConfs(" + Company + "," + TranID + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings_xID_InspRcpts(xID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspRcpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspRcpts1
      :param xID: Desc: xID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspRcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspRcpts",headers=creds) as resp:
           return await resp.json()

async def get_InspProcessings_xID_InspRcpts_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(xID, Company, VendorNum, PurPoint, PackSlip, PackLine, AttributeValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspRcpt item
   Description: Calls GetByID to retrieve the InspRcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspRcpt1
      :param xID: Desc: xID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspRcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspProcessings(" + xID + ")/InspRcpts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspFirstArts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspFirstArts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspFirstArts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspFirstArtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspFirstArts",headers=creds) as resp:
           return await resp.json()

async def get_InspFirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspFirstArt item
   Description: Calls GetByID to retrieve the InspFirstArt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspFirstArt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspFirstArtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspFirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspNonConfs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspNonConfs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspNonConfs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspNonConfRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspNonConfs",headers=creds) as resp:
           return await resp.json()

async def get_InspNonConfs_Company_TranID(Company, TranID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspNonConf item
   Description: Calls GetByID to retrieve the InspNonConf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspNonConf
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspNonConfRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspNonConfs(" + Company + "," + TranID + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspRcpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspRcpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspRcpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspRcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspRcpts",headers=creds) as resp:
           return await resp.json()

async def get_InspRcpts_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, AttributeValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspRcpt item
   Description: Calls GetByID to retrieve the InspRcpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspRcpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspRcptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/InspRcpts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_SupplierXRefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SupplierXRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SupplierXRefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierXRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs",headers=creds) as resp:
           return await resp.json()

async def get_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendNum, VendPartNum, MfgNum, MfgPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SupplierXRef item
   Description: Calls GetByID to retrieve the SupplierXRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SupplierXRef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendNum: Desc: VendNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(plOperation, plMaterial, plInventory, plFirstArt, plReceipt, plRMA, pcInspectorID, pcCutOffDate, whereClauseNonConf, whereClauseFirstArt, whereClauseRcvDtl, whereClauseRMA, whereClauseSelectedSerialNumbers, whereClauseSNFormat, whereClauseInspProcList, sortBy, pageSize, absolutePage, epicorHeaders = None):
   """  
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
      :param plOperation: Desc: If TRUE, include items that were sent to Inspection from a Job Operation.   Required: True
      :param plMaterial: Desc: If TRUE, include items that were sent to Inspection from a Job Material.   Required: True
      :param plInventory: Desc: If TRUE, include items that were sent to Inspection from Inventory.   Required: True
      :param plFirstArt: Desc: If TRUE, include items that were sent to Inspection from a First Article.   Required: True
      :param plReceipt: Desc: If TRUE, include items that were sent to Inspection from a PO or SubContract receipt.   Required: True
      :param plRMA: Desc: If TRUE, include items that were sent to Inspection from an RMA.   Required: True
      :param pcInspectorID: Desc: (optional) The Inspector ID typed in by the user.   Required: True   Allow empty value : True
      :param pcCutOffDate: Desc: (optional) Cut Off Date .   Required: True   Allow empty value : True
      :param whereClauseNonConf: Desc: (optional)Additional Where conditions for NonConf table.   Required: True   Allow empty value : True
      :param whereClauseFirstArt: Desc: (optional)Additional Where conditions for FirstArt table.   Required: True   Allow empty value : True
      :param whereClauseRcvDtl: Desc: (optional)Additional Where conditions for RcvDtl table.   Required: True   Allow empty value : True
      :param whereClauseRMA: Desc: (optional)Additional Where conditions for RMAHead table.   Required: True   Allow empty value : True
      :param whereClauseSelectedSerialNumbers: Desc: (optional)Additional Where conditions for SelectedSerialNumbers table.   Required: True   Allow empty value : True
      :param whereClauseSNFormat: Desc: (optional)Additional Where conditions for SNFormat table.   Required: True   Allow empty value : True
      :param whereClauseInspProcList: Desc: (optional)Additional Where conditions to be applied to result set.   Required: True   Allow empty value : True
      :param sortBy: Desc: Sort By selected in search   Required: True   Allow empty value : True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute page   Required: True
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
   params += "plOperation=" + plOperation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plMaterial=" + plMaterial
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plInventory=" + plInventory
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plFirstArt=" + plFirstArt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plReceipt=" + plReceipt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plRMA=" + plRMA
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pcInspectorID=" + pcInspectorID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pcCutOffDate=" + pcCutOffDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseNonConf=" + whereClauseNonConf
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFirstArt=" + whereClauseFirstArt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvDtl=" + whereClauseRcvDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRMA=" + whereClauseRMA
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspProcList=" + whereClauseInspProcList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sortBy=" + sortBy
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(pcTranID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: To retrieve the Inspection non conformance (InspProcessing dataset) corresponding to the
given TranID and the Operations tab or the Materials tab of the Inspections Processing
screen in Vantage v6.10.
   OperationID: Get_GetByID
      :param pcTranID: Desc: The TranID of the NonConformance.   Required: True
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
   params += "pcTranID=" + pcTranID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")" + params,headers=creds) as resp:
           return await resp.json()

async def post_AssignInspectorFar(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignInspectorNonConf(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignInspectorReceipt(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPlanningContractBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPlanningContractBin
   Description: Method to check Contract bin.
   OperationID: CheckPlanningContractBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlanningContractBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlanningContractBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSerialNumCount(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvQtysToBase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvQtysToBase
   Description: Convert Quantities to base qtys for serial number processing
   OperationID: ConvQtysToBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvQtysToBase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvQtysToBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDateUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDateUser
   Description: This method puts a date/time/user stamp in the text value for the user
   OperationID: GetDateUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDateUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFailedLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFirstArtByID(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInspRcptSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInspRcptSelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable for the InspRcpt RowIdent.
   OperationID: GetInspRcptSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspRcptSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspRcptSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInspResultsPassFail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInspResultsPassFail
   Description: This method will get the passed/failed quantity from InspResults for Non Conformance
   OperationID: GetInspResultsPassFail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspResultsPassFail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspResultsPassFail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNonConfPartTranPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNonConfPartTranPKs
   Description: Return Primary Keys for generated PartTran records.
   OperationID: GetNonConfPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNonConfPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNonConfPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlQueueSeqValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlQueueSeqValue
   Description: Search for the MtlQueueSeq value from the MtlQueue row related to the current Non Conformance.
   OperationID: GetMtlQueueSeqValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlQueueSeqValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueSeqValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPassedLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTranDocType(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReceiptByID(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReceiptPartTranPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReceiptPartTranPKs
   Description: Return Primary Keys for generated PartTran records.
   OperationID: GetReceiptPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReceiptPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceiptPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsLP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsLP
   Description: To retrieve the list of items waiting to be inspected (InspProcList dataset) on the Landing Page.
   OperationID: GetRowsLP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsLP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsLP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable for the InspNonConf RowIdent.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectFirstArt(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectInventory(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectInventory2(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectMaterial(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectMaterial2(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectOperation(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectOperation2(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectReceipt(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InspectReceipt2(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssemblySeq(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFailedQty(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFAInspectedQty(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIssueComplete(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobSeq(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMtlSeq(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePassedIssueTo(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePassedQty(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePassedWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePassedWhse
   OperationID: OnChangePassedWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePassedWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePassedWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCID
   Description: Validates that PCID exists
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: validates serial numbers entered on the generic serial number selection/create form called from the pass/fail form
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisplayWarnMsg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisplayWarnMsg
   OperationID: DisplayWarnMsg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisplayWarnMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisplayWarnMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspProcessingSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspFirstArtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspFirstArtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspNonConfRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspNonConfRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspProcListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspProcListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspRcptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspRcptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SupplierXRefRow] = obj["value"]
      pass

class Erp_Tablesets_InspFirstArtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this first article transaction applies.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the first article transaction applies to.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  An ID of the person who did the first article inspection.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FAStatus:str = obj["FAStatus"]
      """  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  System date at time inspection time.  """  
      self.ActionTime:int = obj["ActionTime"]
      """  System Time (hr-min-sec) at time of inspection.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the inspection.  """  
      self.InspectedQuantity:int = obj["InspectedQuantity"]
      """  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobAsmPartNum:str = obj["JobAsmPartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.JobAsmRevisionNum:str = obj["JobAsmRevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship with InspProcList  """  
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmployeeNumFirstName:str = obj["EmployeeNumFirstName"]
      self.EmployeeNumLastName:str = obj["EmployeeNumLastName"]
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobAsmDescription:str = obj["JobAsmDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspNonConfRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ScrapLaborCost:int = obj["ScrapLaborCost"]
      """  Scrap Labor Cost.  """  
      self.ScrapBurdenCost:int = obj["ScrapBurdenCost"]
      """  Scrap Burden Cost.  """  
      self.ScrapMaterialCost:int = obj["ScrapMaterialCost"]
      """  Scrap Material Cost.  """  
      self.ScrapMaterialBurCost:int = obj["ScrapMaterialBurCost"]
      """  Scrap Material Bur Cost.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  """  
      self.Description:str = obj["Description"]
      """  Describes the Part.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.ScrapUM:str = obj["ScrapUM"]
      """  Defines the Unit of Measure used when part is scrapped.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  The conversion factor used to convert the material.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as a foreign key for LaborDtl record.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Contains comments about the transaction.  """  
      self.FldCommentText:str = obj["FldCommentText"]
      """  Contains comments about the transaction.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Supplier Purchase Point  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Non conformance warehosue code  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.ScrapSubCost:int = obj["ScrapSubCost"]
      """  Scrap Labor Cost.  """  
      self.QtyFrm:str = obj["QtyFrm"]
      """  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  """  
      self.TranID:int = obj["TranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.Plant:str = obj["Plant"]
      """   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Receipt Number of related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Disposition Number of related RMADisp record.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the Non-Conformance transaction.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Mtl Sub Unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Material  Burd unit component cost to date  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.MoveCostsToDMR:bool = obj["MoveCostsToDMR"]
      """   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.MtlSourceTrnType:str = obj["MtlSourceTrnType"]
      """  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WrkCntrDesc:str = obj["WrkCntrDesc"]
      """  Long description of the Work Center.  """  
      self.PassedMove:bool = obj["PassedMove"]
      """  Indicator of user's request to create a MtlQueue for passed items.  """  
      self.PassedWarehouseCode:str = obj["PassedWarehouseCode"]
      """  Location to which passed items are to be moved.  """  
      self.PassedBin:str = obj["PassedBin"]
      """  Location to which passed items are to be moved.  """  
      self.FailedMove:bool = obj["FailedMove"]
      """  Indicator of user's request to create a MtlQueue for failed items.  """  
      self.FailedWarehouseCode:str = obj["FailedWarehouseCode"]
      """  Location to which failed items are to be moved.  """  
      self.FailedBin:str = obj["FailedBin"]
      """  Location to which failed items are to be moved.  """  
      self.CreateCorAct:bool = obj["CreateCorAct"]
      """  Indicator of user's request to create a Corrective Action.  """  
      self.PassedIssueTo:str = obj["PassedIssueTo"]
      """  Issue To specifies where the quantity that passed should be issued. For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  """  
      self.PassedIssuedComplete:bool = obj["PassedIssuedComplete"]
      """  Indicates whether or not the part is complete when it is issued back to the job. If the part is complete (not taken apart) when it is returned to the job, this is YES This field is available if PassedIssueTo is Job Assembly (ASM) or Job Material (MTL).  """  
      self.FailedReasonCode:str = obj["FailedReasonCode"]
      """  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  """  
      self.EnforceSerialNumCount:bool = obj["EnforceSerialNumCount"]
      """  Flag to indicate whether serial numbers will be required during inspection processing.  """  
      self.PassedJobPartNum:str = obj["PassedJobPartNum"]
      """  PartNum of Job Assembly passed part is to be issued to.  """  
      self.PassedJobPartDesc:str = obj["PassedJobPartDesc"]
      """  Description of Job Assembly passed part is to be issued to.  """  
      self.PassedJobQty:int = obj["PassedJobQty"]
      """  This is how many of the assemblies are required to produce the END ITEM.  """  
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship with InspProcList  """  
      self.FailedBinDescription:str = obj["FailedBinDescription"]
      self.FailedReasonDescription:str = obj["FailedReasonDescription"]
      self.FailedWarehouseDescription:str = obj["FailedWarehouseDescription"]
      self.PassedBinDescription:str = obj["PassedBinDescription"]
      self.PassedWarehouseDescription:str = obj["PassedWarehouseDescription"]
      self.DimQuantity:int = obj["DimQuantity"]
      """  Quantity of the material to be scrapped.  """  
      self.DimPassedQty:int = obj["DimPassedQty"]
      """  = PassedQty * DimConvFactor  """  
      self.DimFailedQty:int = obj["DimFailedQty"]
      """  = FailedQty * DimConvFactor  """  
      self.AcceptUM:str = obj["AcceptUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.TranQty:int = obj["TranQty"]
      """  The Quantity field converted to the UOM defined in the job material  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.RequiredQtyUOM:str = obj["RequiredQtyUOM"]
      self.EnableSerialTracking:bool = obj["EnableSerialTracking"]
      """  To enable/disable Serial Tracking options in UI screens.  """  
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.Done:bool = obj["Done"]
      """  It is used to print Inventory Movement after processing.  """  
      self.FailedLegalNumber:str = obj["FailedLegalNumber"]
      """  Failed Legal Number  """  
      self.FailedLegalNumberID:str = obj["FailedLegalNumberID"]
      self.FailedLegalNumberMsg:str = obj["FailedLegalNumberMsg"]
      """  Failed Legal Number Message  """  
      self.FailedTranDocTypeID:str = obj["FailedTranDocTypeID"]
      """  Failed Transaction Document Type  """  
      self.PassedTranDocTypeID:str = obj["PassedTranDocTypeID"]
      """  Passed Transaction Document Type  """  
      self.PassedLegalNumber:str = obj["PassedLegalNumber"]
      """  Passed Legal Number  """  
      self.PassedLegalNumberID:str = obj["PassedLegalNumberID"]
      """  Passed Legal Number ID  """  
      self.PassedLegalNumberMsg:str = obj["PassedLegalNumberMsg"]
      """  Passed Legal Number Message  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PassedPCID:str = obj["PassedPCID"]
      self.FailedPCID:str = obj["FailedPCID"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.ToBinNumDescription:str = obj["ToBinNumDescription"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspProcListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the machine that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.FirstArtSysDate:str = obj["FirstArtSysDate"]
      """  System date at time that record was created.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.NonConfRowIdent:str = obj["NonConfRowIdent"]
      """  RowID of related NonConf record  """  
      self.FirstArtRowIdent:str = obj["FirstArtRowIdent"]
      """  RowId of related First Art record  """  
      self.RcvDtlRowIdent:str = obj["RcvDtlRowIdent"]
      """  RowId of related RcvDtl record  """  
      self.RMARecptRowIdent:str = obj["RMARecptRowIdent"]
      """  RowId of related RMARecpt record  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship between InspProcList and child tables InspFirstArt, InspNonConf, InspRcpt  """  
      self.TrnTypDescription:str = obj["TrnTypDescription"]
      """  Description of the source of the item to be inspected: Operations,First Articles,Inventory,Material,PO Receipts,RMAs  """  
      self.EmpIDFirstName:str = obj["EmpIDFirstName"]
      self.EmpIDLastName:str = obj["EmpIDLastName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.UOM:str = obj["UOM"]
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PCID:str = obj["PCID"]
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspRcptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Indentifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Supplier master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Supplier Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  Dynamic Attribute Value Set ID for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure for this attribute set.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether the Attribute Value was auto-generated by the system.  """  
      self.PUM:str = obj["PUM"]
      """  Supplier selling Unit of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the Supplier unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """  Time of day when inspection transaction was recorded.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship with InspProcList  """  
      self.AcceptUM:str = obj["AcceptUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BinNum:str = obj["BinNum"]
      self.CreateCorAct:bool = obj["CreateCorAct"]
      """  Indicator of user's request to create a Corrective Action.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.DimFailedQty:int = obj["DimFailedQty"]
      """  = FailedQty * DimConvFactor  """  
      self.DimOurQty:int = obj["DimOurQty"]
      """  = OurQty * DimConvFactor  """  
      self.DimPassedQty:int = obj["DimPassedQty"]
      """  = PassedQty * DimConvFactor  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.Done:bool = obj["Done"]
      """  It is used to print Inventory Movement after processing.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.EnforceSerialNumCount:bool = obj["EnforceSerialNumCount"]
      """  Flag to indicate whether serial numbers will be required during inspection processing.  """  
      self.FailedBin:str = obj["FailedBin"]
      """  Location to which failed items are to be moved.  """  
      self.FailedBinDescription:str = obj["FailedBinDescription"]
      self.FailedLegalNumber:str = obj["FailedLegalNumber"]
      """  Failed Legal Number  """  
      self.FailedLegalNumberID:str = obj["FailedLegalNumberID"]
      """  Failed Legal Number ID  """  
      self.FailedLegalNumberMsg:str = obj["FailedLegalNumberMsg"]
      """  Failed Legal Number Message  """  
      self.FailedMove:bool = obj["FailedMove"]
      """  Indicator of user's request to create a MtlQueue for failed items.  """  
      self.FailedReasonCode:str = obj["FailedReasonCode"]
      """  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  """  
      self.FailedReasonDescription:str = obj["FailedReasonDescription"]
      self.FailedTranDocTypeID:str = obj["FailedTranDocTypeID"]
      """  Failed Transaction Document Type  """  
      self.FailedWarehouseCode:str = obj["FailedWarehouseCode"]
      """  Location to which failed items are to be moved.  """  
      self.FailedWarehouseDescription:str = obj["FailedWarehouseDescription"]
      self.FldCommentText:str = obj["FldCommentText"]
      """  Comments on the items failing inspection.  """  
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.IsOkToCloseJobMtl:bool = obj["IsOkToCloseJobMtl"]
      """  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this material requirement?"  """  
      self.IsOkToCloseSubContract:bool = obj["IsOkToCloseSubContract"]
      """  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this subcontract operation?"  """  
      self.IsOkToReopenJobMtl:bool = obj["IsOkToReopenJobMtl"]
      """  Holds user's response to the question: "The Job Material requirement is Closed...  do you really want it reopened?"  """  
      self.IsOkToReopenSubContract:bool = obj["IsOkToReopenSubContract"]
      """  Holds user's response to the question: "The Subcontract operation is complete...  do you really want it reopened?"  """  
      self.IsOkToUnassignSerNums:bool = obj["IsOkToUnassignSerNums"]
      """  Holds user's response to the question: "Serial numbers assigned to Job Subcontracts are not tracked.  The Serial Numbers that have been assigned to this receipt will be deselected.  Are you sure this receipt is to a Job Subcontract?"  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PassedBin:str = obj["PassedBin"]
      """  Location to which passed items are to be moved.  """  
      self.PassedBinDescription:str = obj["PassedBinDescription"]
      self.PassedIssueTo:str = obj["PassedIssueTo"]
      """  Issue To specifies where the quantity that passed should be issued.  For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  """  
      self.PassedJobIUM:str = obj["PassedJobIUM"]
      self.PassedJobPartDesc:str = obj["PassedJobPartDesc"]
      """  Description of Job Assembly passed part is to be issued to.  """  
      self.PassedJobPartNum:str = obj["PassedJobPartNum"]
      """  PartNum of Job Assembly passed part is to be issued to.  """  
      self.PassedJobQty:int = obj["PassedJobQty"]
      """  This is how many of the assemblies are required to produce the END ITEM.  """  
      self.PassedLegalNumber:str = obj["PassedLegalNumber"]
      """  Passed Legal Number  """  
      self.PassedLegalNumberID:str = obj["PassedLegalNumberID"]
      """  Passed Legal Number ID  """  
      self.PassedLegalNumberMsg:str = obj["PassedLegalNumberMsg"]
      """  Passed Legal Number Message  """  
      self.PassedMove:bool = obj["PassedMove"]
      """  Indicator of user's request to create a MtlQueue for passed items.  """  
      self.PassedTranDocTypeID:str = obj["PassedTranDocTypeID"]
      """  Passed Transaction Document Type  """  
      self.PassedWarehouseCode:str = obj["PassedWarehouseCode"]
      """  Location to which passed items are to be moved  """  
      self.PassedWarehouseDescription:str = obj["PassedWarehouseDescription"]
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.POHeaderComment:str = obj["POHeaderComment"]
      """  Contains comments about over all  purchase order. These will be printed on the purchase order.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Comments on items passing inspection.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers. - This description was for when InspRcpt was tied to RcvDtl  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.TranQty:int = obj["TranQty"]
      """  The Quantity field converted to the UOM defined in the job material  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  Was a link column on RcvDtl.  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Was a link column on RcvDtl.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """  Was a link column on RcvDtl.  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Was a link column on RcvDtl.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  Was a link column on RcvDtl.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Was a link column on RcvDtl.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Was a link column on RcvDtl.  """  
      self.PCID:str = obj["PCID"]
      self.FailedPCID:str = obj["FailedPCID"]
      self.PassedPCID:str = obj["PassedPCID"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MfgID:str = obj["MfgID"]
      self.MfgName:str = obj["MfgName"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
      self.PartNum:str = obj["PartNum"]
      self.POReference:bool = obj["POReference"]
      self.Receipt:bool = obj["Receipt"]
      self.VendNum:int = obj["VendNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.Invoice:bool = obj["Invoice"]
      self.RcvXRefNum:int = obj["RcvXRefNum"]
      """  RcvXRefNum  """  
      self.Inspected:bool = obj["Inspected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignInspectorFar_input:
   """ Required : 
   pcInspectorID
   ds
   """  
   def __init__(self, obj):
      self.pcInspectorID:str = obj["pcInspectorID"]
      """  (optional) The Inspector ID typed in by the user.  """  
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class AssignInspectorFar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignInspectorNonConf_input:
   """ Required : 
   pcInspectorID
   ds
   """  
   def __init__(self, obj):
      self.pcInspectorID:str = obj["pcInspectorID"]
      """  (optional) The Inspector ID typed in by the user.  """  
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class AssignInspectorNonConf_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.infoMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class AssignInspectorReceipt_input:
   """ Required : 
   pcInspectorID
   ds
   """  
   def __init__(self, obj):
      self.pcInspectorID:str = obj["pcInspectorID"]
      """  (optional) The Inspector ID typed in by the user.  """  
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class AssignInspectorReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.infoMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPlanningContractBin_input:
   """ Required : 
   ds
   pcSource
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      pass

class CheckPlanningContractBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcPCBinAction:str = obj["parameters"]
      self.pcPCBinMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckSerialNumCount_input:
   """ Required : 
   ds
   pcSource
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      """  "NonConf" or "Receipt"  """  
      pass

class CheckSerialNumCount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ConvQtysToBase_input:
   """ Required : 
   pcPartNum
   piQuantity
   piPassedQty
   piFailedQty
   pcAcceptUM
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  AcceptUM.  """  
      self.piQuantity:int = obj["piQuantity"]
      """  dimQuantity.  """  
      self.piPassedQty:int = obj["piPassedQty"]
      """  dimPassedQty.  """  
      self.piFailedQty:int = obj["piFailedQty"]
      """  dimFailedQty.  """  
      self.pcAcceptUM:str = obj["pcAcceptUM"]
      """  AcceptUM.  """  
      pass

class ConvQtysToBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.piBaseQty:int = obj["parameters"]
      self.piBasePassQty:int = obj["parameters"]
      self.piBaseFailQty:int = obj["parameters"]
      pass

      """  output parameters  """  

class DisplayWarnMsg_input:
   """ Required : 
   PartTranType
   JobNum
   AsmSeq
   JobSeq
   """  
   def __init__(self, obj):
      self.PartTranType:str = obj["PartTranType"]
      self.JobNum:str = obj["JobNum"]
      self.AsmSeq:int = obj["AsmSeq"]
      self.JobSeq:int = obj["JobSeq"]
      pass

class DisplayWarnMsg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_InspFirstArtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this first article transaction applies.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the first article transaction applies to.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  An ID of the person who did the first article inspection.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FAStatus:str = obj["FAStatus"]
      """  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  System date at time inspection time.  """  
      self.ActionTime:int = obj["ActionTime"]
      """  System Time (hr-min-sec) at time of inspection.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the inspection.  """  
      self.InspectedQuantity:int = obj["InspectedQuantity"]
      """  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobAsmPartNum:str = obj["JobAsmPartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.JobAsmRevisionNum:str = obj["JobAsmRevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship with InspProcList  """  
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmployeeNumFirstName:str = obj["EmployeeNumFirstName"]
      self.EmployeeNumLastName:str = obj["EmployeeNumLastName"]
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobAsmDescription:str = obj["JobAsmDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspNonConfRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ScrapLaborCost:int = obj["ScrapLaborCost"]
      """  Scrap Labor Cost.  """  
      self.ScrapBurdenCost:int = obj["ScrapBurdenCost"]
      """  Scrap Burden Cost.  """  
      self.ScrapMaterialCost:int = obj["ScrapMaterialCost"]
      """  Scrap Material Cost.  """  
      self.ScrapMaterialBurCost:int = obj["ScrapMaterialBurCost"]
      """  Scrap Material Bur Cost.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  """  
      self.Description:str = obj["Description"]
      """  Describes the Part.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.ScrapUM:str = obj["ScrapUM"]
      """  Defines the Unit of Measure used when part is scrapped.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  The conversion factor used to convert the material.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as a foreign key for LaborDtl record.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Contains comments about the transaction.  """  
      self.FldCommentText:str = obj["FldCommentText"]
      """  Contains comments about the transaction.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Supplier Purchase Point  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Non conformance warehosue code  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.ScrapSubCost:int = obj["ScrapSubCost"]
      """  Scrap Labor Cost.  """  
      self.QtyFrm:str = obj["QtyFrm"]
      """  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  """  
      self.TranID:int = obj["TranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.Plant:str = obj["Plant"]
      """   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Receipt Number of related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Disposition Number of related RMADisp record.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the Non-Conformance transaction.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Mtl Sub Unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Material  Burd unit component cost to date  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.MoveCostsToDMR:bool = obj["MoveCostsToDMR"]
      """   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.MtlSourceTrnType:str = obj["MtlSourceTrnType"]
      """  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WrkCntrDesc:str = obj["WrkCntrDesc"]
      """  Long description of the Work Center.  """  
      self.PassedMove:bool = obj["PassedMove"]
      """  Indicator of user's request to create a MtlQueue for passed items.  """  
      self.PassedWarehouseCode:str = obj["PassedWarehouseCode"]
      """  Location to which passed items are to be moved.  """  
      self.PassedBin:str = obj["PassedBin"]
      """  Location to which passed items are to be moved.  """  
      self.FailedMove:bool = obj["FailedMove"]
      """  Indicator of user's request to create a MtlQueue for failed items.  """  
      self.FailedWarehouseCode:str = obj["FailedWarehouseCode"]
      """  Location to which failed items are to be moved.  """  
      self.FailedBin:str = obj["FailedBin"]
      """  Location to which failed items are to be moved.  """  
      self.CreateCorAct:bool = obj["CreateCorAct"]
      """  Indicator of user's request to create a Corrective Action.  """  
      self.PassedIssueTo:str = obj["PassedIssueTo"]
      """  Issue To specifies where the quantity that passed should be issued. For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  """  
      self.PassedIssuedComplete:bool = obj["PassedIssuedComplete"]
      """  Indicates whether or not the part is complete when it is issued back to the job. If the part is complete (not taken apart) when it is returned to the job, this is YES This field is available if PassedIssueTo is Job Assembly (ASM) or Job Material (MTL).  """  
      self.FailedReasonCode:str = obj["FailedReasonCode"]
      """  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  """  
      self.EnforceSerialNumCount:bool = obj["EnforceSerialNumCount"]
      """  Flag to indicate whether serial numbers will be required during inspection processing.  """  
      self.PassedJobPartNum:str = obj["PassedJobPartNum"]
      """  PartNum of Job Assembly passed part is to be issued to.  """  
      self.PassedJobPartDesc:str = obj["PassedJobPartDesc"]
      """  Description of Job Assembly passed part is to be issued to.  """  
      self.PassedJobQty:int = obj["PassedJobQty"]
      """  This is how many of the assemblies are required to produce the END ITEM.  """  
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship with InspProcList  """  
      self.FailedBinDescription:str = obj["FailedBinDescription"]
      self.FailedReasonDescription:str = obj["FailedReasonDescription"]
      self.FailedWarehouseDescription:str = obj["FailedWarehouseDescription"]
      self.PassedBinDescription:str = obj["PassedBinDescription"]
      self.PassedWarehouseDescription:str = obj["PassedWarehouseDescription"]
      self.DimQuantity:int = obj["DimQuantity"]
      """  Quantity of the material to be scrapped.  """  
      self.DimPassedQty:int = obj["DimPassedQty"]
      """  = PassedQty * DimConvFactor  """  
      self.DimFailedQty:int = obj["DimFailedQty"]
      """  = FailedQty * DimConvFactor  """  
      self.AcceptUM:str = obj["AcceptUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.TranQty:int = obj["TranQty"]
      """  The Quantity field converted to the UOM defined in the job material  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.RequiredQtyUOM:str = obj["RequiredQtyUOM"]
      self.EnableSerialTracking:bool = obj["EnableSerialTracking"]
      """  To enable/disable Serial Tracking options in UI screens.  """  
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.Done:bool = obj["Done"]
      """  It is used to print Inventory Movement after processing.  """  
      self.FailedLegalNumber:str = obj["FailedLegalNumber"]
      """  Failed Legal Number  """  
      self.FailedLegalNumberID:str = obj["FailedLegalNumberID"]
      self.FailedLegalNumberMsg:str = obj["FailedLegalNumberMsg"]
      """  Failed Legal Number Message  """  
      self.FailedTranDocTypeID:str = obj["FailedTranDocTypeID"]
      """  Failed Transaction Document Type  """  
      self.PassedTranDocTypeID:str = obj["PassedTranDocTypeID"]
      """  Passed Transaction Document Type  """  
      self.PassedLegalNumber:str = obj["PassedLegalNumber"]
      """  Passed Legal Number  """  
      self.PassedLegalNumberID:str = obj["PassedLegalNumberID"]
      """  Passed Legal Number ID  """  
      self.PassedLegalNumberMsg:str = obj["PassedLegalNumberMsg"]
      """  Passed Legal Number Message  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PassedPCID:str = obj["PassedPCID"]
      self.FailedPCID:str = obj["FailedPCID"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.ToBinNumDescription:str = obj["ToBinNumDescription"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspProcListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the machine that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.FirstArtSysDate:str = obj["FirstArtSysDate"]
      """  System date at time that record was created.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.NonConfRowIdent:str = obj["NonConfRowIdent"]
      """  RowID of related NonConf record  """  
      self.FirstArtRowIdent:str = obj["FirstArtRowIdent"]
      """  RowId of related First Art record  """  
      self.RcvDtlRowIdent:str = obj["RcvDtlRowIdent"]
      """  RowId of related RcvDtl record  """  
      self.RMARecptRowIdent:str = obj["RMARecptRowIdent"]
      """  RowId of related RMARecpt record  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship between InspProcList and child tables InspFirstArt, InspNonConf, InspRcpt  """  
      self.TrnTypDescription:str = obj["TrnTypDescription"]
      """  Description of the source of the item to be inspected: Operations,First Articles,Inventory,Material,PO Receipts,RMAs  """  
      self.EmpIDFirstName:str = obj["EmpIDFirstName"]
      self.EmpIDLastName:str = obj["EmpIDLastName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.UOM:str = obj["UOM"]
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PCID:str = obj["PCID"]
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspProcessingTableset:
   def __init__(self, obj):
      self.InspProcList:list[Erp_Tablesets_InspProcListRow] = obj["InspProcList"]
      self.InspFirstArt:list[Erp_Tablesets_InspFirstArtRow] = obj["InspFirstArt"]
      self.InspNonConf:list[Erp_Tablesets_InspNonConfRow] = obj["InspNonConf"]
      self.InspRcpt:list[Erp_Tablesets_InspRcptRow] = obj["InspRcpt"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.SupplierXRef:list[Erp_Tablesets_SupplierXRefRow] = obj["SupplierXRef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InspRcptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Indentifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Supplier master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Supplier Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  Dynamic Attribute Value Set ID for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure for this attribute set.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether the Attribute Value was auto-generated by the system.  """  
      self.PUM:str = obj["PUM"]
      """  Supplier selling Unit of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the Supplier unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """  Time of day when inspection transaction was recorded.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.xID:str = obj["xID"]
      """  Unique ID field to establish relationship with InspProcList  """  
      self.AcceptUM:str = obj["AcceptUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BinNum:str = obj["BinNum"]
      self.CreateCorAct:bool = obj["CreateCorAct"]
      """  Indicator of user's request to create a Corrective Action.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.DimFailedQty:int = obj["DimFailedQty"]
      """  = FailedQty * DimConvFactor  """  
      self.DimOurQty:int = obj["DimOurQty"]
      """  = OurQty * DimConvFactor  """  
      self.DimPassedQty:int = obj["DimPassedQty"]
      """  = PassedQty * DimConvFactor  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.Done:bool = obj["Done"]
      """  It is used to print Inventory Movement after processing.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.EnforceSerialNumCount:bool = obj["EnforceSerialNumCount"]
      """  Flag to indicate whether serial numbers will be required during inspection processing.  """  
      self.FailedBin:str = obj["FailedBin"]
      """  Location to which failed items are to be moved.  """  
      self.FailedBinDescription:str = obj["FailedBinDescription"]
      self.FailedLegalNumber:str = obj["FailedLegalNumber"]
      """  Failed Legal Number  """  
      self.FailedLegalNumberID:str = obj["FailedLegalNumberID"]
      """  Failed Legal Number ID  """  
      self.FailedLegalNumberMsg:str = obj["FailedLegalNumberMsg"]
      """  Failed Legal Number Message  """  
      self.FailedMove:bool = obj["FailedMove"]
      """  Indicator of user's request to create a MtlQueue for failed items.  """  
      self.FailedReasonCode:str = obj["FailedReasonCode"]
      """  Reason the item failed inspection.  Must correspond to an existing Reason master record of type 'D'.  """  
      self.FailedReasonDescription:str = obj["FailedReasonDescription"]
      self.FailedTranDocTypeID:str = obj["FailedTranDocTypeID"]
      """  Failed Transaction Document Type  """  
      self.FailedWarehouseCode:str = obj["FailedWarehouseCode"]
      """  Location to which failed items are to be moved.  """  
      self.FailedWarehouseDescription:str = obj["FailedWarehouseDescription"]
      self.FldCommentText:str = obj["FldCommentText"]
      """  Comments on the items failing inspection.  """  
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.InspDataRequired:bool = obj["InspDataRequired"]
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.IsOkToCloseJobMtl:bool = obj["IsOkToCloseJobMtl"]
      """  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this material requirement?"  """  
      self.IsOkToCloseSubContract:bool = obj["IsOkToCloseSubContract"]
      """  Holds user's response to the question: "Quantity issued is less than requirement...  Are you sure you want to close this subcontract operation?"  """  
      self.IsOkToReopenJobMtl:bool = obj["IsOkToReopenJobMtl"]
      """  Holds user's response to the question: "The Job Material requirement is Closed...  do you really want it reopened?"  """  
      self.IsOkToReopenSubContract:bool = obj["IsOkToReopenSubContract"]
      """  Holds user's response to the question: "The Subcontract operation is complete...  do you really want it reopened?"  """  
      self.IsOkToUnassignSerNums:bool = obj["IsOkToUnassignSerNums"]
      """  Holds user's response to the question: "Serial numbers assigned to Job Subcontracts are not tracked.  The Serial Numbers that have been assigned to this receipt will be deselected.  Are you sure this receipt is to a Job Subcontract?"  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PassedBin:str = obj["PassedBin"]
      """  Location to which passed items are to be moved.  """  
      self.PassedBinDescription:str = obj["PassedBinDescription"]
      self.PassedIssueTo:str = obj["PassedIssueTo"]
      """  Issue To specifies where the quantity that passed should be issued.  For Inventory, Material, and PO Receipts inspections, three choices are available: Stock (STK), Job Assembly (ASM), Job Material (MTL)  """  
      self.PassedJobIUM:str = obj["PassedJobIUM"]
      self.PassedJobPartDesc:str = obj["PassedJobPartDesc"]
      """  Description of Job Assembly passed part is to be issued to.  """  
      self.PassedJobPartNum:str = obj["PassedJobPartNum"]
      """  PartNum of Job Assembly passed part is to be issued to.  """  
      self.PassedJobQty:int = obj["PassedJobQty"]
      """  This is how many of the assemblies are required to produce the END ITEM.  """  
      self.PassedLegalNumber:str = obj["PassedLegalNumber"]
      """  Passed Legal Number  """  
      self.PassedLegalNumberID:str = obj["PassedLegalNumberID"]
      """  Passed Legal Number ID  """  
      self.PassedLegalNumberMsg:str = obj["PassedLegalNumberMsg"]
      """  Passed Legal Number Message  """  
      self.PassedMove:bool = obj["PassedMove"]
      """  Indicator of user's request to create a MtlQueue for passed items.  """  
      self.PassedTranDocTypeID:str = obj["PassedTranDocTypeID"]
      """  Passed Transaction Document Type  """  
      self.PassedWarehouseCode:str = obj["PassedWarehouseCode"]
      """  Location to which passed items are to be moved  """  
      self.PassedWarehouseDescription:str = obj["PassedWarehouseDescription"]
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.POHeaderComment:str = obj["POHeaderComment"]
      """  Contains comments about over all  purchase order. These will be printed on the purchase order.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Comments on items passing inspection.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers. - This description was for when InspRcpt was tied to RcvDtl  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.TranQty:int = obj["TranQty"]
      """  The Quantity field converted to the UOM defined in the job material  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  Was a link column on RcvDtl.  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Was a link column on RcvDtl.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  Was a link column on RcvDtl.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """  Was a link column on RcvDtl.  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Was a link column on RcvDtl.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  Was a link column on RcvDtl.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Was a link column on RcvDtl.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Was a link column on RcvDtl.  """  
      self.PCID:str = obj["PCID"]
      self.FailedPCID:str = obj["FailedPCID"]
      self.PassedPCID:str = obj["PassedPCID"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MfgID:str = obj["MfgID"]
      self.MfgName:str = obj["MfgName"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
      self.PartNum:str = obj["PartNum"]
      self.POReference:bool = obj["POReference"]
      self.Receipt:bool = obj["Receipt"]
      self.VendNum:int = obj["VendNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.Invoice:bool = obj["Invoice"]
      self.RcvXRefNum:int = obj["RcvXRefNum"]
      """  RcvXRefNum  """  
      self.Inspected:bool = obj["Inspected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   pcTranID
   """  
   def __init__(self, obj):
      self.pcTranID:int = obj["pcTranID"]
      """  The TranID of the NonConformance.  """  
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspProcessingTableset] = obj["returnObj"]
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

class GetDateUser_input:
   """ Required : 
   pText
   """  
   def __init__(self, obj):
      self.pText:str = obj["pText"]
      pass

class GetDateUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFailedLegalNumGenOpts_input:
   """ Required : 
   ds
   inspectionType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.inspectionType:str = obj["inspectionType"]
      """  The type of inspection: Inventory, Material, Operation, Receipt  """  
      pass

class GetFailedLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class GetFirstArtByID_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   piOprSeq
   pcResourceID
   piSeqNum
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  The JobNum of the First Article.  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  The AssemblySeq of the First Article.  """  
      self.piOprSeq:int = obj["piOprSeq"]
      """  The OprSeq of the First Article.  """  
      self.pcResourceID:str = obj["pcResourceID"]
      """  The ResourceID of the First Article.  """  
      self.piSeqNum:int = obj["piSeqNum"]
      """  The SeqNum of the First Article.  """  
      pass

class GetFirstArtByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspProcessingTableset] = obj["returnObj"]
      pass

class GetInspRcptSelectedSerialNumbers_input:
   """ Required : 
   pcInspRcptRowIdent
   ds
   """  
   def __init__(self, obj):
      self.pcInspRcptRowIdent:str = obj["pcInspRcptRowIdent"]
      """  Input RowIdent field  of InspRcpt datatable  """  
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class GetInspRcptSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetInspResultsPassFail_input:
   """ Required : 
   ds
   ipSource
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.ipSource:str = obj["ipSource"]
      """  "NonConf", "Receipt", "FirstArt"  """  
      pass

class GetInspResultsPassFail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.totPassed:int = obj["parameters"]
      self.totFailed:int = obj["parameters"]
      self.inspDataEntered:bool = obj["inspDataEntered"]
      pass

      """  output parameters  """  

class GetMtlQueueSeqValue_input:
   """ Required : 
   inspectionType
   company
   nonConfTranID
   vendorNum
   purPoint
   packSlip
   packLine
   tranType
   """  
   def __init__(self, obj):
      self.inspectionType:str = obj["inspectionType"]
      self.company:str = obj["company"]
      self.nonConfTranID:int = obj["nonConfTranID"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      self.tranType:str = obj["tranType"]
      pass

class GetMtlQueueSeqValue_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetNonConfPartTranPKs_input:
   """ Required : 
   ipNonConfID
   ipDMRNum
   ipPassedIssueTo
   """  
   def __init__(self, obj):
      self.ipNonConfID:int = obj["ipNonConfID"]
      """  ipNonConfID  """  
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  DMR number  """  
      self.ipPassedIssueTo:str = obj["ipPassedIssueTo"]
      """  PassedIssueTo  """  
      pass

class GetNonConfPartTranPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPassedLegalNumGenOpts_input:
   """ Required : 
   ds
   inspectionType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.inspectionType:str = obj["inspectionType"]
      """  The type of inspection: Inventory, Material, Operation, Receipt  """  
      pass

class GetPassedLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class GetReceiptByID_input:
   """ Required : 
   piVendorNum
   pcPurPoint
   pcPackSlip
   piPackLine
   """  
   def __init__(self, obj):
      self.piVendorNum:int = obj["piVendorNum"]
      """  The VendorNum of the Receipt.  """  
      self.pcPurPoint:str = obj["pcPurPoint"]
      """  The PurPoint of the Receipt.  """  
      self.pcPackSlip:str = obj["pcPackSlip"]
      """  The PackSlip of the Receipt.  """  
      self.piPackLine:int = obj["piPackLine"]
      """  The PackLine of the Receipt.  """  
      pass

class GetReceiptByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspProcessingTableset] = obj["returnObj"]
      pass

class GetReceiptPartTranPKs_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipPackLine
   ipDMRNum
   ipPassedIssueTo
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor number  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  PurPoint  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  PackSlip  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  PackLine  """  
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  DMR number  """  
      self.ipPassedIssueTo:str = obj["ipPassedIssueTo"]
      """  PassedIssueTo  """  
      pass

class GetReceiptPartTranPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsLP_input:
   """ Required : 
   tranType
   whereClauseInspProcList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.tranType:str = obj["tranType"]
      """  Indicates the Transaction Type of the items to be retrieved. Valid values: ALL = All items, OPR = Job Operation, MTL = Job Material, INV = Inventory, FAR = First Article, POR = PO Receipt, and RMA = RMA  """  
      self.whereClauseInspProcList:str = obj["whereClauseInspProcList"]
      """  Includes the additional Where conditions to be applied to the result set, especially the PartNum condition.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsLP_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspProcessingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   plOperation
   plMaterial
   plInventory
   plFirstArt
   plReceipt
   plRMA
   pcInspectorID
   pcCutOffDate
   whereClauseNonConf
   whereClauseFirstArt
   whereClauseRcvDtl
   whereClauseRMA
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   whereClauseInspProcList
   sortBy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.plOperation:bool = obj["plOperation"]
      """  If TRUE, include items that were sent to Inspection from a Job Operation.  """  
      self.plMaterial:bool = obj["plMaterial"]
      """  If TRUE, include items that were sent to Inspection from a Job Material.  """  
      self.plInventory:bool = obj["plInventory"]
      """  If TRUE, include items that were sent to Inspection from Inventory.  """  
      self.plFirstArt:bool = obj["plFirstArt"]
      """  If TRUE, include items that were sent to Inspection from a First Article.  """  
      self.plReceipt:bool = obj["plReceipt"]
      """  If TRUE, include items that were sent to Inspection from a PO or SubContract receipt.  """  
      self.plRMA:bool = obj["plRMA"]
      """  If TRUE, include items that were sent to Inspection from an RMA.  """  
      self.pcInspectorID:str = obj["pcInspectorID"]
      """  (optional) The Inspector ID typed in by the user.  """  
      self.pcCutOffDate:str = obj["pcCutOffDate"]
      """  (optional) Cut Off Date .  """  
      self.whereClauseNonConf:str = obj["whereClauseNonConf"]
      """  (optional)Additional Where conditions for NonConf table.  """  
      self.whereClauseFirstArt:str = obj["whereClauseFirstArt"]
      """  (optional)Additional Where conditions for FirstArt table.  """  
      self.whereClauseRcvDtl:str = obj["whereClauseRcvDtl"]
      """  (optional)Additional Where conditions for RcvDtl table.  """  
      self.whereClauseRMA:str = obj["whereClauseRMA"]
      """  (optional)Additional Where conditions for RMAHead table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  (optional)Additional Where conditions for SelectedSerialNumbers table.  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  (optional)Additional Where conditions for SNFormat table.  """  
      self.whereClauseInspProcList:str = obj["whereClauseInspProcList"]
      """  (optional)Additional Where conditions to be applied to result set.  """  
      self.sortBy:str = obj["sortBy"]
      """  Sort By selected in search  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspProcessingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectedSerialNumbers_input:
   """ Required : 
   pcInspNonConfRowIdent
   ds
   """  
   def __init__(self, obj):
      self.pcInspNonConfRowIdent:str = obj["pcInspNonConfRowIdent"]
      """  Input RowIdent field  of InspNonConf datatable  """  
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class GetSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

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

class InspectFirstArt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectFirstArt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectInventory2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectInventory2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.message:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectInventory_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectInventory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectMaterial2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectMaterial2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.message:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectMaterial_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectMaterial_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectOperation2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectOperation2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.message:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectOperation_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectOperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectReceipt2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectReceipt2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.message:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.iNonConfID:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InspectReceipt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class InspectReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.iDMRNum:int = obj["parameters"]
      self.iNonConfID:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAssemblySeq_input:
   """ Required : 
   ds
   pcSource
   piProposedAssemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      """  "NonConf" or "Receipt"  """  
      self.piProposedAssemblySeq:int = obj["piProposedAssemblySeq"]
      """  The new proposed Assembly Seq value  """  
      pass

class OnChangeAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFAInspectedQty_input:
   """ Required : 
   ds
   pdInspectedQuantity
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pdInspectedQuantity:int = obj["pdInspectedQuantity"]
      """  The new proposed Inspected Quantity value  """  
      pass

class OnChangeFAInspectedQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeFailedQty_input:
   """ Required : 
   ds
   pcSource
   pdProposedFailedQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      """  "NonConf" or "Receipt"  """  
      self.pdProposedFailedQty:int = obj["pdProposedFailedQty"]
      """  The new proposed Failed Quantity value  """  
      pass

class OnChangeFailedQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.infoMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeIssueComplete_input:
   """ Required : 
   ds
   pcSource
   plProposedIssuedComplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      """  "NonConf" or "Receipt"  """  
      self.plProposedIssuedComplete:bool = obj["plProposedIssuedComplete"]
      """  The new proposed Issued Complete value  """  
      pass

class OnChangeIssueComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcWarningMsg:str = obj["parameters"]
      self.pcResponseField:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   ds
   pcSource
   pcProposedJobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      """  "NonConf" or "Receipt"  """  
      self.pcProposedJobNum:str = obj["pcProposedJobNum"]
      """  The new proposed Job Number value  """  
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeJobSeq_input:
   """ Required : 
   ds
   piProposedJobSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.piProposedJobSeq:int = obj["piProposedJobSeq"]
      """  The new proposed Job Sequence Number value  """  
      pass

class OnChangeJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeMtlSeq_input:
   """ Required : 
   ds
   piProposedMtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.piProposedMtlSeq:int = obj["piProposedMtlSeq"]
      """  The new proposed Material Sequence Number value  """  
      pass

class OnChangeMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePCID_input:
   """ Required : 
   pcid
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.pCallProcess:str = obj["pCallProcess"]
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

class OnChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePassedIssueTo_input:
   """ Required : 
   ds
   pcSource
   pcProposedIssueTo
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      """  "NonConf" or "Receipt"  """  
      self.pcProposedIssueTo:str = obj["pcProposedIssueTo"]
      """  The new proposed PassedIssueTo value  """  
      pass

class OnChangePassedIssueTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePassedQty_input:
   """ Required : 
   ds
   pcSource
   pdProposedPassedQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      """  "NonConf" or "Receipt"  """  
      self.pdProposedPassedQty:int = obj["pdProposedPassedQty"]
      """  The new proposed Passed Quantity value  """  
      pass

class OnChangePassedQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.infoMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePassedWhse_input:
   """ Required : 
   ds
   pcSource
   pcWhseType
   pdProposedWhse
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      self.pcSource:str = obj["pcSource"]
      self.pcWhseType:str = obj["pcWhseType"]
      self.pdProposedWhse:str = obj["pdProposedWhse"]
      pass

class OnChangePassedWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ipPartNum
   ipSerialNo
   ipVendorNum
   ipJobNum
   ipAsmSeq
   ipSubOprSeq
   ipPackSlip
   ipPackLine
   ipReceivedTo
   ipJobSeqType
   isRcpt
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      self.ipSerialNo:str = obj["ipSerialNo"]
      """  Serial Number  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor Number  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Number  """  
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      """  Vendor Number  """  
      self.ipSubOprSeq:int = obj["ipSubOprSeq"]
      """  Job Operation Number  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  Pack Slip  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Pack Slip Line  """  
      self.ipReceivedTo:str = obj["ipReceivedTo"]
      """  Received To  """  
      self.ipJobSeqType:str = obj["ipJobSeqType"]
      """  Job Sequence type  """  
      self.isRcpt:bool = obj["isRcpt"]
      """  Indicates whether the Serial Numbers are being entered for inspection from Receipt  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateTranDocType_input:
   """ Required : 
   ipTranDocTypeID
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  Transaction Document Type ID to be validated  """  
      pass

class ValidateTranDocType_output:
   def __init__(self, obj):
      pass

